import webapp2
import os
import jinja2
import data
from models import TinyU
#from data import newtinydata, getGrade, ageUp, lifeEvent1, lifeEvent2, typeschool

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage((webapp2.RequestHandler)):
    def get(self):
        new_tinyperson = data.newtinydata()
        new_tinyperson.put()
#        self.response.headers['Content-Type'] = 'text/html'

        name = new_tinyperson.name
        age  = new_tinyperson.age
        race  = new_tinyperson.race
        social_class = new_tinyperson.social_class
        user_grade = data.getGrade(age)

        template_vars = {
        "Name": name,
        "Age": age,
        "race": race,
        "Social_Class": social_class,
        "Grade": user_grade
        }

        start_template=jinja_env.get_template("PageTwo.html")
        self.response.write(start_template.render(template_vars))

    def post(self):

        person = TinyU.query().get()

        name = person.name
        age  = person.age
        race  = person.race
        social_class = person.social_class
        user_grade = data.getGrade(age)


        newAge, randschool, newGrade = data.ageUp(person)
        person.put()

        template_vars = {
        "Name": name,
        "Age": newAge,
        "race": race,
        "Social_Class": social_class,
        "Grade": newGrade
        }

        start_template=jinja_env.get_template("PageTwo.html")
        self.response.write(start_template.render(template_vars))

        print randschool
        print newAge
        print randschool





app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
