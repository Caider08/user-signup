
import webapp2
import cgi
import re


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
            <input type="text" name="username" value="%(username_escaped)s"/>
        </label> <span style="color: red">%(usererror)s</span> <br>
        <label>
            Password
            <input type="password" name="password"/>
        </label> <span style="color: red">%(passworderror)s</span> <br>
        <label>
            Verify password
            <input type="password" name="verify"/>
        </label> <span style="color: red">%(verifyerror)s</span> <br>
        <label>
            Email(optional)
            <input type="text" name="email" value="%(email_escaped)s"/>
        </label> <span style="color: red">%(emailerror)s<br>
            <input type="submit" value="Submit"/>
        </form>
            """


class Index(webapp2.RequestHandler):
    def writeForm(self, ue="", pe="", ve="", ee="",uescaped="",escaped=""):
        edict = {"usererror":ue, "passworderror":pe, "verifyerror":ve, "emailerror":ee, "username_escaped":uescaped, "email_escaped":escaped}
        self.response.write(page_header + (submit_form % edict) + page_footer)

    def get(self):
        self.writeForm()

    def post(self):
        username = self.request.get("username")
        username_escaped = cgi.escape(username)
        password = self.request.get("password")
        password_escaped = cgi.escape(password)
        verify = self.request.get("verify")
        verify_escaped = cgi.escape(verify)
        email = self.request.get("email")
        email_escaped = cgi.escape(email)

        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        def valid_username(usernameInput):
            if USER_RE.match(usernameInput):
                return True
            else:
                return False

        USER_pass = re.compile(r"^.{3,20}$")
        def valid_password(passwordInput):
            if USER_pass.match(passwordInput):
                return True
            else:
                return False

        USER_email = re.compile(r"^[\S]+@[\S]+.[\S]+$")
        def invalid_email(emailInput):
            if USER_email.match(emailInput):
                return True
            else:
                return False

        ue = ""
        pe= ""
        ve= ""
        ee= ""
        uescaped = username_escaped
        escaped = email_escaped

        if username == "" or valid_username(username) == False:
            ue += "That isn't a valid username"

        if password == "" or valid_password(password) == False:
            pe += "That isn't a valid password"

        if password != verify:
            ve += "Your passwords don't match"

        if invalid_email(email) == False:
            ee += "That isn't a valid email"

        if invalid_email(email) == True and valid_username(username) == True and valid_password(password) == True and password == verify:
            #self.redirect("/welcome" + confirmation)
            self.redirect("/welcome?username=" + username_escaped)

        self.writeForm(ue,pe,ve,ee,uescaped,escaped)


class Welcome(webapp2.RequestHandler):

    def get(self):
        username = self.request.get('username')

        self.response.write("<h2>  Welcome <h2>" + username)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/welcome', Welcome),
], debug=True)
