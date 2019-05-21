#This Python program was written by Radha Mahalingam (5-12-19)
import sys
from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars

sys.setrecursionlimit(2000)
app = Flask(__name__)

client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_facts

@app.route('/scrape')
def scrape():
   # db.collection.remove()
    mars = scrape_mars.scrape()
    print("\n\n\n")

    db.mars_facts.insert_one(mars)
    return "Just finished the Mars scrapped data"

@app.route("/")
def home():
    mars = list(db.mars_facts.find())
    print(mars)
    return render_template("index.html", mars = mars)


if __name__ == "__main__":
    app.run(debug=True)


