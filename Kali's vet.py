import os
import getenv

login = 'admin.vet'
password = os.getenv('ADMIN_VET_PASSWORD')

l = input('login = ')
p = input('password = ')



if l == login:
    if p == password:
        l = input(login)
        p = input(password)

import colorama
colorama.init()

print(colorama.Fore.BLACK)
print(colorama.Back.LIGHTWHITE_EX)

class Cat:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print('eee')

kali = Cat('kali')
print(kali.name)
kali.make_sound()

class Dog:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print('levretka is coming soon!')

levretka = Dog('levretka')
print(levretka.name)
levretka.make_sound()

import sqlite3 as sl3

connection = sl3.connect("vet.sl3")

cursor = connection.cursor()

cursor.execute("""
    create table IF NOT EXISTS pets ('
        id integer primary key,
        name text,
        age integer
        
INSERT INTO students (id, name, age) VALUES
(1, 'Kali', "kalisto@gmail.com", 1,5)
(2, 'Cat', "cat@gmail.com", ?)
(2, 'Maru', "maruthecatinbox@gmail.com", 3)
    ');
""")

cursor.execute("""
    create table IF NOT EXISTS petfood ('
        name text,
        weight integer,
        taste integer,
        keycode text,
        cost integer

INSERT INTO students (name, weight, taste, keycode, cost) VALUES
(1, 'Carnilove', "500", 'salmon', 48168194, 495)
(2, 'Carnilove', "100", 'duck', 472857108, 195)
(3, 'Carnilove', "100", 'salmon', 3003818, 195)
(3, 'Carnilove', "150", 'salmon', 41179829, 95)
    ');
""")

print(cursor.execute)

connection.commit()

connection.close()