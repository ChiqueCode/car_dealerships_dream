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

# Save references to each table
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
    return jsonify(list(df["Zip"]))


if __name__ == "__main__":
    app.run()    