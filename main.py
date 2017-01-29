
import webapp2
import cgi
import re
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")

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
        text-color: red;
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

class Index(webapp2.RequestHandler):
    def get(self):

        submit_form = """
            <form action="/submit" method="post">
                <label>
                    Username
                    <input type="text" name="username"/>
                </label> <br>
                <label>
                    Password
                    <input type="text" name="password"/>
                </label> <br>
                <label>
                    Verify password
                    <input type="text" name="verify"/>
                </label> <br>
                <label>
                    Email(optional)
                <input type="text" name="email"/>
                </label> <br>
                <input type="submit" value="Submit"/>
            </form>
                """



        self.response.write(page_header + submit_form + page_footer)

class SubmitButton(webapp2.RequestHandler):
    def post(self):
        username = self.request.get("username")
        username_escaped = cgi.escape(username)
        password = self.request.get("password")
        password_escaped = cgi.escape(password)
        verify = self.request.get("verify")
        verify_escaped = cgi.escape(verify)
        email = self.request.get("email")
        email_escaped = cgi.escape(email)

        username_error = "That's not a valid username"
        password_error = "That's not a valid password"
        password_match_error = "Your passwords didn't match"

        confirmation = "Welcome" + username_escaped

        def valid_username(username):
            return USER_RE.match(username)

        if valid_username(username_escaped) == False:
            self.response.write(page_header + submit_form + username_error + page_footer)

        if valid_username(username_escaped) == True:
            self.response.write(page_header + "<h2>" + confirmation + "</h2>" + page_footer)







app = webapp2.WSGIApplication([
    ('/', Index),
    ('/submit', SubmitButton)
], debug=True)
