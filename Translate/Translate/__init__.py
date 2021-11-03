# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 18:24:25 2021

@author: qzia
"""

from flask import Flask, render_template, url_for, jsonify, request
from translate import Translator
from flask_cors import CORS

app = Flask(__name__)
cors=CORS(app)
app.config['JSON_AS_ASCII'] = False

@app.route('/translate-text', methods=['POST'])
#@cross_origin()

def translate_text():
    from translate import Translator
    data = request.get_json()
    text_input = data['text']
    #translation_output = data['to']
    translator= Translator(from_lang="english",to_lang="arabic",email="eawan786@gmail.com")
    response = translator.translate(text_input)
    return jsonify(response)
