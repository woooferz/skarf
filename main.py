from flask import Flask, render_template, redirect, jsonify, send_from_directory
import yaml

print("Loading Config...")
with open("config.yml", "r") as f:
    config = yaml.load(f.read(), Loader=yaml.Loader)
print("Loaded!")
# print(config)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(f"versions/{str(config['version'])}.html", config=config['settings'])


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)


@app.route('/webfonts/<path:path>')
def send_webfonts(path):
    return send_from_directory('static/webfonts', path)


@app.route('/img/<path:path>')
def send_images(path):
    return send_from_directory('static/images', path)


if __name__ == "__main__":
    app.run(port=80, host="0.0.0.0")
