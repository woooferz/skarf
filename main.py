from flask import Flask, render_template, redirect, jsonify, send_from_directory
import yaml

print("Loading Config...")
with open("config/config.yml", "r") as f:
    config = yaml.load(f.read(), Loader=yaml.Loader)
print("Loaded!")
# print(config)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(f"versions/{str(config['version'])}.html", config=config['settings'])


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static/', path)


@app.route('/res/<path:path>')
def send_res(path):
    return send_from_directory('res', path)


if __name__ == "__main__":
    app.run(port=80, host="0.0.0.0")
