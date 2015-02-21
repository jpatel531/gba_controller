import os
from flask import Flask, render_template, request
from flask.ext.pusher import Pusher
from flask.ext.cors import cross_origin


app = Flask(__name__)

app.config['PUSHER_APP_ID'] = os.environ.get('GB_PUSHER_APP_ID')
app.config['PUSHER_KEY'] = os.environ.get('GB_PUSHER_KEY')
app.config['PUSHER_SECRET']= os.environ.get('GB_PUSHER_SECRET')

pusher = Pusher(app)

@app.route("/")
def show_index():
	return render_template('control.html')

@pusher.auth
@cross_origin()
def pusher_auth(channel_name, socket_id):
	return socket_id

if __name__ == "__main__":
    app.run(debug=True)