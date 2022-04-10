class BaseConfig:
    HOST = "0.0.0.0"
    PORT = 5100
    DEBUG = False


class Development(BaseConfig):
    PORT = 5100
    MONGODB_URL = "mongodb://admin:admin@cluster0.kkv90.mongodb.net/test"
    DEBUG = True


class Testing(BaseConfig):
    MONGODB_URL = "mongodb://admin:admin@cluster0.kkv90.mongodb.net/test"



class Prod(BaseConfig):
    MONGODB_URL = "mongodb://admin:admin@cluster0.kkv90.mongodb.net/test"

