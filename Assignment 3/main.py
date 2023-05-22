import webapp2

class MainPage(webapp2.RequestHandler) :
    def get(self):
        self.response.headers["Content-Type"]="text/plain"
        cnt =0
        while cnt<=10:
            self.response.write("Seat No : T190058519\n")
            self.response.write("Department : IT\n")
            self.response.write("\n")
            cnt+=1

app = webapp2.WSGIApplication(
    [('/', MainPage)],debug=True
)
