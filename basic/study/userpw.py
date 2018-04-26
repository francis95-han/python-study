#!/usr/bin/env python3
# -*- coding: utf-8 -*-
db = {}


def newuser():
    prompt = 'login desired:'
    while True:
        name = input(prompt)
        if db.has_key(name):
            prompt = 'name taken,try another: '
            continue
        else:
            break
    pwd = input('passwd:')
    db[name] = pwd


def olduser():
    name = input('login:')
    pwd = input('passwd:')
    passwd = db.get(name)
    if passwd == pwd:
        print('welcomer bcak', name)
    else:
        print('login incorrennt')


def showmenu():
    prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit

Enter choice: """
    done = False
    while not done:

        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print('\nYou picked :[%s]' % choice)
            if choice not in 'neq':
                print('invalued option ,try again')
            else:
                chosen = True
        if (choice == 'q'): done = True
        if (choice == 'n'): newuser()
        if (choice == 'e'): olduser()


if __name__ == '__main__':
    showmenu()
