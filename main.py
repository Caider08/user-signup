
import webapp2
import cgi
import re
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
USER_pass = re.compile(r"^.{3,20}$")


# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User-Signup</title>
    <style type="text/css">
    form {
        text-align: left;

    }

    input {

    }

    .errorm {
        color: red;
    }
    </style>
</head>
<body>
    <h1>
        <h1> Sign-Up </h1>
    </h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""
submit_form = """
    <form method="post">
        <label>
            Username
            <input type="text" name="username"/>
        </label> <span style="color: red">%(error)s</span> <br>
        <label>
            Password
            <input type="text" name="password"/>
        </label> <span name="span 2" value="username_error"> </span> <br>
        <label>
            Verify password
            <input type="text" name="verify"/>
        </label> <span> + verify_error + </span> <br>
        <label>
            Email(optional)
            <input type="text" name="email"/>
        </label> <br>
            <input type="submit" value="Submit"/>
        </form>
            """


class Index(webapp2.RequestHandler):
    def writeForm(self, error=""):
        self.response.out.write(submit_form % {"error": error})

    def get(self):
        self.response.write(page_header + submit_form + page_footer)

    def post(self):
        username = self.request.get("username")
        username_escaped = cgi.escape(username)
        password = self.request.get("password")
        password_escaped = cgi.escape(password)
        verify = self.request.get("verify")
        verify_escaped = cgi.escape(verify)
        email = self.request.get("email")
        email_escaped = cgi.escape(email)



        def valid_username(username):
            return USER_RE.match(username)

        def valid_password(password):
            return USER_pass.match(password)

        if username == "":
            nameerror = "bad"
            self.writeForm("bad")


        #if valid_username(username_escaped) == False:
            #self.response.write(page_header + submit_form + username_error + page_footer)
        #else:
            #self.response.write("<h1>Success</h1>")

        #if valid_username(username_escaped) == True:
            #self.redirect("/welcome" + confirmation)

        #self.redirect("/welcome?username=" + username_escaped)

        #self.response.write(page_header + submit_form + "<p>" + "hello" + "</p>" + page_footer)


class Welcome(webapp2.RequestHandler):

    def get(self):
        username = self.request.get('username')

        self.response.write("<h2>  Welcome <h2>" + username)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/welcome', Welcome),
], debug=True)
