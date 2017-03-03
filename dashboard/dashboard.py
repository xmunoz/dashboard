# -*- coding: utf-8 -*-
import os
import os.path
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import inspect
from ictf import iCTF

app = Flask(__name__)
app.config.from_pyfile(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(
            inspect.currentframe())))), "login.cfg"))
app.config.update(dict(
    DEBUG=True,
))

i = iCTF()
CTF = i.login(app.config["LOGIN_USERNAME"], app.config["LOGIN_PW"])
print("yay! successful login!")

@app.route('/')
def show_team_status():
    status = CTF.get_team_status()
    return render_template('home.html', status=status)

@app.route('/services')
def show_services():
    status = CTF.get_service_list()
    return render_template('service_list.html', status=status)

@app.route('/teams')
def show_teams_list():
    tlist = CTF.get_teams_list()
    return render_template('login.html', teams=tlist)

@app.route('/teams/<tid>')
def show_team(tid):
    tlist = CTF.get_teams_list()
    return render_template('login.html', teams=tlist)
