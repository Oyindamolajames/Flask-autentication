from flask import request, jsonify, make_response, render_template, session
import jwt
from datetime import datetime, timedelta
from app.config import app, db, token_required
from app.models import User



# db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html')


@app.route('/user', methods=["GET"])
@token_required
def user():
    users = User.query.all()
    user_names = [user.name for user in users]
    return jsonify({'users': user_names})


@app.route('/add_user', methods=["POST"])
@token_required
def add_user():
    try:
        # Get the 'name' parameter from the request
        data = request.args.get("name")

        # Check if 'name' is not provided or empty
        if not data:
            return jsonify({"message": "Name parameter is missing or empty"}), 400

        # Create a new user and add it to the database
        new_user = User(name=data)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User added successfully", "name": new_user.name}), 201
    except Exception as e:
        # Handle exceptions, you might want to log the error for debugging
        return jsonify({"message": "Error occurred while adding the user", "error": str(e)}), 500


@app.route("/login", methods=["POST"])
def login():
    if request.form['username'] and request.form['password'] == '123456':
        session['logged_in'] = True

        token = jwt.encode({
            'user': request.form['username'],
            'expiration': str(datetime.utcnow() + timedelta(seconds=6000000))
        },
            app.config['SECRET_KEY'])
        return jsonify({'token': token, 'info': {'token': jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])}})
    else:
        return make_response('Unable to verify', 403)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return "logout succesful"
