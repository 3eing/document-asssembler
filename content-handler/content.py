#!/usr/bin/python
# -*- coding: utf-8 -*-
import configparser
from os.path import abspath
from docxtpl import DocxTemplate
from handling import Article

config = configparser.ConfigParser()
config.read("../config.ini")

class Content:
    def __init__(self, db, template=config["TEST"]["template"]):
        """
        Base class for content for document generation
        :param db: a MetaXML object containing texts to add to content
        """
        self.path = abspath(template)
        self.db = db
        self.document = DocxTemplate(self.path)
        self.context = {}

    def _get_texts_from_tags(self, tags, filter=None):
        """
        Return Articles object that contains parameters given as tags or kwargs
        Example: get_texts_from_tags('energy', 'ship', 'marine', client='Client name'):
        :param tags: Tags or topics wanted in the document
        :type tags: str
        :param kwargs: specific filter for the document (client, language, etc.)
        :type kwargs: str
        :return: a list of Articles objects
        :rtype: list of Article
        """
        return self.db.get_articles(tags, filter)

    def generate_context(self, tags, filter=None):
        """
        Generate the dict necessary to create document
        :param tags: Tags or topics wanted in the document
        :type tags: str
        :param kwargs: specific filter for the document (client, language, etc.)
        :type kwargs: str
        :return: number of articles contextualized
        :rtype: int
        """
        articles = self._get_texts_from_tags(tags, filter)
        i = 0
        for article in articles:
            i += 1
            self.context["client_{}".format(i)] = article.client
            self.context["title_{}".format(i)] = article.title
            self.context["date_{}".format(i)] = article.date
            self.context["body_{}".format(i)] = article.body
            self.context["language_{}".format(i)] = article.language

        return len(articles)


    def generate_docx(self, out_path=config["TEST"]["datasource"]):
        """
        Generate a docx from the content
        :param out_path: The path and filename of the docx
        :type out_path: str
        """
        out_path = abspath(out_path)
        self.document.render(self.context)
        self.document.save(out_path)


if __name__ == '__main__':
    class _db():
        def __init__(self, article):
            self.articles = [article]

        def get_articles(self, tags, filter):
            rep = []
            for article in self.articles:
                if set(tags) & set(article.tags):
                    rep.append(article)
            return rep


    article_1 = Article(tags=['test', 'test2', 'test3'], title='Essai', client='Moi', date='2022-07-06', body='Il était une fois un message', language="fr")
    db = _db(article_1)
    content = Content(db)
    content.generate_context(tags=('test', 'test1'))
    content.generate_docx()


