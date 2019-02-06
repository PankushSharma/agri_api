# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 16:16:17 2019

@author: PANKUSH
"""
from django.db import IntegrityError
from flask import Flask,jsonify,request
import sqlalchemy as db
import pandas as pd
#from django.shortcuts import render_to_response
#import MySQLdb
#from MySQLdb import _mysql_exceptions
#from _mysql_exceptions import OperationalError
agri=Flask(__name__)
engine = db.create_engine('mysql://sql12276751:KTY5JEgbUw@sql12.freemysqlhosting.net:3306/sql12276751')
connection = engine.connect()
metadata = db.MetaData()
customer = db.Table('customer', metadata, autoload=True, autoload_with=engine)
#user={"username":"pankushA","password":"23"}
#result=connection.execute(customer).fetchall()
#customers = pd.DataFrame(result)
# insert command
@agri.route("/create",methods=["Post"])
def posting():
    user=request.get_json()
    un=user["username"]
    pw=user["password"]
    try:
        ins_record = customer.insert().values(username=un,password=pw)
        ResultProxy = connection.execute(ins_record)
        return jsonify({"username created":user["username"]})
    except:
         return jsonify({"username already exist re-enter another username":user["username"]})
agri.run()     
          

# update command
#@agri.route("/update_username",methods=["Put"])
#def update():
 #   user=request.get_json()
  #  un=user["username"]
   # pw=user["password"]
    #try:
        
     #   update = customer.update().where(customer.c.password == 'Khanna').values(lastname = 'Kapoor')
#get
#df = pd.DataFrame(query.fetchall())
#df.columns = query.keys()
#print(df.head())
