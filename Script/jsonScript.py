# The following script is to generate the json files
#   representing a plan with preferences and rating.
import os
import string
import json

#JSON generative code.
def write_file(filename, data):
    with open(filename + '.json', 'a+') as file:
        json.dump(data, file)

def course_data(courses):
    data = {}
    for c in courses:
        data[c.title] = c.get_data()
    return data

class Schedule:

    def get_data(self):
        quarter_array = self.classes.get_data()
        return {
            'plan_name' : self.planName,
            'Major' : self.major,
            'School' : self.school,
            'Time Preference' : self.timePref,
            'Summer Preference' : self.summerPref,
            'Starting Quarter' : self.startQuarter,
            'Starting Math' : self.startMath,
            'Starting English' : self.startEnglish,
            'Enrollment Type' : self.enrollType,
            'Job Type' : self.jobType,

            #Rank
            'Schedule Grade' : self.scheduleGrade,
            'Grade Reason' : self.gradeReason,

            # Classes
            'Classes' : quarter_array
        }
    
    # Preferences
    planName = ''
    major = ''
    school = ''
    timePref = ''
    summerPref = ''
    startQuarter = ''
    startMath = ''
    startEnglish = ''
    enrollType = ''
    jobType = ''

    #Rank
    scheduleGrade = ''
    gradeReason = ''
    
    # Classes
    classes = ''

    def __init__(self):
        pass

class Quarter:

    def get_data(self):
        course_array = courses_data(courses)
        return {
            'id' : self.id,
            'Year' : self.year,
            'Title' : self.title,
            'Courses' : courses_array
        }

    id = ''
    year = ''
    title = ''
    courses = []

    def __init__(self):
        pass

class Course:

    def get_data(self):
        return {
            'id' : self.id,
            'Title' : self.title,
            'Description' : self.description
        }
    
    id = ''
    title = ''
    description = ''

    def __init__(self):
        pass
