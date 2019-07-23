from google.appengine.ext import ndb

class TinyU(ndb.Model):
    age = ndb.IntegerProperty()
#grade would be a math equation
    race =  ndb.StringProperty()
    name =  ndb.StringProperty()
    email =  ndb.StringProperty()
    social_class =  ndb.StringProperty()
    is_current =  ndb.BooleanProperty()
