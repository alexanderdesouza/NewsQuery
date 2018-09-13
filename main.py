# !/usr/bin/env python3

from flask import Flask, render_template, request

app = Flask(__name__)

# Note:
# In the interest of time we use these two lists as a proxy for a more robust database solution. Both dictionaries are
# keyed with the same set of keys.
articles = []
articles_sentiment = {}

# Note:
# A full implementation might include separation of the application components along the lines of its routes into
# individual Python files in several sub-directories, and the main application instanced from inside something like a
# run.py file and including a config.py file as well.


def _article_exists(new_article):
    """
    Validates whether the new article to be added is new/unique.
        :param: new_article: String representation of a news article.
        :return: Boolean return whether or not new_article is already in the list 'articles'.
    """
    if new_article in articles:
        return True
    return False


@app.route('/query_articles', methods=['POST'])
def query_articles():
    """
    Query the list of existing articles and determine the top-most ranked
        :return: Re-renders the main template for the NewsQuery page.
    """
    # Do stuff...
    return render_template("newsquery.html", article_added_or_not="", articles=articles)


@app.route('/add_article', methods=['POST'])
def add_article():
    """
    This method asserts whether the supplied article to be added exists in the list `articles`, and if not, appends the
    new document to the list.
        :return: Re-renders the main template for the NewsQuery page, updating the variable `article_added_or_not` with
                 a String result if the article to be added was successfully appended to the list `articles`, or not.
    """
    new_article = request.form.get('article_to_add')
    article_added_or_not = "Document already exists; article not added."
    if not _article_exists(new_article):
        articles.append(new_article)
        article_added_or_not = "New article added!"
    return render_template("newsquery.html", article_added_or_not=article_added_or_not, articles=articles)


@app.route('/')
@app.route('/index')
def main():
    """
    This is the main webserver route called on application start.
        :return: Renders the main template for the NewsQuery page.
    """
    return render_template("newsquery.html", article_added_or_not="", articles=articles)


if __name__ == '__main__':
    app.run()
