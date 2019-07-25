from models import TinyU,lifeEvent
import random

names = ["Bridget", "Jet", "Hailey","Jen", "Luis"]
races = ["Black", "Hispanic", "White", "Asian"]
socialclass = ["Upper Class", "Middle Class", "Lower Class"]
typesOfSchoolsforBH = ["Predom BH", "Not Predom", "Predom BH", "Predom BH", "Predom BH", "Predom BH", "Predom BH", "Predom BH", "Not Predom", "Not Predom"]
typesOfSchoolsforWA = ["Predom BH", "Not Predom", "Predom BH", "Not Predom", "Not Predom", "Predom BH", "Not Predom", "Not Predom", "Not Predom", "Not Predom"]






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

def stats(tinyperson):


#    School_choice = lifeEvent(shiftkey=0, name ="School Choice", description = "highschool process", forAge = 13, lifeEvents = [""])
#    Private_school = lifeEvent(shiftkey=2, name ="", description = "", forAge = "", lifeEvent = "")

    #here is where there would be statistics
    #70% prem B and H   30% non Predom
    if tinyperson.race == "Black" or tinyperson.race == "Hispanic":
        if tinyperson.social_class == "Lower Class":
                    randschoolBH = random.choice(typesOfSchoolsforBH)
                    return randschoolBH
        if tinyperson.social_class == "Middle Class":
        if tinyperson.social_class == "Upper Class":

    elif tinyperson.race == "White":
            if tinyperson.social_class == "Lower Class":
                randschoolWA = random.choice(typesOfSchoolsforWA)
                return randschoolWA
            if tinyperson.social_class == "Middle Class":
            if tinyperson.social_class == "Upper Class":

        randschoolWA = random.choice(typesOfSchoolsforWA)
        return randschoolWA
    else tinyperson.race == "Asian":
#                if tinyperson.social_class == "Lower Class":
#                if tinyperson.social_class == "Middle Class":
#                if tinyperson.social_class == "Upper Class":
        randschoolWA = random.choice(typesOfSchoolsforWA)
        return randschoolWA


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
