import sqlite3
from Todo import Todo
from pprint import pprint

class TodoDAO:
    
    def __init__(self,db_file):
        self._con = sqlite3.connect(db_file)
        
    def save(self,todo:Todo):
        cur = self._con.cursor()
        
        sql_inser = f"""INSERT INTO 
todos_tbl(user_id,title,completed) 
VALUES(
    {todo.userId},
    '{todo.title}',
    {todo.completed}
    )
"""
        cur.execute(sql_inser)
        self._con.commit()
        
    
    def findAll(self):
        # allTodos=[]
        cur = self._con.cursor()
        res = cur.execute("SELECT id,user_id,title,completed FROM todos_tbl")
        data = res.fetchall()
        for d in data:
            t = Todo(*d)
            yield t
            # allTodos.append(t)
        
            # return allTodos
    
    def __del__(self):
        self._con.close()