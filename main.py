from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    with open("res.txt","r") as f:
        ad = f.read()
        return ad

@app.route("/change/<ip>")
def change(ip):
    with open("res.txt","w") as f:
        f.write(ip)
    return "ok"

@app.route("/logs", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.get_json()
        name = data.get("name")


if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)


