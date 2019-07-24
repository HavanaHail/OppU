import webapp2
import os
import jinja2
from data import newtinydata
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
        newtinydata()
#        template = jinja_env.get_template('/templates/index.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write("HI")
        file = TinyU.query().get()
        self.response(file)

#        self.response.headers['Content-Type'] = 'text/plain'



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/newuser', newUser),
], debug=True)
