from flask import Flask,redirect,jsonify

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
    with open("res.txt","r") as f:
        ad = f.read()
        return redirect("https://"+ad)

@app.route("/change/<ip>/<passs>")
def change(ip,passs):
    if passs != "yessir":
        return redirect("/denied")
    with open("res.txt","w") as f:
        f.write(ip)
    return "ok",200

@app.route("/logs", methods=["GET", "POST"])
def logs():
    if request.method == "POST":
        data = request.get_json()
        name = data.get("name")


if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)


