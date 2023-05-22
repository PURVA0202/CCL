import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"]="text/plain"
        for i in range(1,11):
            self.response.write("\n")
            self.response.write("5 x ")
            self.response.write(i)
            self.response.write("=")
            self.response.write(5*i)
            self.response.write("\n")

app  = webapp2.WSGIApplication(
    [("/",MainPage)],debug = True
)
