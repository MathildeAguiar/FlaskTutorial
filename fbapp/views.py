from flask import Flask, render_template, url_for, request

app = Flask(__name__)

app.config.from_object('config') #just config not config.py

from .utils import find_content

@app.route('/')


@app.route('/index/')
def index():
    # here we define what will we displayed on the index page 
    # we need the description, the blur parameter, what page it's linked to  
    description = """
        Ready to find out what delicious you are ? Connect to Facebook to find out !
    """
    return render_template('index.html',
        blur = True,
        description = description,
        user_img = url_for('static', filename= 'img/baozi.jpg'),
        user_name = "秋さん"
    )

@app.route('/result/')
def result():
    gender = request.args.get('gender') 
    user_name = request.args.get('first_name') #taken out of Facebook URL
    uid = request.args.get('id')
    #description = "おめでとうございます！" + user_name + "餃子です。"
    profile_pic = "http://graph.facebook.com/" + uid + "/picture?type=large" 

    return render_template(
        'result.html',
        user_name = user_name, 
        description = find_content(gender).description, #descriptions in the db are needed!!
        user_img = profile_pic #taken out of Facebook 
    )


if __name__ == "__main__":
    app.run()