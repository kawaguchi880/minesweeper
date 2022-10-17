from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,make_response,flash
import json

app = Flask(__name__)
app.config["SECRET_KEY"] = "jabf6OsdgoIaoiwfh"


@app.route('/')

def index():
   user_info = request.cookies.get('user_info')
   if user_info is not None:
        user_info = json.loads(user_info)
   return render_template('index.html',user_info=user_info)

@app.route('/sudoku')
def sudoku():
   user_info = request.cookies.get('user_info')
   if user_info is not None:
        user_info = json.loads(user_info)
   return render_template('sudoku.html',user_info=user_info)


@app.route('/minesweeper_easy')
def minesweeper_easy():
   user_info = request.cookies.get('user_info')
   if user_info is not None:
        user_info = json.loads(user_info)
   return render_template('minesweeper_easy.html',user_info=user_info)

@app.route('/minesweeper_nomal')
def minesweeper_nomal():
   user_info = request.cookies.get('user_info')
   if user_info is not None:
        user_info = json.loads(user_info)
   return render_template('minesweeper_nomal.html',user_info=user_info)

@app.route('/minesweeper_hard')
def minesweeper_hard():
   user_info = request.cookies.get('user_info')
   if user_info is not None:
        user_info = json.loads(user_info)
   return render_template('minesweeper_hard.html',user_info=user_info)

@app.route('/mypage')
def mypage():
   user_info = request.cookies.get('user_info')
   if user_info is not None:
        user_info = json.loads(user_info)
   return render_template('mypage.html',user_info=user_info)

@app.route('/setcookie',methods = ['POST','GET'])
def setcookie():
   if request.method =='POST':
      user_name = request.form['nm']
      buttle_count = "0"
      win_count ="0"
      mine_easy_count="0"
      mine_nomal_count ="0"
      mine_hard_count="0"
      mine_easy_win_count="0"
      mine_nomal_win_count="0"
      mine_hard_win_count = "0"
      user_icon = "images/{}.png".format(request.form['icon'])
      user_info = {'user_name':user_name,'user_icon':user_icon,'win_count':win_count,'buttle_count':buttle_count,'mine_hard_count':mine_hard_count,'mine_hard_win_count':mine_hard_win_count,'mine_nomal_count':mine_nomal_count,'mine_nomal_win_count':mine_nomal_win_count,'mine_easy_win_count':mine_easy_win_count,'mine_easy_count':mine_easy_count}
      flash('登録しました。  ユーザー名：{}  アイコン：{}'.format(user_name,request.form['icon']), 'register')

   res = make_response(render_template('mypage.html'))
   res.set_cookie('user_info',value=json.dumps(user_info))
   
   return res

@app.route('/delete_cookie')
def delete_cookie():
    res = make_response(render_template('mypage.html'))
    res.delete_cookie('user_info')
    return res

@app.route('/game_result',methods = ['POST','GET'])
def buttle_rerult():
   user_info = request.cookies.get('user_info')
   if  user_info is None:
      return render_template('index.html')
   elif request.method =='POST':
      user_info = json.loads(user_info)
      result = request.form['game_result']
      game_level = request.form['game_level']
      print(user_info)
      # 総試合数の更新
      buttle_count = int(user_info['buttle_count']) 
      buttle_count += 1
      user_info['buttle_count'] = buttle_count
      # # 難易度，ゲーム別の試合数の更新
      if game_level == 'hard':
         mine_hard_count = int(user_info['mine_hard_count'])
         mine_hard_count +=1
         user_info['mine_hard_count'] = mine_hard_count
      if game_level == 'nomal':
         mine_nomal_count = int(user_info['mine_nomal_count'])
         mine_nomal_count +=1
         user_info['mine_nomal_count'] = mine_nomal_count
      if game_level == 'easy':
         mine_easy_count = int(user_info['mine_easy_count'])
         mine_easy_count +=1
         user_info['mine_easy_count'] = mine_easy_count

      if result == 'win':
         win_count = int(user_info['win_count'])
         win_count +=1
         user_info['win_count'] = win_count
         if game_level == 'hard':
            mine_hard_win_count = int(user_info['mine_hard_win_count'])
            mine_hard_win_count +=1
            user_info['mine_hard_win_count'] = mine_hard_win_count
         if game_level == 'nomal':
            mine_nomal_win_count = int(user_info['mine_nomal_win_count'])
            mine_nomal_win_count +=1
            user_info['mine_nomal_win_count'] = mine_nomal_win_count
         if game_level == 'easy':
            mine_easy_win_count = int(user_info['mine_easy_win_count'])
            mine_easy_win_count +=1
            user_info['mine_easy_win_count'] = mine_easy_win_count

   print(user_info)
   res = make_response(render_template('index.html',user_info=user_info))
   res.set_cookie('user_info',value=json.dumps(user_info))
   return res

@app.route('/statistics')
def statistics():
   user_info = request.cookies.get('user_info')
   user_info = json.loads(user_info)
   print(user_info)
   buttle_count = int(user_info['buttle_count'])
   print(user_info)
   print(buttle_count)
   if buttle_count == 0:
      flash("戦績はまだありません!!",'errtext')
      return  redirect('/')
   else:
      return render_template('statistics.html',user_info=user_info)
   
if __name__ == '__main__':
   app.run()
