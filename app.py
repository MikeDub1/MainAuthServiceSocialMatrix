import firebase_admin
import os
import json
import base64
import hashlib
from google.auth import jwt
from firebase_admin import credentials, auth
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig


app = Flask(__name__)
postgres_db = SQLAlchemy(app)
app.config.from_object(DevelopmentConfig)

from models import database
from loginRegistration import bp
app.register_blueprint(database)
app.register_blueprint(bp)
migrate = Migrate(app, postgres_db, os.path.join(os.getcwd(), "migrations"))


cred = credentials.Certificate("F:\GitHubStuffDesktop\MainAuthServiceSocialMatrix\socialmatrix-52e60-firebase-adminsdk-dkjm8-ce7221ea64.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://socialmatrix-52e60-default-rtdb.firebaseio.com/'
})



#Sender must send a unique identifier(MAC Adress) with the token over HTTPS
#How to get MAC Address: https://docs.unrealengine.com/4.26/en-US/API/Runtime/Core/GenericPlatform/FGenericPlatformMisc/GetMacAddress/