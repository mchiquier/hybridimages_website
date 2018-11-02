from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask import request, render_template, flash, redirect, url_for
from flask import send_from_directory, send_file
from werkzeug.utils import secure_filename
from scipy import misc
import numpy
import time
import os
from calculations import hybridImage

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__, template_folder='templates')
api = Api(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'my unobvious secret key'
count = 0


@app.route('/', methods=['GET'])
def home():
    count = 0
    images = os.listdir('/Users/miachiquier/test2/hybrid_website/static/images')
    img1 = images[count]
    img2 = images[count + 1]
    count = count + 1
    return render_template("webpage.html",file1=img1,file2=img2)
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/process', methods = ['GET', 'POST'])
def process():
    high_pass_threshold = request.form.get('highpassthresh')
    low_pass_threshold = request.form.get('lowpassthresh')
    images = os.listdir('/Users/miachiquier/test2/hybrid_website/static/images')
    img1 = images[0]
    img2 = images[1]
    highFreqPath = ''
    lowFreqPath = ''
    if request.method == 'POST':
        hybrid = hybridImage('static/images/' + img1, 'static/images/' + img2, int(high_pass_threshold), int(low_pass_threshold))

        sec = str(round(time.time() * 1000))+ ".png"
        misc.imsave("static/results/" + sec, numpy.real(hybrid))
        return "static/results/" + sec
    #return on the desk and then put it back out 

    return 'images/marilyn-einstein.png'
    #send_file('images/einstein.png')
if __name__ == '__main__':
    app.run(debug=False)