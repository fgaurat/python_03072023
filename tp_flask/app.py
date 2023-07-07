from flask import Flask
from TodoDAO import TodoDAO
app = Flask(__name__)

@app.route("/")
def hello_world():
    dao = TodoDAO('todos_db.db')
    
    html=""
    for todo in dao.findAll():
        html+=f"<li>{todo.title}</li>"
        
    
    return f"<ul>{html}</ul>"