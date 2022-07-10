import json

import yaml
from flask import Flask, render_template, send_from_directory

skarf_version = "v0.2.2"

print(f"Skarf {skarf_version}")

print("Loading Config...")


def load_config():
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
    return config


config = load_config()

if config:
    print("Loaded!")
    try:
        if config["debug"]:
            print("SKARF IS IN DEBUG MODE! THIS IS NOT PRODUCTION READY!")
    except KeyError:
        pass
else:
    print("Error while loading config")
# print(config)

app = Flask(__name__)


@app.route("/")
def home():
    global config
    if config:
        try:
            if config["debug"]:
                print("Reloading Config! (THIS IS BECAUSE DEBUG MODE IS ON)")
                config = load_config()
                print("FINISHED RELOADING CONFIG")
        except KeyError:
            pass
    if config:
        return render_template(
            f"versions/{str(config['version'])}.html",
            config=config["settings"],
            more=config,
            version=skarf_version,
        )
    else:
        return render_template("no_config.html", the_version=skarf_version)


@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static/", path)


@app.route("/res/<path:path>")
def send_res(path):
    return send_from_directory("res", path)


if __name__ == "__main__":
    app.run(port=80, host="0.0.0.0")
