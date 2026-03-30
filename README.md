# AI Study Assistant

## About
An AI-powered study assistant that generates structured study plans for any topic.

## Tech Stack
- FastAPI
- Python
- HTML, CSS, JavaScript
- OpenAI API

## How to Run

1. Clone the repo:git clone https://github.com/diksha-codess/ai-study-assistant.git


2. Go to project folder:

cd ai-study-assistant


3. Create virtual environment:

python -m venv venv
venv\Scripts\activate


4. Install dependencies:

pip install -r requirements.txt


5. Add your OpenAI API key in `app.py`:

client = OpenAI(api_key="YOUR_API_KEY")


6. Run backend:

uvicorn app:app --reload


7. Open frontend:

frontend/index.html


## Features
- AI-generated study plans
- Simple and fast UI
- Helps students organize learning

## Future Scope
- Quiz generator
- Progress tracking
- Personalized learning paths
