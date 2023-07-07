import sys
import sqlite3
from TodoDAO import TodoDAO
from Todo import Todo
import configparser
import argparse
from tkinter import *
from tkinter import ttk

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

    ws = Tk()
    ws.title('TodoList')
    ws.geometry('800x600')
    ws['bg']='#fb0'

    tv = ttk.Treeview(ws,show="headings")
    tv['columns']=('Id', 'Title', 'Completed')
    tv.column('Id',  anchor=CENTER,stretch=NO)
    tv.column('Title', anchor=CENTER, width=80)
    tv.column('Completed', anchor=CENTER, width=80)

    tv.heading('Id', text='Id', anchor=CENTER)
    tv.heading('Title', text='Title', anchor=CENTER)
    tv.heading('Completed', text='Completed', anchor=CENTER)
    
    for todo in todos:
        tv.insert(parent='', index=todo.id, iid=todo.id, text='', values=(todo.id,todo.title,todo.completed))
    
    tv.pack(fill=BOTH,expand=True)


    ws.mainloop()

if __name__=='__main__':
    main()
