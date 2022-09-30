from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,make_response,flash,session
import json
from datetime import timedelta

app = Flask(__name__)
app.config["SECRET_KEY"] = "jabf6OsdgoIaoiwfh"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def index():
   user_info = request.cookies.get('user_info')
   if user_info is not None:
        user_info = json.loads(user_info)
   return render_template('index.html',user_info=user_info)



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

@app.route('/setcookie',methods = ['POST','GET'])
def setcookie():
   
   if request.method =='POST':
      session.permanent = True
      user_name = request.form['nm']
      user_icon = "images/{}.png".format(request.form['icon'])
      user_info = {'user_name':user_name,'user_icon':user_icon}
      flash('登録しました。  ユーザー名：{}  アイコン：{}'.format(user_name,request.form['icon']), 'register')

   res = make_response(render_template('mypage.html'))
   res.set_cookie('user_info',value=json.dumps(user_info))
   
   return res

@app.route('/delete_cookie')
def delete_cookie():
    res = make_response(render_template('mypage.html'))
    res.delete_cookie('user_info')
    return res


if __name__ == '__main__':
   app.run()
