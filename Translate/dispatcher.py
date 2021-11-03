# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 18:29:22 2021

@author: qzia
"""

import flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
# from werkzeug.wsgi import DispatcherMiddleware
#from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.exceptions import NotFound
from  flask_cors import CORS, cross_origin
from Translate import app as app1
import sys

#from ClaimPredictionModal_Qamar import app as app2
context = ('cert.pem', 'pkey.pem')

app = flask.Flask(__name__)
CORS(app)

app.wsgi_app = DispatcherMiddleware(NotFound(), {
    '/Translate': app1
    


})

if __name__ == "__main__":
    app.run(host='localhost',port=5000, debug=True)
    #app.run(ssl_context='adhoc')
    
#,ssl_context=context