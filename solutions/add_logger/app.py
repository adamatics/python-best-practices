from flask import Flask
import random
import logging  # Added import

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

quotes = [
    "Code is like humor. When you have to explain it, it’s bad.",
    "Fix the cause, not the symptom.",
    "Optimism is an occupational hazard of programming.",
    "Welcome to the Python Best Practices Workshop!"
]

@app.route('/')
def hello():
    quote = random.choice(quotes)
    logger.info(f"Quote displayed: {quote}")  # Added logging
    return quote

if __name__ == '__main__':
    logger.info("Starting the Flask app...")  # Added logging
    app.run(debug=True)
