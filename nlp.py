# import requests
# r = requests.get('https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2017-02-27&text=I%20still%20have%20a%20dream%2C%20a%20dream%20deeply%20rooted%20in%20the%20American%20dream%20%E2%80%93%20one%20day%20this%20nation%20will%20rise%20up%20and%20live%20up%20to%20its%20creed%2C%20%22We%20hold%20these%20truths%20to%20be%20self%20evident%3A%20that%20all%20men%20are%20created%20equal.&features=entities,keywords', 
# 	auth=('f574cea4-378e-4808-adc5-be02d2a1a976', 'p2aIUnoBazzl'))
# # print('r.status_code', r.status_code)
# print('r.headers[content-type]', r.headers['content-type'])
# print(r.json())

import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 \
  as Features

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username="f574cea4-378e-4808-adc5-be02d2a1a976",
  password="p2aIUnoBazzl",
  version="2017-02-27")

response = natural_language_understanding.analyze(
   text="IBM has one of the largest workforces in the world",
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