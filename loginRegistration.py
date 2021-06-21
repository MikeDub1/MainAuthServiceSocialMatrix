import json
import base64
import hashlib
from google.auth import jwt
from firebase_admin import auth, db
from flask import Blueprint, request, Response
from models import User
from firebase_admin.exceptions import FirebaseError

bp = Blueprint("login_registration", __name__)


@bp.route("/login")
def login():
    #Verify user creds here!...
    email = request.args['username']
    pswd = requests.args['password']

    try:
        user = auth.get_user_by_email(email)
    except FirebaseError:
        return Response(status=404) #User not found!
    

    users_ref = db.reference("/Users")
    snapshot = users_ref.get()
    custom_token = snapshot[str(user.uid)][token]

    #Use db here to manipulate the firebase database...
    
    
    return custom_token

@bp.route("/signup")
def signup():
    email = request.args['username']
    pswd = request.args['password']

    user = auth.create_user(email=email, email_verified=False, password=pswd, disabled=False)

    algo = hashlib.sha256()
    fullacc = email + " " + pswd
    algo.update(fullacc.encode('utf-8'))
    key = algo.digest()
    custom_token = auth.create_custom_token(str(key))

    users_ref = db.reference("/Users")
    users_ref.set({
        user.uid : {
            'email': email,
            'password': pswd,
            'token': custom_token.decode("utf-8")
        }
    })
    return custom_token