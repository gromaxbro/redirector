from flask import Flask,redirect,jsonify
import requests
import psycopg2
import os

# Render automatically loads environment variables
DATABASE_URL = os.environ.get('DATABASE_URL')


conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()


app = Flask(__name__)

@app.route("/bad_request")
def bad_request():
    return jsonify(error="Something went wrong"), 400

@app.route("/denied")
def not_found():
    return jsonify(error="Access Denied"), 403

@app.route("/server_error")
def server_error():
    return jsonify(error="Internal server error"), 500

@app.route("/")
def home():
    cur.execute("SELECT url FROM ngrok_url;")
    row = cur.fetchone()[0]
    check_ping = requests.get(row)
    if check_ping.status_code == 200:
        return redirect(row)
    else:
        reg = check_ping.headers
        cur.execute("SELECT updated_at FROM ngrok_url;")
        up = cur.fetchone()[0]
        return f"Server is offline or wrong url \n ping result:\n {reg} \n last_update={up}"


@app.route("/change/<ip>/<passs>")
def change(ip,passs):
    if passs != "yessir":
        return redirect("/denied")

    cur.execute(f"update ngrok_url SET url='https://{ip}' , updated_at=NOW() where id=1;")
    conn.commit()

    return "ok",200

@app.route("/logs", methods=["GET", "POST"])
def logs():
    if request.method == "POST":
        data = request.get_json()
        name = data.get("name")


if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)


