class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="sarjuthakkar",
    password="*****",
    hostname="sarjuthakkar.mysql.pythonanywhere-services.com",
    databasename="sarjuthakkar$default",
)
    SQLALCHEMY_POOL_RECYCLE = 299
    SQLALCHEMY_TRACK_MODIFICATIONS = False
