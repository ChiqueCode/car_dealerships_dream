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


if __name__ == "__main__":
    app.run()    