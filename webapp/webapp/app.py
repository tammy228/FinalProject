from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title': 'HELLO!',
        'time': timeString
    }
    return render_template('index.html', **templateData)
 
@app.route('/<theAction>')
def takePictures(theAction):
    #if request.method == 'POST':
    if theAction != "":
        try:
            #raspistill -o <name>.jpg
            responseHere = "your choose to " + theAction + "."
        except:
            responseHere = "There was an error to " + theAction + "."
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title': theAction,
        'time': timeString
    }

    return render_template('index.html', response=responseHere, **templateData)

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
