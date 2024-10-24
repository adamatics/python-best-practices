from fastapi.testclient import TestClient
from unittest.mock import patch
from lundpy.app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World"}

def test_get_post_without_mock():
    response = client.get("/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data

@patch("lundpy.app.requests.get")
def test_get_post_with_mock(mock_get):
    # Define the mock response data
    mock_response = {
        "userId": 1,
        "id": 1,
        "title": "Mocked Title",
        "body": "Mocked body content"
    }

    # Configure the mock to return a response with the mock data
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    response = client.get("/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data == mock_response

@patch("lundpy.app.requests.post")
def test_create_post_with_mock(mock_post):
    # Define the mock request data and response
    new_post = {
        "title": "Test Post",
        "body": "This is a test post.",
        "userId": 1
    }
    mock_response = {
        "id": 101,  # Assuming the next ID
        **new_post
    }

    # Configure the mock to return a response with the mock data
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = mock_response

    response = client.post("/posts", json=new_post)
    assert response.status_code == 200
    data = response.json()
    assert data == mock_response