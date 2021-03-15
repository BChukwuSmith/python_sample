# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
# [START gae_python3_app]
from flask import Flask, request,render_template


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

#@app.route('/index')
@app.route('/')
def hello():
    return 'test' ## render_template('index.html')
    # return render_template(index.html, "Successful" if success else "Failed")
    # if request.form["submit"] == "submit":
    #     name = request.form['name']
    #     quest = request.form['quest']
    #     success = process(name, quest)
    # return render_template(index.html, "Successful" if success else "Failed")
    """Return a friendly HTTP greeting."""
    # return 'Hello World! <br/> Chioma is the best! <br/> \
    # Hi Bapu! <br/> \
    # Yaya\'s garden is so nice! <br/> \
    # Great, Yaya is so nice! <br/><br/> \
    # who is nicer than yaya?<br/><br/> yaya grden \
    # is so nice!<br/><br/> \
    # Hi Brian and Samuel! I added a .py file below <br/><br/> \
    # I hope it works!<br/><br/> \
    # i love yaya bapu<br/><br/> \
    # my name is samuel i love yaya and bapu\
    # <form action="/" methods=["GET","post">\
    #     Name:<br /> \
    #     <input type="text" name = "Name"><br /> \
    #     Quest:<br /> \
    #     <input type="text" quest="Quest"><br /> \
    #     <input type="submit" value="submit"> \
    # </form>'

# @app.route('/index')
# def index():
#     # if request.method == "GET":
#     if request.form["submit"] == "submit":
#         name = request.form['name']
#         quest = request.form['quest']
#         success = process(doritos, oreos)
#         return render_template(index.html, "Successful" if success else "Failed")


    # {% if Quest is not none %} \
    #     {{ challenge }} \
    # { % endif %} \
    # {% if Name is not none %} \
    #     {{ welcome }} \
    # { % endif %}'

# Sample code
# @app.route('/index', methods=['GET', 'POST'])
# def index():
#     if request.method == "GET":
#         return render_template("index.html")
#
#     if request.form["submit"] == "submit":
#         doritos = request.form["doritos"]
#         oreos = request.form["oreos"]
#         success = process(doritos, oreos)
#
#         return render_template("index.html", "Successful" if success else "Failed")
#
#      elif request.form["submit"] == "pita":
#         success = process("pita")
#         return render_template("index.html", "Successful" if success else "Failed")
#
#      elif request.form["submit"] == "chip":
#         success = process("chip")
#         return render_template("index.html", "Successful" if success else "Failed")


# Sample code on templates
# @app.route('/')
# def index():
#     return render_template(
#         'weather.html',
#         data=[{'name':'Toronto'}, {'name':'Montreal'}, {'name':'Calgary'},
#               {'name':'Ottawa'}, {'name':'Edmonton'}, {'name':'Mississauga'},
#               {'name':'Winnipeg'}, {'name':'Vancouver'}, {'name':'Brampton'},
#               {'name':'Quebec'}])
#
# @app.route("/result" , methods=['GET', 'POST'])
# def result():
#     data = []
#     error = None
#     select = request.form.get('comp_select')
#     resp = query_api(select)
#     pp(resp)
#     if resp:
#         data.append(resp)
#         if len(data) != 2:
#             error = 'Bad Response from Weather API'
#             return render_template(
#                 'result.html',
#                 data=data,
#                 error=error)


# def welcome(name):
#     return 'Welcome sir ' + name
#
# @app.route('/Quest')
# def challenge():
#     return 'You seek the Grail?!'

# Bapu added this program.
# He also added this comment -- the delay loop is very sensitive to where the return statement is place relative to the nested loops. To change delay change number of interations of loops
namestring="SamuelChukwuSmith"
def delay():
    for j in range (20000):
        q= 434345. / 4.555
        for k in range (2000):
            junk =3.666577545 /4.66666456
            for n in range (2000):
                p = 665432.234 / 4.777
        return junk
for i in range (6):
    modstring = namestring
    print("*" + modstring + "*")
    wait = delay()
    modstring = namestring[1:16]
    print(" *" + modstring + "*")
    wait = delay()
    modstring = namestring[2:15]
    print("  *" + modstring + "*")
    wait = delay()
    modstring = namestring[3:12]
    print("    *" + modstring + "*")
    wait = delay()
    modstring = namestring[5:10]
    print("      *" + modstring + "*")
    wait = delay()
    modstring = namestring[7:8]
    print("         **")
    wait = delay()
    modstring = namestring[5:10]
    print("      *" + modstring + "*")
    wait = delay()
    modstring = namestring[3:12]
    print("    *" + modstring + "*")
    wait = delay()
    modstring = namestring[2:15]
    print("  *" + modstring + "*")
    wait = delay()
    modstring = namestring[1:16]
    print(" *" + modstring + "*")
    wait = delay()
    modstring = namestring
    print("*" + modstring + "*")
    wait = delay()























if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
