import requests
import json
import helpers



class School:
    def __init__(self, school):
        self.SchoolId = school["SchoolId"]
        self.SchoolName = school["SchoolName"]
        #print(school)

    def get_menu(SchoolId):
        todays_menu_items =[]
        date = helpers.get_date()
        url = "https://webapis.schoolcafe.com/api/CalendarView/GetDailyMenuitems?SchoolId="+SchoolId+"&ServingDate="+date+"&ServingLine=A%20Line&MealType=Lunch"
        input_file = requests.get(url)
        json_array = json.loads(input_file.content)
        return(json_array)

    def get_entrees(SchoolId):
        json_array = School.get_menu(SchoolId)
        entrees_list = []
        for item in json_array['ENTREES']:
            entrees_list.append(item["MenuItemDescription"])
        for i in entrees_list:
            print("ENTREES: "+i)

    def get_veggies_served(SchoolId):
        json_array = School.get_menu(SchoolId)
        veggies_list = []
        for item in json_array['VEGETABLE SERVED']:
            veggies_list.append(item["MenuItemDescription"])
        for i in veggies_list:
            print("VEGETABLE SERVED: "+i)

    def get_veggies_choice(SchoolId):
        json_array = School.get_menu(SchoolId)
        veggies_list = []
        for item in json_array['VEGETABLES CHOICE BAR']:
            veggies_list.append(item["MenuItemDescription"])
        for i in veggies_list:
            print("VEGETABLES CHOICE BAR: "+i)    

    def get_fruits(SchoolId):
        json_array = School.get_menu(SchoolId)
        veggies_list = []
        for item in json_array['FRUITS']:
            veggies_list.append(item["MenuItemDescription"])
        for i in veggies_list:
            print("FRUITS: "+i) 

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
