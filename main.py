
from flask import *

import chatbot

app = Flask(__name__)


@app.route("/")
def sendToWebsite():
    return render_template("chatbotPage.html")

@app.route("/get")
def getFromWebsite():
    s = chatbot.getMessage();
    return s



if __name__ == '__main__':
    app.run()