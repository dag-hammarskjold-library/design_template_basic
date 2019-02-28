from flask import Flask, render_template, request, abort, jsonify, Response, url_for
#from requests import get
#from bson.objectid import ObjectId
#from config import Config
#import boto3, re, time, os, pymongo

# Initialize your application.
app = Flask(__name__)
#collection = Config.DB.pressReleases

# Define any classes you want to use here, or you could put
# them in other files and import.

# And start building your routes.
@app.route('/template/<number>')
def index(number):
    try:
        return(render_template('template_0{}.html'.format(number)))
    except:
        pass

if __name__ == '__main__':
   app.run()