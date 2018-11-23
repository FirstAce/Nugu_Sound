from hischool import app
from hischool.database import *
from hischool.api import *
from flask import (
    render_template,
    redirect,
    request,
    abort,
    url_for,
    session
)

@app.route('/health')
def healthCheck():
    return 'OK'

@app.route('/', methods=['GET', 'POST'])
def home():
    req = request.json
    print(request.json)
    action = req['action']['actionName']
    if action == 'getMeal':
        return getMeal(req)
    elif action == 'getQuote':
        return getQuote()
    elif action == 'getSchedule':
        return getSchedule(req)
    return ''
