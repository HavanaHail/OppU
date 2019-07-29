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
    print newAge

    randschool = typeschool(tinyperson)
    newGrade = getGrade(newAge)
    uniqueDescription = descriptions(tinyperson)

    return newAge, randschool, newGrade, uniqueDescription

def lifeEvent1(tinyperson):
    School_choice = lifeEvent(title="School Choice", description="You are now applying for high school! You have the option of applying to either public school or private school. Which will you choose?", forAge=13)
    return School_choice, uniqueDescription
    print School_choice

def lifeEvent2(tinyperson):
    College_readiness = lifeEvent(title="Standardized Testing", description="You now have to take the SAT to apply for college. Would you like to attend paid tutoring sessions to help prepare for the exam?", forAge=16)
    return College_readiness
    print College_readiness

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

def descriptions(tinyperson):
    if tinyperson.race == "Black" or tinyperson.race == "Hispanic":
        if tinyperson.social_class == "Lower Class":
            randschoolLCBH = random.choice(typesOfSchoolsforLCBH)
            # return randschoolLCBH
            if randschoolLCBH == "Predom BH":
                popUpDescription = "You attend a school with extremely limited resources. You find it difficult to search for more extracurriculars that peak your interest, and there's very few Honors or AP courses that you can take to push your academic capabilities."
                print popUpDescription
            else:
                popUpDescription = "You attend a school that exhibits more diversity, which is more commonly found in schools in Queens or Manhattan. While your high school may have more resources available, you still find it difficult to find more opportunities to support students from your background."
                print popUpDescription
        elif tinyperson.social_class == "Middle Class":
            randschoolMCBH = random.choice(typesOfSchoolsforMCBH)
            # return randschoolMCBH
            if randschoolMCBH == "Predom BH":
                popUpDescription = "You attend a school with extremely limited resources. You find it difficult to search for more extracurriculars that peak your interest, and there's very few Honors or AP courses that you can take to push your academic capabilities."
                print popUpDescription
            else:
                popUpDescription = "While your high school could potentially be lacking in resources, you don't see it as much of an impediment to your success. You're available to afford things such as test prep and prestigious summer programs that make up for what your high school may lack."
                print popUpDescription
        else:
            randschoolUCBH = random.choice(typesOfSchoolsforUCBH)
            # return randschoolUCBH
            if randschoolUCBH == "Predom BH":
                popUpDescription = "While your high school could potentially be lacking in resources, you don't see it as much of an impediment to your success. You're available to afford things such as test prep and prestigious summer programs that make up for what your high school may lack."
                print popUpDescription
            else:
                popUpDescription = "As someone belonging in the Upper Class bracket, you have the ability to go into private school, which will prepare you well into getting into selective colleges in the country. Your school is filled with resources, and you feel as if there's so many opportunities available that it's unfortunate that you can't do everything your heart desires."
                print popUpDescription

    if tinyperson.race == "White":
        if tinyperson.social_class == "Lower Class":
            randschoolLCW = random.choice(typesOfSchoolsforLCW)
            # return randschoolLCW
            if randschoolLCW == "Predom W":
                popUpDescription = "While it may be economically challenging for your family to support you academically, you might be in a school that can aid you in your educational endeavors."
                print popUpDescription
            else:
                popUpDescription = "You attend a school that exhibits more diversity, which is more commonly found in schools in Queens or Manhattan. While your high school may have more resources available, you still find it difficult to find more opportunities to support students from your background."
                print popUpDescription
        elif tinyperson.social_class == "Middle Class":
            randschoolMCW = random.choice(typesOfSchoolsforMCW)
            # return randschoolMCW
            if randschoolMCW == "Predom W":
                popUpDescription = "You attend a school with an abundance of resources. You never get tired of finding activities to do in high school, and you have quick, instant access to a support system of any kind when you need it."
                print popUpDescription
            else:
                popUpDescription = "You attend a school that exhibits more diversity, which is more commonly found in schools in Queens or Manhattan. Your high school may have more resources available."
                print popUpDescription
        else:
            randschoolUCW = random.choice(typesOfSchoolsforUCW)
            # return randschoolUCW
            if randschoolUCW == "Predom W":
                popUpDescription = "You attend a school with an abundance of resources. You never get tired of finding activities to do in high school, and you have quick, instant access to a support system of any kind when you need it."
                print popUpDescription
            else:
                popUpDescription = "While your high school could potentially be lacking in resources, you don't see it as much of an impediment to your success. You're available to afford things such as test prep and prestigious summer programs that make up for what your high school may lack."
                print popUpDescription

    if tinyperson.race == "Asian":
        if tinyperson.social_class == "Lower Class":
            randschoolLCA = random.choice(typesOfSchoolsforLCA)
            # return randschoolLCA
            if randschoolLCA == "Predom A":
                popUpDescription = "You attend a school with an abundance of resources. You never get tired of finding activities to do in high school, and you have quick, instant access to a support system of any kind when you need it."
                print popUpDescription
            else:
                popUpDescription = "You attend a school with an abundance of resources. You never get tired of finding activities to do in high school, and you have quick, instant access to a support system of any kind when you need it."
                print popUpDescription
        elif tinyperson.social_class == "Middle Class":
            randschoolMCA = random.choice(typesOfSchoolsforMCA)
            # return randschoolMCA
            if randschoolMCA == "Predom A":
                popUpDescription = "You attend a school with an abundance of resources. You never get tired of finding activities to do in high school, and you have quick, instant access to a support system of any kind when you need it."
                print popUpDescription
            else:
                popUpDescription = "You attend a school with an abundance of resources. You never get tired of finding activities to do in high school, and you have quick, instant access to a support system of any kind when you need it."
                print popUpDescription
        elif tinyperson.social_class == "Upper Class":
            randschoolUCA = random.choice(typesOfSchoolsforUCA)
            # return randschoolUCA
            if randschoolUCA == "Predom A":
                popUpDescription = "You attend a school with an abundance of resources. You never get tired of finding activities to do in high school, and you have quick, instant access to a support system of any kind when you need it."
                print popUpDescription
            else:
                popUpDescription = "While your high school could potentially be lacking in resources, you don't see it as much of an impediment to your success. You're available to afford things such as test prep and prestigious summer programs that make up for what your high school may lack."
                print popUpDescription


#age up button
#def age():
 #age starts off as 5
 #age goes up by one
