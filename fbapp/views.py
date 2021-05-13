from flask import Flask, render_template, url_for, request

app = Flask(__name__)

app.config.from_object('config') #just config not config.py

from .utils import find_content

@app.route('/')


@app.route('/index/')
def index():
    if 'img' in request.args:
        img = request.args['img']
        og_url = url_for('index', img=img, _external=True)
        og_image = url_for('static', filename=img, _external=True)
    else:
        og_url = url_for('index', _external=True)
        og_image = url_for('static', filename='img/baozi.jpg', _external=True)

    page_title = "食べ物の性格のテスト"
    # here we define what will we displayed on the index page 
    # we need the description, the blur parameter, what page it's linked to  
    og_description = """
        Ready to find out what delicious you are ? Connect to Facebook to find out !
    """
    description = "あの夢をなぞって"
    return render_template('index.html',
        blur = True,
        page_title=page_title,
        description = description,
        og_url=og_url,
        og_image=og_image,
        og_description = og_description,
        user_img = url_for('static', filename= 'img/baozi.jpg'),
        user_name = "秋さん"
    )

@app.route('/result/')
def result():
    gender = request.args.get('gender') 
    user_name = request.args.get('first_name') #taken out of Facebook URL
    uid = request.args.get('id')
    img = 'img/cat.jpg'
    og_url = url_for('index', img=img, _external=True)
    #description = "おめでとうございます！" + user_name + "餃子です。"
    profile_pic = "http://graph.facebook.com/" + uid + "/picture?type=large" 

    return render_template(
        'result.html',
        user_name = user_name, 
        description = find_content(gender).description, #descriptions in the db are needed!!
        user_img = profile_pic, #taken out of Facebook
        og_url = og_url 
    )


if __name__ == "__main__":
    app.run()