from random import randint
from flask import Flask, session, redirect, url_for
from db_scripts import get_question_after


quiz = 0
last_question = 0

def index():
   global quiz, last_question
   quiz = 1
   last_question = 0
   return '<a href="/question">Тест на дебелизм</a>'


def question():
   global last_question
   result = get_question_after(last_question, quiz)
   if result is None or len(result) == 0:   
           return redirect(url_for('result'))
   else:
       last_question = result[0]
       return '<h1>' + str(quiz) + '<br>' + str(result) + '</h1>'

def result():
   return "<h1>Викторина закончилась</h1>"


app = Flask(__name__)  
app.add_url_rule('/', 'index', index)   # создаёт правило для URL '/'
app.add_url_rule('/question', 'question', question) # создаёт правило для URL '/test'
app.add_url_rule('/result', 'result', result) # создаёт правило для URL '/test'

if __name__ == '__main__':
   # Запускаем веб-сервер:
   app.run()
