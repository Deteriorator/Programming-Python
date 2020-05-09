#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    peoplecgi.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.08   9:23
-------------------------------------------------------------------------------
   @Change:   2020.05.08
-------------------------------------------------------------------------------
"""

import cgi, shelve, sys, os

shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')

form = cgi.FieldStorage()
print('Content-type: text/html')
sys.path.insert(0, os.getcwd())

replyhtml = """
<html>
<title>People Input Form</title>
<body>
<form method=post action="peoplecgi.py">
<table>
<tr><th>key<td><input type=text name=key value="%(key)s">
$ROWS$
</table>
<p>
<input type="submit" value="Fetch" name=action>
<input type="submit" value="Update" name=action>
</form>
</body>
</html>

"""

rowhtml = '<tr><th>%s<td><input type=text name=%s value="%%(%s)s">\n'
rowshtml = ''

for fieldname in fieldnames:
    rowshtml += (rowhtml % ((fieldname, ) * 3))

replyhtml = replyhtml.replace('$ROWS$', rowshtml)

def htmlize(adict):
    new = adict.copy()
    for field in fieldnames:
        value = new[field]
        new[field] = cgi.escape(repr(value))
    return new


def fetch_record(db, form):
    try:
        key = form['key'].value
        record = db[key]
        fields = record.__dict__
        fields['key'] = key
    except:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing or invalid key!'
    return fields


def update_record(db, form):
    if 'key' not in form:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing key input!'
    else:
        key = form['key'].value
        if key in db:
            record = db[key]
        else:
            from person import Person
            record = Person(name='?', age='?')
        for field in fieldnames:
            setattr(record, field, eval(form[field].value))
        db[key] = record
        fields = record.__dict__
        fields['key'] = key
    return fields


db = shelve.open(shelvename)
action = form['action'].value if 'action' in form else None
if action == 'Fetch':
    fields = fetch_record(db, form)
elif action == 'Update':
    fields = update_record(db, form)
else:
    fields = dict.fromkeys(fieldnames, '?')
    fields['key'] = 'Missing or invalid action!'
db.close()
print(replyhtml % htmlize(fields))

