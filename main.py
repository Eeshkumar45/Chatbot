
from flask import *

app = Flask(__name__)


@app.route("/")
def sendToWebsite():
    return render_template("chatbotPage.html")

i = 0
@app.route("/get")
def getFromWebsite():
    global i
    i+=1
    return str(i)



if __name__ == '__main__':
    app.run()