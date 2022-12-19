from flask import Flask
from flask_cors import CORS

import country_codes

app = Flask(__name__)
CORS(app)

@app.route("/europe")
def europe():
    europe_country_codes = country_codes.fetch_europe_country_codes()
    
    return europe_country_codes