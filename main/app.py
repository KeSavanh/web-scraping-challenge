from typing import Collection
from flask import Flask, render_template
import pymongo

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)


db = client.mars_db
Collection = db.info


app = Flask(__name__)


