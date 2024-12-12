from flask import Blueprint, render_template, request, redirect, url_for
from models import User

# Blueprintの作成
user_bp = Blueprint('user', __name__, url_prefix='/users')

# 
#   会員データ一覧
#



@user_bp.route('/')
def list():
    users = User.select()
    return render_template('user_list.html', title='会員一覧', items=users)


@user_bp.route('/add', methods=['GET', 'POST'])
def add():
    
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        date = request.form['date']
        User.create(name=name, number=number, date=date)
        return redirect(url_for('user.list'))
    
    return render_template('user_add.html')


@user_bp.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit(user_id):
    user = User.get_or_none(User.id == user_id)
    if not user:
        return redirect(url_for('user.list'))

    if request.method == 'POST':
        user.name = request.form['name']
        user.number = request.form['number']
        user.date = request.form['date']
        user.save()
        return redirect(url_for('user.list'))

    return render_template('user_edit.html', user=user)