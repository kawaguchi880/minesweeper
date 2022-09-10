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



if __name__ == '__main__':
   app.run()
