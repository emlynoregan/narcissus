import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Yo Dawg, I hear you like old memes.')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)