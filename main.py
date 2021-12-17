import requests
import datetime
import json
from school import *

school_list = []
school_id = "b4a627df-67b5-4b5c-8cc3-5685d6b4ce74"

def find_school():
    school_list.extend(s1.get_school_list())
    sl = s1.display_schools(school_list)

s1 = School
def get_all_the_food():
    day_of_week = helpers.get_day_of_week()
    if day_of_week < 5: 
        s1.get_entrees(school_id)
        s1.get_veggies_served(school_id)
        s1.get_veggies_choice(school_id)
        s1.get_fruits(school_id)
    else:
        print("Today is the weekend.  No menu available")

get_all_the_food()