from re import DEBUG
from typing import Text
from flask import Flask
from flask import send_from_directory, render_template, request, send_file
from flask.helpers import flash
from youtube import youtube
from instascrape import Reel
import os

from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/download_reel", methods=['POST', 'GET'])
def download_reel():

    # Instascrape Request
    link = request.form['reelurl']
    SESSIONID = "23463609043%3AcfaDFTV7EDxZvG%3A8"
    headers = {
        "User-Agent":
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "cookie": f'sessionid={SESSIONID};'
    }
    reel = Reel(link)
    reel.scrape(headers=headers)
    print(reel.video_url)
    # Downloading reel to user
    try:
        return redirect(reel.video_url)
    except Exception:
        return "Try Again Later"


@app.route("/youtube")
def hello():
    return render_template("youtube.html")


@app.route("/download_youtube", methods=['POST', 'GET'])
def download_youtube():
    link = request.form['reelurl']
    url = youtube(link)
    return redirect(url)

if (__name__ == "__main__"):
    app.run(host='0.0.0.0', debug=False)
