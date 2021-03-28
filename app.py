from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo
import scrape_mars

#create an instance of our Flask App
app = Flask(__name__)

# ------------------------------------------#

#Create connection variable
conn = 'mongodb://localhost:27017'

#Pass connection to the pymongo instance
client = pymongo.MongoClient(conn)

#Connect to a database. Will create one if not already available.
db = client.mars
collection = db.mars_data

#Drops collection if available to remove duplicates
#db.mars.drop()

# HOW DO I GET THIS TO WORK
#insert dictionary from scrape_mars.py to the collection 
#db.mars.insert_one(scrape_mars_dict)

# ------------------------------------------#

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/phone_app")


@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scraper():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)


scraper()


