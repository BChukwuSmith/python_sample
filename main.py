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
from flask import Flask


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World! <br/> Chioma is the best! <br/> \
    Hi Bapu! <br/> \
    Yaya\'s garden is so nice! <br/> \
    Great, Yaya is so nice! <br/><br/> \
    who is nicer than yaya?<br/><br/> yaya grden \
    is so nice!<br/><br/> \
    Hi Brian and Samuel! I added a .py file below <br/><br/> \
    I hope it works!<br/><br/> \
    i love yaya bapu<br/><br/> \
    my name is samuel i love yaya and bapu'

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
