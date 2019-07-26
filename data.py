from models import TinyU, lifeEvent
import random

names = ["Bridget", "Jet", "Hailey", "Jen", "Luis"]
races = ["Black", "Hispanic", "White", "Asian"]
socialclass = ["Upper Class", "Middle Class", "Lower Class"]
typesOfSchoolsforLCBH = ["Predom BH", "Not Predom", "Predom BH", "Predom BH", "Predom BH", "Predom BH", "Predom BH", "Predom BH", "Not Predom", "Not Predom"]
# 70% Predom BH
typesOfSchoolsforMCBH = ["Predom BH", "Not Predom", "Predom BH", "Predom BH", "Predom BH", "Predom BH", "Predom BH", "Predom BH", "Not Predom", "Not Predom"]
# 50% Predom BH
typesOfSchoolsforUCBH = ["Predom BH", "Not Predom", "Predom BH", "Not Predom", "Not Predom", "Predom BH", "Not Predom", "Not Predom", "Not Predom", "Not Predom"]
# 30% Predom BH
typesOfSchoolsforLCW = ["Not Predom W", "Not Predom W", "Not Predom W", "Not Predom W", "Not Predom W", "Not Predom W", "Predom W", "Predom W", "Predom W", "Predom W"]
# 40% Predom W
typesOfSchoolsforMCW = ["Not Predom W", "Not Predom W", "Not Predom W", "Not Predom W", "Predom W", "Predom W", "Predom W", "Predom W", "Predom W", "Predom W"]
# 60% Predom W
typesOfSchoolsforUCW = ["Not Predom W", "Not Predom W", "Predom W", "Predom W", "Predom W", "Predom W", "Predom W", "Predom W", "Predom W", "Predom W"]
# 80% Predom W
typesOfSchoolsforLCA = ["Not Predom A", "Not Predom A", "Not Predom A", "Not Predom A", "Not Predom A", "Not Predom A", "Not Predom A", "Not Predom A", "Not Predom A", "Predom A"]
# 10% Predom A
typesOfSchoolsforMCA = ["Not Predom A", "Not Predom A", "Not Predom A", "Not Predom A", "Not Predom A", "Not Predom A", "Not Predom A", "Not Predom A", "Predom A", "Predom A"]
# 20% Predom A
typesOfSchoolsforUCA = ["Not Predom A", "Not Predom A", "Not Predom A", "Not Predom A", "Not Predom A", "Not Predom A", "Not Predom A", "Predom A", "Predom A", "Predom A"]
# 30% Predom A

# a way to be multiple races
#first gen stuff!

def newtinydata():
    randrace = random.choice(races)
    randname = random.choice(names)
    randsocialclass = random.choice(socialclass)
#    randTestscore = random.randint(1,4)
    tinyperson = TinyU(age=11, race=randrace, name=randname, social_class=randsocialclass, ela_test_score=6, is_current=True)
    return tinyperson

def getGrade(age):
#matches age to grade
#takes age in as argument

    if age < 18:
        num = age - 5
        newGrade = str(num) + "th"
        return newGrade
    elif age >= 18:
        status = "highschool graduate"
        return newGrade

    #email="jarry.",
#    tinyperson.put()
#    is_current = false
#    return tinyperson


#age up button
def ageUp(tinyperson):
    pastAge = tinyperson.age
    tinyperson.age += 1
    newAge = tinyperson.age

    randschool = typeschool(tinyperson)
    newGrade = getGrade(newAge)
    return newAge,randschool,newGrade






def stats(tinyperson):

    School_choice = lifeEvent(shiftkey=0, name ="School Choice", description ="highschool process", forAge = 13)
    return School_choice
    #, lifeEvents = [1,2,3]
#    Private_school = lifeEvent(shiftkey=2, name ="", description = "", forAge = "", lifeEvent = "")
#LOOK INTO HARRY POTTER TUPLES

# if statmemnt for if age = life event ??
def typeschool(tinyperson):
#    if tinyperson.grade == School_choice.forAge:
    if tinyperson.race == "Black" or tinyperson.race == "Hispanic":
        if tinyperson.social_class == "Lower Class":
            randschoolLCBH = random.choice(typesOfSchoolsforLCBH)
            return randschoolLCBH
       elif tinyperson.social_class == "Middle Class":
            randschoolMCBH = random.choice(typesOfSchoolsforMCBH)
            return randschoolMCBH
       elif tinyperson.social_class == "Upper Class":
            randschoolUCBH = random.choice(typesOfSchoolsforUCBH)
            return randschoolUCBH
    if tinyperson.race == "White":
        if tinyperson.social_class == "Lower Class":
            randschoolLCW = random.choice(typesOfSchoolsforLCW)
            return randschoolLCW
        elif tinyperson.social_class == "Middle Class":
            randschoolMCW = random.choice(typesOfSchoolsforMCW)
            return randschoolLCW
        elif tinyperson.social_class == "Upper Class":
            randschoolUCW = random.choice(typesOfSchoolsforUCW)
            return randschoolLCW
    if tinyperson.race == "Asian":
        if tinyperson.social_class == "Lower Class":
            randschoolLCA = random.choice(typesOfSchoolsforLCA)
            return randschoolLCA
        elif tinyperson.social_class == "Middle Class":
            randschoolLCA = random.choice(typesOfSchoolsforMCA)
            return randschoolMCA
        elif tinyperson.social_class == "Upper Class":
            randschoolLCA = random.choice(typesOfSchoolsforUCA)
            return randschoolUCA

#    elif tinyperson.race == "White":
#            if tinyperson.social_class == "Low Income":
#                randschoolWA = random.choice(typesOfSchoolsforWA)
#                return randschoolWA
            #this is just so the console will shut up
#            else:
#              if tinyperson.social_class == "Middle Class":
#                  randschoolWA = random.choice(typesOfSchoolsforWA)
#            if tinyperson.social_class == "Upper Class":



#    else tinyperson.race == "Asian":
#                if tinyperson.social_class == "Lower Class":
#                if tinyperson.social_class == "Middle Class":
#                if tinyperson.social_class == "Upper Class":
#        randschoolWA = random.choice(typesOfSchoolsforWA)
#        return randschoolWA


#age up button
#def age():
 #age starts off as 5
 #age goes up by one
