from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world from smart-snippet server"

@app.route("/test_server")
def test_server():
    return "Smart-snippet server running"

@app.route("/submit_query", methods=['POST'])
def submit_query():
    return "query submitted"

@app.route("/submit_reviewed_snippet", methods=['POST'])
def submit_reviewed_snippet():
    return "reviewed snippet submitted"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
