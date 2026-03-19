from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Running"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    topic = data.get("topic")

    tasks = [
        f"Day 1: Basics of {topic}",
        f"Day 2: Practice {topic}",
        f"Day 3: Mini project",
        f"Day 4: Revision",
        f"Day 5: Final project"
    ]

    return jsonify({"tasks": tasks})

if __name__ == '__main__':
    app.run(debug=True)