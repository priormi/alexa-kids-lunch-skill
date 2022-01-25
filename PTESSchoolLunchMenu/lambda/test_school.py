import pytest
import requests
import datetime
import school

SchoolId = "b4a627df-67b5-4b5c-8cc3-5685d6b4ce74"
day_offset = 0

@pytest.fixture
def menu_mock():
    return [
        {
            #"given_name" : "Alfonsa",
            "ENTREES" : "Turkey Pepperoni Stuffed Sandwich",
            "VEGETABLE SERVED" : "Carrots",
            "VEGTABLES" : "Corn",
            "VEGETABLES CHOICE BAR" : "Snap Peas",
            "FRUITS" : "Applesauce Cup",

        },
    ]


def test_get_entrees():
    assert school.get_entrees(SchoolId, day_offset, menu_mock) == [
        "Turkey Pepperoni Stuffed Sandwich",
        "Carrots",
        "Snap Peas",
        "Applesauce Cup",
    ] 