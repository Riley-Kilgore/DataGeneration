#import jsonScript.py
import os
import string
import json

int id = 0

schedule = new Schedule()
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

def generateCourses(schedule):
    schedule.classes = []
    while (true):
        schedule.classes.append(generateQuarter())
        if(input("Is the schedule complete? (yes/no)\n") == "yes"):
            break

def generateQuarter():
    q = Quarter()
    q.id = nextID()
    q.year = input("Year?\n")
    q.title = input("Which Quarter?\n")
    q.courses = []
    while(true):
        q.append(generateClass())
        if(input("Is the quarter complete? (yes/no)\n") == "yes"):
            break
    return q

def generateClass():
    c = Course()
    c.id = 0 #input("Class ID?\n")
    c.title = input("Which class?\n")
    c.desc = "A class."

def nextID():
    tempid = id
    id = id + 1
    return tempid

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
