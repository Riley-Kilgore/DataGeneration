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
    planName
    major
    school
    timePref
    summerPref
    startQuarter
    startMath
    startEnglish
    enrollType
    jobType

    #Rank
    scheduleGrade
    gradeReason

    # Classes
    classes

class Quarter:
    id
    year
    title
    courses

class Course:
    id
    title
    description
