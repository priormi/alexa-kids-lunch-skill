import requests
import json
import helpers

def get_all_food(day_offset):
    SchoolId = "b4a627df-67b5-4b5c-8cc3-5685d6b4ce74"
    entiremenu = ""
    allfoodarray = []
    day_of_week = helpers.get_day_of_week(day_offset)
    json_array = get_menu(SchoolId, day_offset)

    if day_of_week < 5:
        entree = get_entrees(SchoolId, day_offset, json_array)
        allfoodarray.append(entree)
        grains = get_grains(SchoolId, day_offset, json_array)
        if grains is not None:
            allfoodarray.append(grains)
        veggies = get_veggies_served(SchoolId, day_offset, json_array)
        if veggies is not None:
            allfoodarray.append(veggies)
        fruits = get_fruits(SchoolId, day_offset, json_array)
        if fruits is not None:
            allfoodarray.append(fruits)
        for item in allfoodarray:
            entiremenu = entiremenu+item
        speak_output = entiremenu.replace("&", "and")
    else:
        speak_output = "The day you asked about is the weekend.  There is no menu available."
    return speak_output




def get_menu(SchoolId, day_offset):
    todays_menu_items =[]
    date = helpers.get_date(day_offset)
    url = "https://webapis.schoolcafe.com/api/CalendarView/GetDailyMenuitems?SchoolId="+SchoolId+"&ServingDate="+date+"&ServingLine=A%20Line&MealType=Lunch"
    input_file = requests.get(url)
    json_array = json.loads(input_file.content)
    return(json_array)

def get_entrees(SchoolId, day_offset, json_array):
    #json_array = get_menu(SchoolId, day_offset)
    entrees_list = "Entrees include "
    for item in json_array['ENTREES']:
        entrees_list =  entrees_list+(item["MenuItemDescription"]) +" , "
    return entrees_list

def get_veggies_served(SchoolId, day_offset, json_array):
    #json_array = get_menu(SchoolId, day_offset)
    day_offset = day_offset
    if "VEGETABLE SERVED" in json_array:
        for item in json_array['VEGETABLE SERVED']:
            veggies_list = " your veggies are  "
            veggies_list =  veggies_list+(item["MenuItemDescription"]) +" , "
    elif "VEGETABLES" in json_array:
        for item in json_array['VEGETABLES']:
            veggies_list = " your veggies are  "
            veggies_list =  veggies_list+(item["MenuItemDescription"]) +" , "
        return veggies_list
    else:
        pass

def get_veggies_choice(SchoolId, day_offset, json_array):
    day_offset = day_offset
    #json_array = get_menu(SchoolId, day_offset)
    veggies_list = []
    for item in json_array['VEGETABLES CHOICE BAR']:
        veggies_list.append(item["MenuItemDescription"])

def get_fruits(SchoolId, day_offset, json_array):
    day_offset = day_offset
    #json_array = get_menu(SchoolId, day_offset)
    if "FRUITS" in json_array:
        for item in json_array['FRUITS']:
            fruits_list = " and your fruit choice is "
            fruits_list = fruits_list+(item["MenuItemDescription"]) +" , "
        return fruits_list
    else:
        pass

def get_grains(SchoolId, day_offset, json_array):
    day_offset = day_offset
    #json_array = get_menu(SchoolId, day_offset)
    if "GRAINS" in json_array:
        for item in json_array['GRAINS']:
            grains_list = " for grains you can eat  "
            grains_list = grains_list+(item["MenuItemDescription"]) +" , "
        return grains_list
    else:
        pass

def get_school_by_id(rando_number):
    school_list =[]
    url = "https://webapis.schoolcafe.com/api/GetSchoolsList?districtId=468"
    input_file = requests.get(url)
    json_array = json.loads(input_file.content)
    for item in json_array:
        school = School(item)
        school_list.append(item["SchoolId"])
    schoolid = school_list[rando_number]
    return(schoolid)
