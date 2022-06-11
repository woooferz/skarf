from flask import Flask, render_template, redirect, jsonify, send_from_directory
import yaml
import json

skarf_version = "v0.1.3"

print(f"Skarf {skarf_version}")

print("Loading Config...")
try:
    with open("config/config.yml", "r") as f:
        config = yaml.load(f.read(), Loader=yaml.Loader)
    print("Loaded YAML")
except FileNotFoundError:
    try:
        with open("config/config.json", "r") as f:
            config = json.loads(f.read())
        print("Loaded JSON")
    except FileNotFoundError:
        print("Could not find config")
        config = None

if config:
    print("Loaded!")
else:
    print("Error while loading config")
# print(config)

app = Flask(__name__)


@app.route("/")
def home():
    if config:
        return render_template(f"versions/{str(config['version'])}.html", config=config['settings'])
    else:
        return render_template("no_config.html", the_version=skarf_version)


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static/', path)


@app.route('/res/<path:path>')
def send_res(path):
    return send_from_directory('res', path)


if __name__ == "__main__":
    app.run(port=80, host="0.0.0.0")
