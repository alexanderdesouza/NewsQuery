# NewsQuery
_NewsQuery_ is a Flask-driven web-application that demonstrates basic semantic natural language processing and text
analysis. The baseline corpus is taken from headlines of the Australian Broadcasting Corporation (ABC News, for articles published between 2003 and 2016). The data was originally obtained from user "_therohk_" and is publically available at
https://www.kaggle.com/therohk/million-headlines.

## Setup
### Dependencies
Built using Python 3.7; the code has not been verified against earlier versions. Installation additionally requires
`virtualenv`.
### Installation
Clone the repository to your local machine:
```
git clone https://github.com/alexanderdesouza/NewsQuery
```
Enter the directory and setup a virtual environment there, activate the virtual environment, and install the
application's requirements:
```
cd newsQuery
virtualenv newsQuery
source newsQuery/bin/activate
pip3 install -r requirements.txt
```

## Running the Application
Once setup is complete the application can be launched from the command line as follows:
```
python main.py
```
The site will be hosted locally at http://127.0.0.1:5000/.

_Please note that functionality has only been verified using Chrome (latest as of 13 Sep 2018)._

## Exploration
The `exploration` folder contains two iPyNb that explore different models for semantically tagging documents,
identifying and comparing similar documents, and the possibility of updating the models iteratively (incomplete).

* `data_and_model_exploration.ipynb` attempts to solve this problem with a traditional, albeit simple here, TF-IDF
approach.
* `doc2vec_experiment.ipynb` makes use of a Doc2Vec model for document identification. Tagging and model updates were
not implemented in this notebook.
