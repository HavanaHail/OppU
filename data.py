from models import TinyU
import random

names = ["Bridget", "Jet", "Hailey","Jen", "Luis"]
races = ["black", "hispanic", "white", "asian"]
socialclass = ["Upper Class","Upper Middle Class", "Lower Middle Class", "Working Class"]
grades = ["kindergarden", "1st", "2nd", "3rd"]

# a way to be multiple races
#first gen stuff!




def newtinydata():
    randrace = random.choice(races)
    randname = random.choice(names)
    randsocialclass = random.choice(socialclass)

    print("test")
    tinyperson = TinyU(age=5, race=randrace, name=randname, social_class=randsocialclass, is_current=True)
    #email="jarry.",
    tinyperson.put()
#    is_current = false
    return tinyperson

def stats():
    Private_school = lifeEvent(shiftkey=1, name ="", description = "", forAge = "", lifeEvent = "")
#age up button
#def age():
 #age starts off as 5
 #age goes up by one





def getGrade(age):
#matches age to grade
#takes age in as argument
    if age < 9:
       num = age - 5
       grade =  grades[num]
       return grade
    elif age < 18:
        num = age - 5
        grade = str(num) + "th"
        return grade
    elif age >= 18:
        status = "highschool graduate"
        return status
