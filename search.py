import sys
import os
import json

discovery = DiscoveryV1(
    username = 'username',
    password ='password',
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

qopts = {'query': 'petrol'}
my_query = discovery.query(news_environment_id, 'news', qopts)
print(json.dumps(my_query, indent=2))