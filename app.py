from flask import Flask, render_template, request, abort, jsonify, Response, url_for

# Initialize your application.
app = Flask(__name__)

# And start building your routes.
@app.route('/template/<number>')
def index(number):
    try:
        return(render_template('template_0{}.html'.format(number)))
    except:
        pass

if __name__ == '__main__':
   app.run()