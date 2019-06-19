# Dealership Leads

Created by:
- [Kseniya Bogoslavskaya](https://chique.dev/)
- Monika Raj
- Sajani Menon
- Amit Raut

BACKGROUND

We are nationwide cable company with a extensive database of customer data. Our database is highly confidential and maintains all ethical norms. 
We the Business Intelligence team at CoolCable were approached for a 2020 project idea with a goal to increase revenue. 
What you will see is a POC that was put together to request funding.

About US
Data is knowledge. Using the data and insights we have about our data, we have created an interactive dashboard for Car dealers. 

This website will be a one stop shop for car dealers to find their next customer. A car dealer can browse through our website, enter their criteria requirements for an email, phone or mail campaigns and purchase the required dataset for a nominal fee. 

Source 

The database is based on real authentic data and contains information of only those customers who are willing to share their credentials and the same has been built over regular surveys conducted by the CoolCable marketing research team.    

Inspiration

![End Goal](https://github.com/sajanimenon/A-Car-Dealer-s-Dream/blob/master/static/images/image001.png)

Sources

Read data CSV with over 50000 records and demographics

WorkFlow

Extract Data
Take data from available CSV file and review the parameters 

Clean Data
Use a jupyter notebook to clean the data and read the data from CSV to a SQLite database
Define data types and change Zip to a "string" and rename columns as required
Save data as SQLite database
The database created by runnign the data engienering file is creates SQLite database leads.sqlite saved outside of the db folder. We need to move it to the db folder to make it run 

Visualization

Visualizations are done using Ploty, Leaflet, D3plus and Mapbox. To answer the following questions reading from SQLite database to answer the following questions:-

Demographic Insights

1. How many people are interested in purchasing the vehicle in your area? (Heat Map, gauge with number of leads)
2. Gender Composition, Age composition of the database

Financial Insights

3. Financial Stability analysis of the credit scores of the possible customers
4. Audience Count by Household incomes

Building Form for purchase:

How to Purchase

Fill out the Form and find your next customers instantly 

Fields on the form:
1. Name of the Dealership
2. Address
5. Phone 

Hit Pay with PayPal => Thank you, you payment has been processed, take a look at your opportunities:

Table of the customers name, address, and so on

The Map with your dealership and the leads 

Tools Used: 
- [Foundation](https://foundation.zurb.com/sites/docs/)
