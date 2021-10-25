from flask import Flask
from flask import render_template, request, send_file, redirect

from instascrape import Reel
app = Flask(__name__)
app.static_folder = "./static"


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/download_reel", methods=['POST', 'GET'])
def download_reel():

    # Instascrape Request
    link = request.form['reelurl']
    SESSIONID = "47363229164%3ABsZWZOQRxmDnYY%3A29"
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
        return redirect(reel.video_url+"&dl=1")
    except Exception:
        return "Try Again Later"


if(__name__ == "__main__"):
    app.run(host='0.0.0.0', debug=True)
