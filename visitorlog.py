from flask import Blueprint,request
from sqlalchemy.sql import text
from db import db
import datetime

visitor_blueprint=Blueprint('visitor_blueprint',__name__)
@visitor_blueprint.route('/log-visitors',methods=['POST'])
def addVisitorData():
    gender=request.form['gender']
    ageGroup=request.form['age-group']
    currentDate=datetime.datetime.today().strftime("%Y-%m-%d")
    currentTime = datetime.datetime.now().strftime("%H:%M:%S")
    sql = text('INSERT INTO visitor_log(gender,age_group,date,time) values('+str(gender)+','+str(ageGroup)+',"'+currentDate+'","'+currentTime+'")')
    
    db.engine.execute(sql)

    return "Data logged Successfully"