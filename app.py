# Importing Dependancies 
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

#################################################
# Database Setup
#################################################

rds_connection_string = f"root:121212nJ@127.0.0.1/leads_db"
engine = create_engine(f'mysql+pymysql://{rds_connection_string}')

leads_df = pd.read_sql('SELECT * FROM leadscsv', con=engine)
print(leads_df.head())
# app.config["SQLALCHEMY_DATABASE_URI"] = ""
# db = SQLAlchemy(app)

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(db.engine, reflect=True)

# # Save references to each table
# TENNISDATA = Base.classes.TENNISDATA

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/data")
def get_data():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(leads_df).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])    




if __name__ == "__main__":
    app.run()    