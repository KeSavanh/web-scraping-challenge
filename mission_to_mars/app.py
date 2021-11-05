
from flask import Flask, render_template, redirect
import pymongo
import scrape_mars


conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)


db = client.mars_db
collection = db.mars_info


app = Flask(__name__)

@app.route("/")
def home():
    data = collection.find_one()
    return render_template("index.html", data=data)





if __name__ == "__main__":
    app.run(debug=True)