from flask import request
from requests import get

@app.route("/get_ip", methods=["GET"])
def get_ip():
	ip = get('https://api.ipify.org').json
    return (ip), 200