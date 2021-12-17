from school import *
from helpers import *

def test_school_name():
    s = School
    current_school = s.get_school_list()[0]
    assert(current_school.SchoolName == "ANKENY HIGH SCHOOL")

