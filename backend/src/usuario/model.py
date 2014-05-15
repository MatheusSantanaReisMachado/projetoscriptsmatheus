# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from google.appengine.ext import ndb

__author__ = 'Matheus'

class Usuario (ndb.Model):
    nome = ndb.StringProperty()
    email = ndb.StringProperty()
    google_id = ndb.StringProperty()

    @classmethod
    def query_by_google(cls, google_id):
        return cls.query(cls.google_id == google_id)