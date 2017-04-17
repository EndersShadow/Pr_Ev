from flask import Flask, render_template, request, session, make_response
from src.common.database import Database

__author__= 'rtaylor'


app = Flask(__name__)

@app.before_first_request
def initialize_database():
    Database.initialize()
