# Dependancies
import os
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy



from sqlalchemy.sql import func


app = Flask(__name__)

# Database Setup
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/leads.sqlite"
db = SQLAlchemy(app)

# Reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Creating an easier reference
Leads_table = Base.classes.leads_table

# Home route 
@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")
    app.add_url_rule('/', 'index', index)

@app.route("/Charts")
def index1():
    """Return the homepage."""
    return render_template("Chart.html") 
    app.add_url_rule('/', 'index1', index1)     

@app.route("/Map")
def index2():
    """Return the homepage."""
    return render_template("Map.html") 
    app.add_url_rule('/', 'index2', index2)  

# Route for testing the data 
@app.route("/test")
def test_func():
    stmt = db.session.query(Leads_table).statement
    df = pd.read_sql_query(stmt, db.session.bind)
    return jsonify(list(df))


# Data route
@app.route("/data")
def get_data():

    # All the columns for selection
    sel = [
        Leads_table.ConsumerID,
        Leads_table.Zip,
        Leads_table.Audience_Count,
        Leads_table.City,
        Leads_table.State,
        Leads_table.Gender,
        Leads_table.Age,
        Leads_table.MaritalStatus,
        Leads_table.EthnicGroup,
        Leads_table.CreditScore,
        Leads_table.Kids,
        Leads_table.Email_Address
    ]

    # Saving all the data from quering above columns
    # results = db.session.query(*sel).\
    #     limit(500).all()

    # Query all the records
    results = db.session.query(*sel).all()         

    # Creating Pandas dataframe
    df = pd.DataFrame(results, columns=["ConsumerID", "Zip", "Audience_Count", "City", "State", "Gender", "Age", "MaritalStatus", "EthnicGroup", "CreditScore", "Kids", "Email_Address"])

    # Return results in JSON format for the interwebz
    return jsonify(df.to_dict(orient="records"))

@app.route("/data/nj")
def get_data_by_state():

    # All the columns for selection
    sel = [
        Leads_table.ConsumerID,
        Leads_table.Zip,
        Leads_table.Audience_Count,
        Leads_table.City,
        Leads_table.State,
        Leads_table.Gender,
        Leads_table.Age,
        Leads_table.MaritalStatus,
        Leads_table.EthnicGroup,
        Leads_table.CreditScore,
        Leads_table.Kids,
        Leads_table.Email_Address
    ]

    results_by_state = db.session.query(*sel).\
        filter(Leads_table.State == "NJ").\
        all()           

    # Creating Pandas dataframe
    df_by_state = pd.DataFrame(results_by_state, columns=["ConsumerID", "Zip", "Audience_Count", "City", "State", "Gender", "Age", "MaritalStatus", "EthnicGroup", "CreditScore", "Kids", "Email_Address"])

    # Return results in JSON format for the interwebz
    return jsonify(df_by_state.to_dict(orient="records"))

@app.route("/Charts/AgeBin")
def AgeBin_data():
    """Return Age Bin and Audience Count"""

    # Query for Audience Count by Age Bin
    sel = [Leads_table.AGEBIN,func.count(Leads_table.ConsumerID)]
    results = db.session.query(*sel).\
        group_by(Leads_table.AGEBIN).all()
    df = pd.DataFrame(results, columns=['AgeBin', 'AudienceCount'])
    return jsonify(df.to_dict(orient="records"))

@app.route("/Charts/Gender")
def Gender_data():
    """Return Gender and Audience Count"""

    # Query for Audience Count by Age Bin
    sel = [Leads_table.Gender,func.count(Leads_table.ConsumerID)]
    results = db.session.query(*sel).\
        group_by(Leads_table.Gender).all()
    df1 = pd.DataFrame(results, columns=['Gender', 'AudienceCount'])
    return jsonify(df1.to_dict(orient="records"))

@app.route("/Charts/CreditScore")
def CreditScore_data():
    """Return Credit Score and Audience Count"""
   # Query for Audience Count by Credit Score
    sel = [Leads_table.CreditScore,func.count(Leads_table.ConsumerID)]
    results = db.session.query(*sel).\
        group_by(Leads_table.CreditScore).all()
    df2 = pd.DataFrame(results, columns=['CreditScore', 'AudienceCount'])
    # Format the data for Plotly
    data = {
        "x": df2["CreditScore"].values.tolist(),
        "y": df2["AudienceCount"].values.tolist(),
        "type": "bar"
    }
    return jsonify(data)
           

@app.route("/Charts/Household_Income")
def Household_Income_data():
    """Return Household_Income and Audience Count"""
    # Query for Audience Count by Credit Score
    sel = [Leads_table.Household_Income,func.count(Leads_table.ConsumerID)]
    results = db.session.query(*sel).\
        group_by(Leads_table.Household_Income).all()
    df3 = pd.DataFrame(results, columns=['Household_Income', 'AudienceCount'])
    # Format the data for Plotly
    data = {
        "x": df3["Household_Income"].values.tolist(),
        "y": df3["AudienceCount"].values.tolist(),
        "type": "bar"
    }
    return jsonify(data)




if __name__ == "__main__":
    app.run()    