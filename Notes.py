# Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, редактированием и удалением заметок.
# Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки.
# Сохранение заметок необходимо сделать в формате json или csv формат (разделение полей рекомендуется делать через точку с запятой). 
# Реализацию пользовательского интерфейса студент может делать как ему удобнее, можно делать как параметры запуска программы (команда, данные), 
# можно делать как запрос команды с консоли и последующим вводом данных, как-то ещё, на усмотрение студента.
# должно уметь сохранять данные в файл, уметь читать данные из файла, делать выборку по дате, выводить на экран выбранную запись, 
# выводить на экран весь список записок, добавлять записку, редактировать ее и удалять.


import argparse
import json
import os

from datetime import datetime
from datetime import date


def add(notes, title, body, date):
    if len(notes) == 0:
        identifier = 1
    else:
        identifier = notes[-1]['identifier'] + 1

    notes.append({'identifier':identifier, 'title': title, 'body': body, 'date': date})


def read_notes(filename):
    with open(filename, 'r') as file:
        return json.load(file)
    

def write_notes(filename, notes):
    with open(filename, 'w') as file:
        json.dump(notes, file, indent = 3)

def delete(notes, identifier):
    for note in notes:
        if note['identifier'] == identifier:
            notes.remove(note)

def find(notes, identifier):
    for note in notes:
        if note['identifier'] == identifier:
            print(note)


def find_date(notes, date):
    for note in notes:
        if datetime.fromisoformat(note['date']).date() == date:
            print(note)


def find_all(notes):
    for note in notes:
        print(note)
    
    
def update(notes, identifier, title, body, date):
    for note in notes:
        if note['identifier'] == identifier:
            note['title'] = title
            note['body'] = body
            note['date'] = date



parser = argparse.ArgumentParser(description= "хранилище записок")
subprocess = parser.add_subparsers(dest='command')
cmd_add = subprocess.add_parser('add')
cmd_add.add_argument('title',  type=str)
cmd_add.add_argument('body',  type=str)

cmd_del = subprocess.add_parser('delete')
cmd_del.add_argument('id',  type=int)

cmd_find = subprocess.add_parser('find')
cmd_find.add_argument('--id', type=int)
cmd_find.add_argument('--date', type=date.fromisoformat)
