#!/usr/bin/python
# -*- coding: utf-8 -*-

import os.path
import xml.etree.ElementTree as ET


class Article:
    def __init__(self, tags=None, title=None, client=None, date=None, body=None, language="fr"):
        """
        Object that represent articles
        :param tags: Tags or topics of the article
        :type tags: list
        :param title: Title of the article
        :type title: str
        :param client: clients of the project
        :type client: str
        :param date: date of the article
        :type date: str
        :param body: Content of the article
        :type body: str
        :param language: Language of the article ex: fr, en, es
        :type language: str
        """
        self.tags = tags
        self.title = title
        self.client = client
        self.date = date
        self.body = body
        self.language = language


class MetaXML():
    def __init__(self, path):
        """

        :param path_list:
        :type path_list:
        """

