#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re

header = "<h1>User Signup</h1>"
form = """
         <form method='post'>
               <label>Username:
               <input type='text' name='username'>
               </label>
<br></br>
               <label>Passcode:
               <input type='text' name='passcode'>
               </label>
<br></br>
               <label>Verify:
               <input type='text' name='verify'>
               </label>
<br></br>
               <label>Email(optional):
               <input type='text' name='email'>
               </label>
<br></br>
               <input type='submit'>
        </form>"""
content = header + form
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(content)

    def post(self):
        def valid_login(username, passcode, verify, email):
                if valid_username(username):
                        valid = True
                else:
                        self.redirect('/signup')
                if valid_passcode(passcode):
                        valid = True
                else:
                        self.redirect('/signup')
                if passwords_match(passcode, verify):
                        valid = True
                else:
                        self.redirect('/signup')
                                        
                return valid

        def passwords_match(passcode, verify):
                if passcode == verify:
                        return True
        
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        def valid_username(username):
            return username and USER_RE.match(username)

        PASS_RE = re.compile(r"^.{3,20}$")
        def valid_passcode(passcode):
            return password and PASS_RE.match(password)

        EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
        def valid_email(email):
            return not email or EMAIL_RE.match(email)
        username = self.request.get('username')
        passcode = self.request.get('passcode')
        verify   = self.request.get('verify')
        email    = self.request.get('email')
        valid_login(username, passcode, verify, email)
        
                                  
class signup(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("<h1>User Signup</h1>" + "<h2>Please Signup</h2>" + form)

class Welcome(webapp2.RequestHandler):      
    def get(self):   
            self.response.out.write("<h1>Welcome, " + username + "</h1>")
        else:
            self.redirect('/signup')

app = webapp2.WSGIApplication([
    ('/', MainHandler),('/signup', signup),('/welcome', Welcome)
], debug=True)
