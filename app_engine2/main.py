import webapp2
import os
from google.appengine.ext.webapp import template



class IndexHandler(webapp2.RequestHandler):
    def get(self):
        template_params={}
        print(str(os.getenv('SERVER_SOFTWARE', '')))
        html = template.render("app/dist/index.html", template_params)
        self.response.out.write(html)


class Hello(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("hello")



config={}
routes=[
    (r'/', IndexHandler),
    (r'/hello', Hello),
]

app = webapp2.WSGIApplication(
    routes=routes, debug=True, config=config)
