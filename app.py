from re import DEBUG
from typing import Text
from flask import Flask
from flask import send_from_directory, render_template, request, send_file

from instascrape import Reel
import os

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
    # Deleting Download Folder
    dir = 'downloads'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

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

    # Downloading reel to website
    fname = reel.upload_date.strftime("%Y-%m-%d %Hh%Mm")
    reel.download(f"downloads/{fname}.mp4")
    path = "downloads\{}.mp4".format(fname)

    # Downloading reel to user
    return send_file(path, as_attachment=True)


@app.route("/hello"):
def hello():
    return "hello"


if (__name__ == "__main__"):
    app.run(host='0.0.0.0', debug=False)
