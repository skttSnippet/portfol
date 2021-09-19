#### run the following in cmd before hand

# > mkdir myproject
# > cd myproject

# set the main folder as a virtual env
# > py -3\ -m venv foldername

# go to the main folder and run activate
# > foldername\Scripts\activate

# > set FLASK_APP=pyfilename.py
# > set FLASK_ENV=development
# > flask run

# THEN Running on http://127.0.0.1:5000/
# in flask server, htmls go to 'templates' folder
#                  css/js go to 'static' folder
#                  favicon goes to 'static' folder


from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
import csv

app = Flask(__name__)
print(__name__)

# in html file, flask includes a templating lib called 'jinjia' to define double curly brackets{{}}as expressions
# python counterpart of this will be print() func

'''
Variable Rules
You can add variable sections to a URL by marking sections with <variable_name>. Your function then receives the <variable_name> as a keyword argument. Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>.
from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
'''
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types
# Browsers use the so called MIME type, no the file extension, to determine how to process a URL
# so it's important that web servers send the correct MINME type in the response's Content-Type header.
# If this is not correctly configured, browsers are likely to misinterpret the contents of files and
# sites will not work correctly, and downloaded files maybe  mishandled.
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        #  'a' = append
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        #  'a' = append
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database,
                                delimiter=',',
                                quotechar='|',
                                quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'


# @app.route("/index.html")
# def my_home():
#     return render_template('index.html')
#
# @app.route("/about.html")
# def about():
#     return render_template('about.html')
#
# @app.route("/work.html")
# def work():

#     return render_template('work.html')
#
# @app.route("/works.html")
# def works():
#     return render_template('works.html')
#
# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')
#
# @app.route("/components.html")
# def components():
#     return render_template('components.html')

