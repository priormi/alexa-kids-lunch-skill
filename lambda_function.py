
from __future__ import print_function
import random
import datetime
import json
import requests


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
    

# --------------- Functions that control the skill's behavior -----------------
        
def get_entree_menu_response():
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Today's  menu items are " + get_todays_menu_items()
    reprompt_text = "I don't know if you heard me, welcome to your custom alexa application!"
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def get_todays_menu_items():
    todays_menu_items = ""
    date = get_date()
    url = "https://webapis.schoolcafe.com/api/CalendarView/GetDailyMenuitems?SchoolId=b4a627df-67b5-4b5c-8cc3-5685d6b4ce74&ServingDate="+date+"&ServingLine=A%20Line&MealType=Lunch"
    input_file = requests.get(url)
    json_array = json.loads(input_file.content)
    for item in json_array['ENTREES']:
        todays_menu_items =  todays_menu_items+(item["MenuItemDescription"]) +" , "
    return todays_menu_items

def get_date():
    month = datetime.datetime.now().strftime("%m")
    day = datetime.datetime.now().strftime("%d")
    year = datetime.datetime.now().strftime("%Y")
    date = month +"%2f"+day+"%2f"+year
    return date

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Alexa Skills Kit sample. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts.
        One possible use of this function is to initialize specific 
        variables from a previous state stored in an external database
    """
    # Add additional code here as needed
    pass

    

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    # Dispatch to your skill's launch message
    return get_entree_menu_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "lunch":
        return get_entree_menu_response()
    elif intent_name == "AMAZON.HelpIntent":
        return get_entree_menu_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])


# --------------- Main handler ------------------

def lambda_handler(event, context):
    print("Incoming request...")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
print(get_entree_menu_response())
