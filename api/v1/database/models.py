import json

from mongoengine import Document, StringField


class New(Document):
    image = StringField(required=True)
    title = StringField(required=True)
    sybTitle = StringField(required=True)
    date = StringField(required=True)
    body = StringField(required=True)

    def __init__(self, image, title, sybTitle, date, body, *args, **values):
        super().__init__(*args, **values)
        self.image = image
        self.title = title
        self.sybTitle = sybTitle
        self.date = date
        self.body = body



class Wiki(Document):
    image = StringField(required=True)
    model = StringField(required=True)
    title = StringField(required=True)
    cat = StringField(required=True)
    body = StringField(required=True)

    def __int__(self, image, model, title, cat, body):
        self.image = image
        self.model = model
        self.title = title
        self.cat = cat
        self.body = body


