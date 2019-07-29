import webapp2
import os
import jinja2
import data
import models
#models.lifeEvent

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
#                   NEW USER
#
        list_of_people = models.TinyU.query(models.TinyU.is_current == True).fetch()
        for person in list_of_people:
            person.is_current = False
            person.put()

        new_tinyperson = data.newtinydata()
        new_tinyperson.is_current = True
        new_tinyperson.put()

        name = new_tinyperson.name
        age = new_tinyperson.age
        race = new_tinyperson.race
        social_class = new_tinyperson.social_class
        user_grade = data.getGrade(age)

        WordsForAge = "You are this old:"

        description = data.descriptions(new_tinyperson)
        extracurricular = data.extracurriculars(new_tinyperson)

        template_vars = {
        "Name": name,
        "Age": age,
        "race": race,
        "Social_Class": social_class,
        "Grade": user_grade,
        "WordsForAge": WordsForAge,
        "Description": description,
        "Extracurricular": extracurricular,
        }

        # life_event_vars = {
        # "Title": title,
        # "Description": description,
        # "forAge": forAge,
        # }

        start_template=jinja_env.get_template("PageTwo.html")
        self.response.write(start_template.render(template_vars))



    def post(self):

        person = models.TinyU.query(models.TinyU.is_current == True).get()

        newAge, randschool, newGrade, uniqueDescription = data.ageUp(person)
        person.put()

        # test
#       print person
        print randschool
        print newAge
        print uniqueDescription

        name = person.name
        age  = newAge
        race  = person.race
        social_class = person.social_class

        schoolChoice = data.lifeEvent1(person)

        WordsForAge = "You are currently this old:"
        # list_center(WordsForAge, newAge)

        template_vars = {
        "Name": name,
        "Age": newAge,
        "race": race,
        "Social_Class": social_class,
        "Grade": newGrade,
        "WordsForAge": WordsForAge,
        "school" : randschool,
        "person": person,
        #"center_text": center_text
        }

        start_template=jinja_env.get_template("PageTwo.html")
        self.response.write(start_template.render(template_vars))


app = webapp2.WSGIApplication([
    ('/', MainPage)

#    ('/experienceit',PageTwo)
], debug=True)
