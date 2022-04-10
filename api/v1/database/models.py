from mongoengine import Document, StringField,DateTimeField


class New(Document):
    image = StringField(required=True)
    title = StringField(required=True)
    sybTitle = StringField(required=True)
    date = DateTimeField(required=True)
    body = StringField(required=True)


class Wiki(Document):
    image = StringField(required=True)
    model = StringField(required=True)
    title = StringField(required=True)
    cat = StringField(required=True)
    body = StringField(required=True)