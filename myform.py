import re
import pdb
import json
from bottle import post, request

questions = {}

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    quest = request.forms.get('QUEST')
    pattern=r"^[a-zA-Z0-9]{1,100}[@][a-z]{2,6}\.[a-z]{2,4}"
    number_re=re.compile(pattern)

    if len(quest) == 0:
        return "Sorry, your quest incorrect!"
    elif number_re.findall(mail):
        questions[mail] = quest

        if (mail in questions):
            questions[mail] = quest
        with open('data.txt', 'w') as outfile:
            json.dump(questions, outfile)

        return "Thanks! The answer will be sent to the mail %s" % mail
    else:
        return "Sorry, your mail incorrect!"
    