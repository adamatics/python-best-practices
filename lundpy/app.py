import fastapi
import uvicorn
from fastapi import Request

app=fastapi.FastAPI()

@app.get('/')
async def read_root():
 return {"message":"Hello, World"}

@app.get('/items/{item_id}')
async def read_item(item_id):
 return {"item_id":item_id}

@app.post('/items/')
async def create_item(item:dict):
    return {"item":item}

@app.get('/users/{user_id}')
def get_user(user_id:int):
 return {"user_id":user_id}

@app.post('/users/')
def create_user(user:dict):
 return {"user":user}

if __name__=='__main__':
 uvicorn.run(app,host='127.0.0.1',port=8000)

# Problems with this file
# *	Inconsistent indentation (mix of 2 and 4 spaces).
# * Missing type hints for function parameters and return types.
# * No linting or formatting applied.
# * Inconsistent spacing around operators.
# * No code structure or organization (all code in one file).