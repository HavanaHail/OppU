import webapp2
import os
import jinja2
import data
from models import TinyU

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)



class MainPage(webapp2.RequestHandler):

    def get(self):
        tinyperson = data.newtinydata()
        self.response.headers['Content-Type'] = 'text/html'
#        self.response.write("HI")
        name = tinyperson.name
        age  = tinyperson.age
        race  = tinyperson.race
        social_class = tinyperson.social_class
        user_grade = data.getGrade(tinyperson.age)

        template_vars = {
        "Name": name,
        "Age": age,
        "race": race,
        "Social_Class": social_class,
        "Grade": user_grade
        }
#    def post(self):
        start_template=jinja_env.get_template("PageTwo.html")
        self.response.write(start_template.render(template_vars))


        newAge, randschool, newGrade = data.ageUp(tinyperson)
        print randschool
        print newAge





app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
