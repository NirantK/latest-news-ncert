# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os, json, urllib
from flask import Flask, jsonify

from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 \
  as Features

app = Flask(__name__)

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

@app.route('/myapp')
def WelcomeToMyapp():
    return 'Welcome again to my app running on Bluemix!'

@app.route('/api/people')
def GetPeople():
    list = [
        {'name': 'John', 'age': 28},
        {'name': 'Bill', 'val': 26}
    ]
    return jsonify(results=list)

@app.route('/api/people/<name>')
def SayHello(name):
    message = {
        'message': 'Hello ' + name
    }
    return jsonify(results=message)

# @app.route('/api/text/')
def readfile():
    # hard_override_filename = "static\\books\\class6-sci\\fesc102.txt"
    # root_dir = "https://raw.githubusercontent.com/NirantK/ncert/master/"
    # filename = root_dir + content + "/" + "fesc" + chapter + ".txt"
    filename = "https://raw.githubusercontent.com/NirantK/ncert/master/class6-sci/fesc101.txt"
    text = urllib.request.urlopen(filename).read()
    # fp = open(filename, 'rb')
    # text = fp.read()
    return(text)

@app.route('/api/nlp/')
def processText():
    in_text = readfile()
    in_text = str(in_text)
    print(in_text)

    natural_language_understanding = NaturalLanguageUnderstandingV1(
        username = 'username',
        password ='password',
        version="2017-02-27")

    response = natural_language_understanding.analyze(text=in_text,
    features=[
        Features.Concepts(
            # Concepts options
            limit=50
        ),
        Features.Keywords(
          # Keywords options
          # sentiment=True,
          # emotion=True,
          limit=10
        )
        ]
    )

    print(json.dumps(response, indent=2))
    return jsonify(response)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
