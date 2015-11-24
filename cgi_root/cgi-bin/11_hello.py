#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()
user_name = form.getvalue('name', 'Anonymous')
template_values = {'user_name': user_name}
print "Content-Type: text/html"
print
print """\
<html>
    <body>
        <h2>Hello {user_name}!</h2>
        <form method="post">
            What is your name?
            <input type="text" name="name"/>
            <input type="submit"/>
        </form>
    </body>
</html>
""".format(**template_values)
