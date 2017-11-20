from flask import Flask
from flask_mail import Mail
from flask_mail import Message

app = Flask(__name__)
mail = Mail(app)
@app.route('/<name>/<email>/<message>', methods=['POST'])
def handle_data(name,email,message):
    msg = Message(message,
                  subject=name
                  sender=email,
                  recipients=["anjanbharadwaj02@gmail.com"])
    mail.send(msg)
    # your code
    # return a response
@app.route("/upload/<documentName>", methods=['POST'])
def upload(documentName):
    with open(os.path.join("/home/pi/Documents/WebServer/dropbox/", documentName), 'wb') as temp_file:
        temp_file.write(buff)

    return documentName
