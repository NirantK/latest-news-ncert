# Topics to Relevant News Stories

## Recognition
The project was inteneded as an entry to the [Opened.ai AI for Education Hackathon 2017](www.opened.ai/index.html). We received a **Honorable Mention** for *Best use of IBM Watson API* alongside teams from 3 continents and universities like Oxford, CMU and Purdue. 

## What we do?
Generate relevant news articles for content the student is currently viewing using IBM Watson NLU API to extract key concepts from text and using IBM News API for retrieving related news clips.

## Demo
Please find the interactive demo at [Awesome NCERT](http://www.nirantk.in/awesome-ncert/)

## Dataset
- Dataset is available at [NirantK/ncert](https://github.com/NirantK/ncert/)
- Scrapped the Official NCERT textbooks for Class 6 Science (available as pdfs) 
- Converted them to text for easier data manipulation and Natural Language Processing

## Video
[Demo Video made for Opened.ai Hackathon](https://youtu.be/DVV10VSIevc)

### Process flow:
Read a NCERT Chapter (Natural Language Understanding) -> Find key concepts -> Find relevant news stories

### Intentions
By understanding the text book topics with their related new stories helps in enriching the user learning experience.

For example, while learning the text book topic such as “Where does food come from?” and it’s one of the related news such as "Botanists Say There's No Such Thing As Vegetables" and recommended to the student. To do this, we have processed the text books, and identify the news that can be mapped to the text book topics.

### Credits
1. Thanks for Anshul Baghi and Opened.ai team for organizing the *AI for Education* hackathon 2017
2. Thanks to IBM for the Watson NLU and News API which saved us a lot of time

### Run the app locally

1. [Install Python][]
1. cd into this project's root directory
1. Run `pip install -r requirements.txt` to install the app's dependencies
1. Run `python welcome.py`
1. Access the running app in a browser at <http://localhost:5000>

[Install Python]: https://www.python.org/downloads/
