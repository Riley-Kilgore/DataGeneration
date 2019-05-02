import jsonScript
import os
import string
import json

ID = 0

def nextID(id):
    tempid = id
    id = id + 1
    return tempid

def generateClass():
    c = jsonScript.Course()
    c.id = 0 #input("Class ID?\n")
    c.title = input("Which class?\n")
    c.desc = "A class."

def generateQuarter():
    q = jsonScript.Quarter()
    q.id = nextID(ID)
    q.year = input("Year?\n")
    q.title = input("Which Quarter?\n")
    q.courses = []
    while(True):
        q.courses.append(generateClass())
        if(input("Is the quarter complete? (yes/no)\n") == "yes"):
            break
    return q

def generateCourses(schedule):
    schedule.classes = []
    while (True):
        schedule.classes.append(generateQuarter())
        if(input("Is the schedule complete? (yes/no)\n") == "yes"):
            break

schedule = jsonScript.Schedule()
schedule.planName = input("Plan Name?\n")
schedule.major = input("Major?\n")
schedule.school = input("School?\n")
schedule.timePref = input("Time Preference?\n")
schedule.summerPref = input("Summer? yes/no\n")
schedule.startQuarter = input("Starting Quarter?\n") # (No Year)\n")
schedule.startMath = input("Starting Math?\n")
schedule.startEnglish = input("Starting English?\n")
schedule.enrollType = input("Enrollment (Full/Part) Time?\n")
schedule.jobType = input("Job Type (Full/Part/No)\n")
generateCourses(schedule)
schedule.scheduleGrade = input("Schedule Grade 1-5\n")
schedule.gradeReason = input("Why this grade?\n")

jsonScript.write_file('./test', schedule)
