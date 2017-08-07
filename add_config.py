import sys
import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
  username='baba5abd-0342-4418-a917-d9b120b23c31',
  password='RIUok8yT0g2n',
  version='2017-08-01'
)

environments = discovery.get_environments()
print(json.dumps(environments, indent=2))

#  if x['name'] == 'Watson Discovery News Environment'
news_environments = [x for x in environments['environments']]
news_environment_id = news_environments[0]['environment_id']
print(json.dumps(news_environment_id, indent=2))

with open(os.path.join(os.getcwd(), 'config.json')) as config_data:
    data = json.load(config_data)
    new_config = discovery.create_configuration(news_environment_id, data)
    print(json.dumps(new_config, indent=2))