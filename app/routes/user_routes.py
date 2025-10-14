from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile/<username>')
def profile(username):
    return f"<h1>O perfil de {username}</h1>"
