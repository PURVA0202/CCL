import webapp2

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers["Content-Type"] = "text/plain"
        for i in range(5):
            self.response.write("Name : Purva Bapecha\n")
            self.response.write("Seat No: T190058519\n")
            self.response.write("Department: Information Technology\n")
            self.response.write("\n")

app = webapp2.WSGIApplication(
        [("/",MainPage)],
        debug=True
)