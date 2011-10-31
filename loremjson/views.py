# -*- coding: utf-8 -*-
from loremjson import app, utils
from flask import render_template, request, url_for, abort, Response


@app.route('/static/*')
def static_files():
    """Handles static files requests
    """
    endswith = request.path.endswith
    if endswith('main.css'):
        return url_for('static', filename='css/main.css')
    return ''
    

@app.route('/')
def index():
    """Handles index requests
    """
    response = {
        "title" : u"Welcome",
        "items" : ['/json/test%d.json' % num for num in range(1, 5)]
    }
    return render_template('index.html', **response)
    
    
@app.route('/json/<name>.json')
def raw_json(name=None):
    try:
        json_contents = utils.read_json_file(name)
    except IOError:
        abort(404)
    return Response(json_contents, mimetype='application/json')