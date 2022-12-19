import json

EUROPE_COUNTRY_CODES_FILE = "database/" + "europe.json"

def read_europe():
    f = open(EUROPE_COUNTRY_CODES_FILE)

    data = json.load(f)

    f.close()

    return data

def fetch_europe_country_codes():
    europe = read_europe()
    return europe
