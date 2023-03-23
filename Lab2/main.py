import webapp2
import os
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        path=os.path.join(os.path.dirname(__file__),'index.html')
        template_values = {}
        self.response.out.write(template.render(path,template_values))
    
    def post(self):
        name=self.request.get('name')
        age=self.request.get('age')
        gender=self.request.get('gender')
        email=self.request.get('email')
        mobile=self.request.get('mobile')
        address=self.request.get('address')
        


        values={
            'name' : name,
            'mobile' : mobile,
            'age' : age,
            'gender' : gender,
            'address' : address,
            'email' : email
        }
        path = os.path.join(os.path.dirname(__file__), 'result.html')
        self.response.out.write(template.render(path, values))

app =webapp2.WSGIApplication([('/',MainPage)],debug=True)