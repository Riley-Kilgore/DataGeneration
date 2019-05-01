# The following script is to generate the json files
#   representing a plan with preferences and rating.
import os
import string
import json

#JSON generative code.
def write_file(filename, data):
    with open(filename + '.json', 'a+') as file:
        json.dump(data, file)

class Schedule:
    # Preferences
    string planName
    string major
    string school
    string timePref
    string summerPref
    string startQuarter
    string startMath
    string startEnglish
    string enrollType
    string jobType

    #Rank
    string scheduleGrade
    string gradeReason

    # Classes
    Quarter[] classes

class Quarter:
    string id
    int year
    string title
    Course[] courses

class Course:
    string id
    string title
    string description
