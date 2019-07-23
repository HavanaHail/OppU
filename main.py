import webapp2
import os
import jinja2
from data import newtinydata

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
        file = models.TinyU.query(models.TinyU).get()
        print file
#        self.response.headers['Content-Type'] = 'text/plain'



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/newuser', newUser),
], debug=True)
