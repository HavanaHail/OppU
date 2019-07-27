from models import TinyU, lifeEvent
import random

names = ["Bridget", "Jet", "Hailey", "Jen", "Luis"]
races = ["Black", "Hispanic", "White", "Asian"]
socialclass = ["Upper Class", "Middle Class", "Lower Class"]
twoschools = ["Public School", "Private School"]
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
    tinyperson = TinyU(age=11, race=randrace, name=randname, social_class=randsocialclass, ela_test_score=6)
    return tinyperson

def getGrade(age):
#matches age to grade
#takes age in as argument

    if age < 18:
        num = age - 5
        newGrade = str(num) + "th"
        return newGrade
    elif age >= 18:
        newGrade = "highschool graduate"
        return newGrade

#age up button
def ageUp(tinyperson):
    pastAge = tinyperson.age
    tinyperson.age += 1
    newAge = tinyperson.age

    randschool = typeschool(tinyperson)
    newGrade = getGrade(newAge)
    return newAge, randschool, newGrade

def lifeEvent1(tinyperson):
    School_choice = lifeEvent(title="School Choice", description="You are now applying for high school! You have the option of applying to either public school or private school. Which will you choose?", forAge=13)
    return School_choice

def lifeEvent2(tinyperson):
    College_readiness = lifeEvent(title="Standardized Testing", description="You now have to take the SAT to apply for college. Would you like to attend paid tutoring sessions to help prepare for the exam?", forAge=16)
    return College_readiness

def typeschool(tinyperson):
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
            return randschoolMCW
        elif tinyperson.social_class == "Upper Class":
            randschoolUCW = random.choice(typesOfSchoolsforUCW)
            return randschoolUCW
    if tinyperson.race == "Asian":
        if tinyperson.social_class == "Lower Class":
            randschoolLCA = random.choice(typesOfSchoolsforLCA)
            return randschoolLCA
        elif tinyperson.social_class == "Middle Class":
            randschoolMCA = random.choice(typesOfSchoolsforMCA)
            return randschoolMCA
        elif tinyperson.social_class == "Upper Class":
            randschoolUCA = random.choice(typesOfSchoolsforUCA)
            return randschoolUCA



#age up button
#def age():
 #age starts off as 5
 #age goes up by one
