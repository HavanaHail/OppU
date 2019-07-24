from google.appengine.ext import ndb

class TinyU(ndb.Model):
    age = ndb.IntegerProperty()
#grade would be a math equation
    race =  ndb.StringProperty()
#repeated = True
    name =  ndb.StringProperty()
    grade = ndb.StringProperty()
#    email =  ndb.StringProperty()
    social_class =  ndb.StringProperty()
    is_current =  ndb.BooleanProperty()
# first gen second gen stuff
class lifeEvent():
shiftkey = ndb.IntegerProperty()
name =  ndb.StringPropert()
description = ndb.TextProperty()
forAge = nbd.IntegerProperty()
lifeEvents = ndb.StringPropert(repeated = True)
