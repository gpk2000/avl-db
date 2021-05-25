import os
from typing import Type
from avltree.AVLTree import AVLTree, KeyNotFoundError

DB = AVLTree()


def display_commands():
    msg = """\nSelect one of the following options
1) get      - gets the value of key from the database
2) set      - sets the (key, value) pair in database
3) mget     - gets the values of keys from the database
4) mset     - sets the (key, value) pairs in database
5) delete   - deletes the key and its value from the database
6) flush    - deletes the whole database and start from scratch\n\n"""
    print(msg)


while True:
    display_commands()
    try:
        cmd = input(">>> ")
    except (KeyboardInterrupt, EOFError):
        print()
        break
    
