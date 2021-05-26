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


def get_val_db():
    print("GET USAGE: [key]")
    while True:
        key = input("KEY: ")
        if len(key) < 1:
            print("Too few arguments")
        else:
            break

    try:
        val = DB.get_value(key)
        print("VALUE: " + val)
    except KeyNotFoundError:
        print("(nil)")


def set_dt_db():
    print("SET USAGE: [key] [value]")
    while True:
        key = input("KEY: ")
        if len(key) < 1:
            print("Too few arguments")
        else:
            break

    while True:
        value = input("VALUE: ")
        if len(value) < 1:
            print("Too few arguments")
        else:
            break

    DB.insert_data(key, value)
    print("OK\n")


def mget_val_db():
    print("MGET USAGE: [key_1] [key_2] [key_3] [key_4] ...")
    while True:
        keys = input().split()
        if len(keys) < 1:
            print("Too few arguments")
        else:
            break

    for i, key in enumerate(keys):
        try:
            val = DB.get_value(key)
            print(f"{i+1}) VALUE: {val}")
        except KeyNotFoundError:
            print(f"{i+1}) (nil)")
    print()

def flush():
    global DB
    del DB
    DB = AVLTree()
    print("Flushed the database\n")


def dlt_dt_db():
    print("DELETE USAGE: [key]")
    while True:
        key = input("KEY: ")
        if len(key) < 1:
            print("Too few arguments")
        else:
            break
    DB.delete_data(key)


def mset_dt_db():
    print("MSET USAGE: [key_1] [value_1] [key_2] [value_2] ...")
    while True:
        args = input().split()
        if len(args) % 2 or len(args) == 0:
            print("Fewer arguments specified")
        else:
            break

    for i in range(0, len(args), 2):
        DB.insert_data(args[i], args[i+1])
    print("OK\n")


print("type `help` or `h` to get help message(without backticks)")
while True:
    try:
        cmd = input(">>> ").lower()
    except (KeyboardInterrupt, EOFError):
        print()
        break

    if cmd == "h" or cmd == "help":
        display_commands()
    elif cmd == "1" or cmd == "get":
        get_val_db()
    elif cmd == "2" or cmd == "set":
        set_dt_db()
    elif cmd == "3" or cmd == "mget":
        mget_val_db()
    elif cmd == "4" or cmd == "mset":
        mset_dt_db()
    elif cmd == "5" or cmd == "delete":
        dlt_dt_db()
    elif cmd == "6" or cmd == "flush":
        flush()
    else:
        print("Unrecognized command.\n")
