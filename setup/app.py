from flask import Flask, Response
import requests
import json

app = Flask(__name__)

AUTH = ("user", "password")
API_URL = "http://192.168.178.95:8080/api/GetCurrentData"

@app.route("/metrics")
def metrics():
    try:
        r = requests.get(API_URL, auth=AUTH, timeout=5)
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        return Response(f"# Error fetching API: {e}\n", mimetype="text/plain")

    lines = []
    for k, v in data.items():
        if isinstance(v, (int, float)):
            metric_name = k.lower()
            lines.append(f"{metric_name} {v}")

    return Response("\n".join(lines)+"\n", mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
