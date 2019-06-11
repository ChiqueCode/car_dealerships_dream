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
# @app.route("/test")
# def test_func():
#     stmt = db.session.query(Leads_table).statement
#     df = pd.read_sql_query(stmt, db.session.bind)
#     return jsonify(list(df["Zip"]))


# Data route
@app.route("/data")
def get_data():

    # All the columns for selection
    sel = [
        Leads_table.Zip,
        Leads_table.City,
        Leads_table.State,
        Leads_table.Gender,
        Leads_table.Age,
        Leads_table.MaritalStatus,
        Leads_table.CreditScore,
        Leads_table.Kids,
        Leads_table.Email_Address
    ]

    # Saving all the data from quering above columns
    results = db.session.query(*sel).all()

    # Creating Pandas dataframe
    df = pd.DataFrame(results, columns=["Zip", "City", "State", "Gender", "Age", "MaritalStatus", "CreditScore", "Kids", "Email_Address"])

    # Return results in JSON format for the interwebz
    return jsonify(df.to_dict(orient="records"))


if __name__ == "__main__":
    app.run()    