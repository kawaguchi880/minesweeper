from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')


@app.route('/minesweeper_easy')
def minesweeper_easy():
   return render_template('minesweeper_easy.html')

@app.route('/minesweeper_nomal')
def minesweeper_nomal():
   return render_template('minesweeper_nomal.html')

@app.route('/minesweeper_hard')
def minesweeper_hard():
   return render_template('minesweeper_hard.html')

@app.route('/mypage')
def mypage():
   return render_template('mypage.html')




if __name__ == '__main__':
   app.run()
