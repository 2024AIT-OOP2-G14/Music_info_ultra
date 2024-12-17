from flask import Blueprint, render_template,json,request, redirect, url_for,jsonify
from models import User
from models import register_chart
import datetime

register_bp = Blueprint('index', __name__, url_prefix='/')

@register_bp.route('/get_data', methods=['GET'])
def register():
    print('a')
    users = User.select()
    userDate = [user.date for user in users]    #登録日のdatetime.dateリスト

    userDate_list = []  #登録日のintリスト

    for user in userDate:
        userDate_list.append( str(user)[:7].split('-') )
    
    print(userDate_list)
    
    thisYear = str(datetime.datetime.now().year)

    regi_Transition = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for d in userDate_list:
        if d[0] == thisYear:
            for i in range(0,12):
                if int(d[1])-1 == i:
                    regi_Transition[i] += 1

    return jsonify(regi_Transition)