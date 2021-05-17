import re
import pdb
from bottle import post, request

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    quest = request.forms.get('QUEST')
    pattern=r"^[a-zA-Z0-9]{1,100}[@][a-z]{2,6}\.[a-z]{2,4}"
    number_re=re.compile(pattern)

    questions = {}

    if len(quest) == 0:
        return "Sorry, your quest incorrect!"
    elif number_re.findall(mail):
        questions[mail] = quest
        pdb.set_trace()
        return "Thanks! The answer will be sent to the mail %s" % mail
    else:
        return "Sorry, your mail incorrect!"
    