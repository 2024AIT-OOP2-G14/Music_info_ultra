from flask import Blueprint, render_template, request, redirect, url_for
from models import User
from models import register_chart

register_bp = Blueprint('index', __name__, url_prefix='/')

@register_bp.route('/')
def register():
    print('a')
    users = User.select()
    print(users)
    
    return render_template('index.html', items=users)