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
        self.response.headers['Content-Type'] = 'text/plain'
#        self.response.write('Hello, World!')
class newUser(webapp2.RequestHandler):
    def get(self):
        tinyperson = data.newtinydata()
#        template = jinja_env.get_template('/templates/index.html')
        self.response.headers['Content-Type'] = 'text/html'
#        self.response.write("HI")
        name = tinyperson.name
        age  = tinyperson.age
        race  = tinyperson.name
        social_class = tinyperson.social_class
        user_grade = data.getGrade(tinyperson.age)

        template_vars = {
        "Name": name,
        "Age": age,
        "race": race,
        "Social_Class": social_class,
        "Grade": user_grade
        }

        start_template=jinja_env.get_template("PageTwo.html")
        self.response.write(start_template.render(template_vars))




#        self.response.headers['Content-Type'] = 'text/plain'



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/newuser', newUser),
], debug=True)
