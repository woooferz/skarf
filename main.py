import json
import os
from distutils.dir_util import copy_tree

import yaml
from flask import Flask, render_template, send_from_directory
import requests

skarf_version = "v0.2.6"

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
    if config:
        for i in config['settings']['links']:
            try:
                i['copy']
            except KeyError:
                i['copy'] = False
        try:
            for i in config['settings']['mini-links']:
                try:
                    i['copy']
                except KeyError:
                    i['copy'] = False
        except KeyError:
            pass
    else:
        try:
            print("Attempting to download example config(s).")
            example_yml_t = ""
            example_json_t = ""
            print("Starting YAML Download")

            example_yml = requests.get(
                "https://raw.githubusercontent.com/woooferz/skarf/master/config/config.yml", timeout=3)
            example_yml_t = ""
            example_json_t = ""
            if example_yml.status_code >= 200 and example_yml.status_code < 300:
                example_yml_t = example_yml.text
            else:
                return None
            with open("config/config.yml", "w") as f:
                f.write(example_yml_t)
            print("Example YAML Downloaded!")
            print("Starting YAML Download")
            example_json = requests.get(
                "https://raw.githubusercontent.com/woooferz/skarf/master/config/config.json", timeout=3)
            if example_json.status_code >= 200 and example_json.status_code < 300:
                example_json_t = example_json.text
            else:
                return None
            with open("config/config.json", "w") as f:
                f.write(example_json_t)
            print("Example JSON Downloaded!")
            config = load_config()
        except requests.ConnectionError:
            print("Failed.")

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
try:
    if config:
        if config['static'] and config['version']:
            print("Static Mode: ON")
            from jinja2 import Environment, FileSystemLoader

            file_loader = FileSystemLoader('templates')
            env = Environment(loader=file_loader)

            template = env.get_template(
                f"versions/{str(config['version'])}.html")

            output = template.render(config=config["settings"],
                                     more=config,
                                     version=skarf_version,)
            try:
                with open("build/index.html", "w") as f:
                    f.write(output)
            except FileNotFoundError:
                os.mkdir("build")
                with open("build/index.html", "w") as f:
                    f.write(output)

            copy_tree("res", "build/res")
            copy_tree("static", "build/static")
            print("Success.\n\nExiting!")
            exit()
except KeyError:
    pass
app = Flask(__name__)


@ app.route("/")
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


@ app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static/", path)


@ app.route("/res/<path:path>")
def send_res(path):
    return send_from_directory("res", path)


if __name__ == "__main__":
    app.run(port=80, host="0.0.0.0")
