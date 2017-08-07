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
from flask import Flask, jsonify, send_from_directory

from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 \
  as Features

from watson_developer_cloud import DiscoveryV1

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


@app.route('/api/text/<fname>')
def readfile(fname):
    # return send_from_directory('static\\books', fname)    

    # hard_override_filename = "static\\books\\class6-sci\\fesc102.txt"
    # root_dir = "https://raw.githubusercontent.com/NirantK/ncert/master/"
    # filename = root_dir + content + "/" + "fesc" + chapter + ".txt"
    
    # filename = "https://raw.githubusercontent.com/NirantK/ncert/master/class6-sci/fesc101.txt"
    # text = urllib.request.urlopen(filename).read()
    try:
        fp = open(fname, 'rb')
        text = fp.read()
    except Exception as e:
        print(e)
        print('File not found')
        return('File not found')
    # text = app.send_static_file('fesc101.txt')
    # print(text)
    return(text)

# @app.route('/api/news/')
def get_news(query):
    discovery = DiscoveryV1(
        username = 'username',
        password = 'password',
        version='2017-08-01'
    )
    environments = discovery.get_environments()
    print(json.dumps(environments, indent=2))

    #  if x['name'] == 'Watson Discovery News Environment'
    news_environments = [x for x in environments['environments']]
    news_environment_id = news_environments[0]['environment_id']
    print(json.dumps(news_environment_id, indent=2))

    collections = discovery.list_collections(news_environment_id)
    news_collections = [x for x in collections['collections']]
    print(json.dumps(collections, indent=2))

    qopts = {'query': 'Fruit Seed Plant Omnivore'}
    my_query = discovery.query(news_environment_id, 'news', qopts)
    print(json.dumps(my_query, indent=2))
    return(jsonify(my_query))

@app.route('/api/nlp/<fname>')
def processText(fname):
    print('fname', fname)
    in_text = readfile(fname)
    in_text = str(in_text)
    
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        username = 'username',
        password = 'password',
        version="2017-02-27")

    response = natural_language_understanding.analyze(text=in_text,
    features=[
        Features.Concepts(
            # Concepts options
            limit=50
        ),
        # Features.Keywords(
        #   # Keywords options
        #   # sentiment=True,
        #   # emotion=True,
        #   limit=10
        # ),
        # Features.Entities(
        # )
        ]
    )

    # return jsonify(response)
    return json.dumps(response, indent=2)

@app.route('/api/news/<fname>/')
def construct_query(fname):
    response = json.loads(processText(fname))
    concepts = response['concepts']
    texts = [concept['text'] for concept in concepts]
    # print(texts)
    query = " ".join(texts)
    news = get_news(query)
    # return jsonify(response)
    return news

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
