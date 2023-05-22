import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"]="text/plain"
        cnt=0
        a=0
        b=1
        self.response.write(a)
        self.response.write("\n")
        self.response.write(b)
        self.response.write("\n")
        while cnt<6:
            c=a+b
            self.response.write(c)
            self.response.write("\n")
            a=b
            b=c
            cnt+=1

app = webapp2.WSGIApplication(
    [("/",MainPage)],debug=True
)
