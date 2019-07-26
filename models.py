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
    ela_test_score = ndb.IntegerProperty()
    type_of_school =  ndb.StringProperty()

    # is_current =  ndb.BooleanProperty()
#    location = ndb.StringProperty()
# first gen second gen stuff

class lifeEvent():
    title =  ndb.StringProperty()
    description = ndb.TextProperty()
    forAge = ndb.IntegerProperty()
