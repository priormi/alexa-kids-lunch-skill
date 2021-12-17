import requests
import datetime
import json
from school import *

school_list = []

def find_school():
    school_list.extend(s1.get_school_list())
    sl = s1.display_schools(school_list)

s1 = School
#find_school()
def get_all_the_food():
    day_of_week = helpers.get_day_of_week()
    if day_of_week < 5: 
        s1.get_entrees("b4a627df-67b5-4b5c-8cc3-5685d6b4ce74")
        s1.get_veggies_served("b4a627df-67b5-4b5c-8cc3-5685d6b4ce74")
        s1.get_veggies_choice("b4a627df-67b5-4b5c-8cc3-5685d6b4ce74")
        s1.get_fruits("b4a627df-67b5-4b5c-8cc3-5685d6b4ce74")
    else:
        print("Today is the weekend.  No menu available")

get_all_the_food()
#users_input = input("Enter name of school: ")
#for s in school_list:
#    if (s.SchoolName == users_input):
#        print("School selcted: " + s.SchoolId + " -- " +s.SchoolName)
#        menu_items = s1.get_menu(s.SchoolId)




    def get_school_list():
        school_list =[]
        url = "https://webapis.schoolcafe.com/api/GetSchoolsList?districtId=468"
        input_file = requests.get(url)
        json_array = json.loads(input_file.content)
        for item in json_array:
            school = School(item)
            school_list.append(school)
        return(school_list)

    def display_schools(self):
        for obj in self:
            print(obj.SchoolName)

