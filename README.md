# NewsQuery
_NewsQuery_ is a Flask web-application that demonstrates basic semantic natural language processing and text analysis,
using headlines from the Australian Broadcasting Corporation (ABC News; between 2003 and 2016). The data was originally
obtained from user "_therohk_" at https://www.kaggle.com/therohk/million-headlines.

## Setup
Clone the repository to your local machine:
```
git clone https://github.com/alexanderdesouza/NewsQuery
```
Setup a virtual environment, activate it, and install the application's requirements:
```
virtualenv newsQuery
source newsQuery/bin/activate
pip3 install -r requirements.txt
```

## Running the Application
Once setup is complete the application can be launched from the command line as follows:
```
python main.py
```
The site will be hosted locally at http://127.0.0.1:5000/, which you can visit in your browser.

_Please note that functionality has only been verified using Chrome (latest as of 13 Sep 2018)._