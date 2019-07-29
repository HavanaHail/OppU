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
        # for x in range(0, 3):
        #     person = models.TinyU.query(models.TinyU.is_current == True).get()
        #     person.is_current = false
        #     person.put()

        new_tinyperson = data.newtinydata()
#        new_tinyperson.is_current = True
        new_tinyperson.put()


        name = new_tinyperson.name
        age  = new_tinyperson.age
        race  = new_tinyperson.race
        social_class = new_tinyperson.social_class
        user_grade = data.getGrade(age)

        WordsForAge = "You are this old:"
        template_vars = {
        "Name": name,
        "Age": age,
        "race": race,
        "Social_Class": social_class,
        "Grade": user_grade,
        "WordsForAge": WordsForAge
        }

        start_template=jinja_env.get_template("PageTwo.html")
        self.response.write(start_template.render(template_vars))


    def post(self):


        person = models.TinyU.query().get()
#       person = models.TinyU.query(models.TinyU.is_current == True).get()


    def post(self):

        newAge, randschool, newGrade, uniqueDescription = data.ageUp(self.tinyperson)
        person.put()
        newAge, randschool, newGrade = data.ageUp(person)
        # test
#       print person
        print randschool
        print newAge
        print uniqueDescription

        WordsForAge = "You are this old:"
        # list_center(WordsForAge, newAge)

        template_vars = {
        "Name": name,
        "Age": newAge,
        "race": race,
        "Social_Class": social_class,
        "Grade": newGrade,
        "WordsForAge": WordsForAge,
        "school" : randschool,
        #"center_text": center_text

        }


        start_template=jinja_env.get_template("PageTwo.html")
        self.response.write(start_template.render(template_vars))

        start_template=jinja_env.get_template("PageTwo.html")
        self.response.write(start_template.render(template_vars))

app = webapp2.WSGIApplication([
    ('/', MainPage)

    ('/experienceit',PageTwo)
], debug=True)
