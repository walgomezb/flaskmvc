# -*- coding: utf-8 -*-
from flask import Flask, request, g
from flask import render_template
import sys

app = Flask(__name__)


sys.path.append("./controllers/")
from usrListCtrl import UserListCtrl

@app.route('/')
def main_page():
    """Searches the database for entries, then displays them."""
    #db = get_db()
    #cur = db.execute('select * from entries order by id desc')
    #entries = cur.fetchall()
    #return render_template('index.html', entries=entries)
    print("ya recibi peticion")
    myUsrListCtrl=UserListCtrl("miListaDevnet")
    return render_template('index.html', entries=myUsrListCtrl.userList.listOfUser)

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=8088)