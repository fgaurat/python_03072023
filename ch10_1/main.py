import sys
import requests
import sqlite3
from TodoDAO import TodoDAO
from Todo import Todo
import configparser
import argparse


def main():
    parser = argparse.ArgumentParser(
                prog='TodoDAO',
                description='ça fait des trucs',
                epilog='la fin de l\'aide')
    # parser.add_argument("config",help="config file")
    parser.add_argument("-c","--config",help="config file",default="config.ini")
    args = parser.parse_args()
    args.config
    
    config = configparser.ConfigParser()
    config.read(args.config)
    
    dao = TodoDAO(config['DB']['db_file'])
    todos = dao.findAll()
    l = list(todos)
    print(l)
    # for todo in todos:
    #     print(todo)
        
        
        
def main_save_todos():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    todos = response.json()    
    dao = TodoDAO("todos_db.db")
    for todo in todos:
        t=Todo(**todo)
        dao.save(t)
        





def main_test_todo():
    dao = TodoDAO("todos_db.db")
    # all_todos = dao.findAll()
    t = Todo(userId=12,title="Le titre",completed=True)
    dao.save(t)
    
    
    

def main_sql():

    with sqlite3.connect("todos_db.db") as con:
        cur = con.cursor()

        url = "https://jsonplaceholder.typicode.com/todos"
        response = requests.get(url)
        todos = response.json()
        print(todos[0])
       
        sql_inser = f"""INSERT INTO 
todos_tbl(user_id,title,completed) 
VALUES(
    {todos[0]['userId']},
    '{todos[0]['title']}',
    {todos[0]['completed']}
    )
"""
    cur.execute(sql_inser)
    con.commit()
    
    
    

if __name__=='__main__':
    main()
