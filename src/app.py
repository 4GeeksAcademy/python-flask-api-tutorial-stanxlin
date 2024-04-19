from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [{"label": "My first task", "done": False}]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def hello_world():
    request_body = request.json
    print("Request with this body: ", request_body)
    todos.append(request_body)
    return jsonfiy(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("Position of the item to delete:", position)
    todos.pop(position)
    return jsonify(todos)

# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)