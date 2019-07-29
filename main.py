import webapp2
import os
import jinja2
import data
from models import TinyU

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


# class MainPage(webapp2.RequestHandler):
#     def __init__(self, response, request):
#         self.tinyperson = tinyperson = data.newtinydata();
class MainPage((webapp2.RequestHandler)):
    def __init__(self, request, response):
#        self.tdict = {}
        self.initialize(request, response)
        self.tinyperson = data.newtinydata();



    def get(self):

#        self.response.headers['Content-Type'] = 'text/html'

        name = self.tinyperson.name
        age  = self.tinyperson.age
        race  = self.tinyperson.race
        social_class = self.tinyperson.social_class
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

        newAge, randschool, newGrade, uniqueDescription = data.ageUp(self.tinyperson)

        print randschool
        print newAge
        print uniqueDescription




app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
