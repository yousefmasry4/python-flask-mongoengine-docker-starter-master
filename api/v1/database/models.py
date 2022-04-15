from mongoengine import Document, StringField, DateTimeField


class New(Document):
    image = StringField(required=True)
    title = StringField(required=True)
    sybTitle = StringField(required=True)
    date = DateTimeField(required=True)
    body = StringField(required=True)

    def __init__(self, image, title, sybTitle, date, body):
        self.image = image
        self.title = title
        self.sybTitle = sybTitle
        self.date = date
        self.body = body

    def to_json(self, *args, **kwargs):
        return {
            'image': self.image,
            'title': self.title,
            'sybTitle': self.sybTitle,
            'date': self.date,
            'body': self.body,
            'id': self.id
        }


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

    def to_json(self, *args, **kwargs):
        return {
            'image': self.image,
            'model': self.model,
            'title': self.title,
            'cat': self.cat,
            'body': self.body,
            'id': self.id
        }

