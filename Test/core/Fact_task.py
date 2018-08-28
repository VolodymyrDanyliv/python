import urllib2
import json

while True:
    URL = 'https://the-cat-fact.herokuapp.com/api/randomfact'
    status_code = 200

    answer = raw_input("Do you want to know something interesting?: ")
    if answer.lower() == 'yes':
        try:
            '''Get URL'''
            response = urllib2.urlopen(URL)
            '''Get Status Code'''
            actual_code = response.getcode()
            if actual_code == status_code:
                '''Get JSON Dictionary '''
                values_string = json.loads(response.read())
                '''Access to FACT value'''
                message = values_string.get('message')
                fact = values_string.get('data')[0].get('fact')
                print "You %s:  %s" % (message, fact)
            else:
                print "Recourse unavailable"
        except urllib2.HTTPError:
            choice = raw_input("Connection error occurred. Do you want to continue?: ")
            if choice.lower() == 'yes':
                print ""
            elif choice.lower() == 'no':
                exit(0)
            else:
                print "Please type Yes or No"
    elif answer.lower() == 'no':
        exit(0)
    else:
        print "Please type Yes or No"
