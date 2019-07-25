from models import TinyU
import random

names = ["Bridget", "Jet", "Hailey","Jen", "Luis"]
races = ["black", "hispanic", "white", "asian"]
socialclass = ["Upper Class","Middle Class", "Lower Class"]






# a way to be multiple races
#first gen stuff!




def newtinydata():
    randrace = random.choice(races)
    randname = random.choice(names)
    randsocialclass = random.choice(socialclass)
    randTestscore = random.randint(1,4)



    tinyperson = TinyU(age=11, race=randrace, name=randname, social_class=randsocialclass, ela_test_score=randTestscore, is_current=True)
    #email="jarry.",
    tinyperson.put()
#    is_current = false
    return tinyperson

def stats():
    test_prep = lifeEvent(shiftkey=1, name ="Test Prep", description = "Can you afford test prep?", forAge = 12, lifeEvent = "")
    Private_school = lifeEvent(shiftkey=2, name ="", description = "", forAge = "", lifeEvent = "")
#age up button
#def age():
 #age starts off as 5
 #age goes up by one





def getGrade(age):
#matches age to grade
#takes age in as argument

    if age < 18:
        num = age - 5
        grade = str(num) + "th"
        return grade
    elif age >= 18:
        status = "highschool graduate"
        return status
