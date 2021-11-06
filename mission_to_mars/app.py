
from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.mars_db
collection = db.mars_info

@app.route("/")
def home():
    destination_data = collection.find_one()
    return render_template("index.html", mars_data=destination_data)


@app.route("/scrape")
def scrape():
    mars_info = scrape_mars.scrape()
    collection.drop()
    collection.insert_one(mars_info)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)