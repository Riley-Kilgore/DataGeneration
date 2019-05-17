from tkinter import *
from tkinter import messagebox
from optparse import OptionParser
import schedule
import sys
import os
import json

authors = ['Matt Johnson', 'Will Thomas', 'Riley Kilgore']
version = 'v2.0'

def main():
    options = parse_options()
    if options.info:
        print('author(s): ')
        for author in authors:
            print('\t' + author)
        print('version: ' + version)
        sys.exit()
    root = Tk()
    root.title('schedule generator')
    root.geometry('540x500')
    create_schedule(root)

def external_schedule_creation(file_name, schdl):
    options = parse_options()
    if options.info:
        print('version: ' + version)
        sys.exit()
    write_json(file_name, schdl.get_data)

def parse_options():
    parser = OptionParser()
    parser.add_option('-i', '--info', action='store_true', dest='info', default=False, help='show script info and quit')
    options, _args = parser.parse_args()
    return options

schdl = None
q = None

#Create Schedule, formatting for schedule creation. Creates display with boxes and labels to allow
#Users to enter their information. "add quarter" button allows the user to add a quarter. Can be done
#multiple times.
def create_schedule(root):
    global schdl
    global pref
    heading = Label(root, text="schedule creation", font=("arial", 20, "bold"), fg="steelblue")
    heading.grid(column=0, row=0)
    schdl = schedule.Schedule()
    pref = schedule.Preferences()
    pref.courses = StringVar()
    pref.credits = StringVar()
    pref.english = StringVar()
    pref.enrollment = StringVar()
    pref.evening = StringVar()
    pref.job = StringVar()
    pref.major = StringVar()
    pref.math = StringVar()
    pref.quarter = StringVar()
    pref.quarters = StringVar()
    pref.school = StringVar()
    pref.summer = StringVar()
    schdl.id = StringVar()
    schdl.date_created = StringVar()
    schdl.date_modified = StringVar()
    schdl.academic_year = StringVar()
    schdl.student_id = StringVar()
    schdl.metadata = StringVar()
    entry_courses = Entry(root, textvariable= pref.courses, width=25, bg="lightgrey")
    entry_credits = Entry(root, textvariable= pref.credits, width=25, bg="lightgrey")
    entry_english = Entry(root, textvariable= pref.english, width=25, bg="lightgrey")
    entry_enrollment = Entry(root, textvariable= pref.enrollment, width=25, bg="lightgrey")
    entry_evening = Entry(root, textvariable= pref.evening, width=25, bg="lightgrey")
    entry_job = Entry(root, textvariable= pref.job, width=25, bg="lightgrey")
    entry_major = Entry(root, textvariable= pref.major, width=25, bg="lightgrey")
    entry_math = Entry(root, textvariable= pref.math, width=25, bg="lightgrey")
    entry_quarter = Entry(root, textvariable= pref.quarter, width=25, bg="lightgrey")
    entry_quarters = Entry(root, textvariable= pref.quarters, width=25, bg="lightgrey")
    entry_school = Entry(root, textvariable= pref.school, width=25, bg="lightgrey")
    entry_summer = Entry(root, textvariable= pref.summer, width=25, bg="lightgrey")
    entry_id = Entry(root, textvariable= schdl.id, width=25, bg="lightgrey")
    entry_dcreated = Entry(root, textvariable= schdl.date_created, width=25, bg="lightgrey")
    entry_dmod = Entry(root, textvariable= schdl.date_modified, width=25, bg="lightgrey")
    entry_ayear = Entry(root, textvariable= schdl.academic_year, width=25, bg="lightgrey")
    entry_sid = Entry(root, textvariable= schdl.student_id, width=25, bg="lightgrey")
    # TODO: Metadata needs to have a separate json entry. (Like quarters/courses)
    entry_meta = Entry(root, textvariable=schdl.metadata, width=25, bg="lightgrey")
    add_qtr = Button(root, text="add quarter", width=10, height=1, bg="cyan", command=create_quarter)
    done_button = Button(root, text="save", width=10, height=1, bg="cyan", command=save_schedule)
    # TODO: What the fuck is courses?
    Label(root, text="Courses..?").grid(row=1, column=0)
    entry_courses. grid(row=1, column=1)
    Label(root, text="Credits").grid(row=2, column=0)
    entry_credits.grid(row=2, column=1)
    Label(root, text="English").grid(row=3, column=0)
    entry_english.grid(row=3, column=1)
    Label(root, text="Enrollment").grid(row=4, column=0)
    entry_enrollment.grid(row=4, column=1)
    Label(root, text="Evening").grid(row=5, column=0)
    entry_evening.grid(row=5, column=1)
    Label(root, text="Job Type").grid(row=6, column=0)
    entry_job.grid(row=6, column=1)
    Label(root, text="Major").grid(row=7, column=0)
    entry_major.grid(row=7,column=1)
    Label(root, text="Starting Math").grid(row=8, column=0)
    entry_math.grid(row=8, column=1)
    Label(root, text="Starting Quarter").grid(row=9, column=0)
    entry_quarter.grid(row=9, column=1)
    Label(root, text="Quarters Left").grid(row=10, column=0)
    entry_quarters.grid(row=10, column=1)
    Label(root, text="School").grid(row=11, column=0)
    entry_school.grid(row=11, column=1)
    Label(root, text="Summer Preference").grid(row=12, column=0)
    entry_summer.grid(row=12, column=1)
    Label(root, text="Plan ID").grid(row=13, column=0)
    entry_id.grid(row=13, column=1)
    Label(root, text="Date Created").grid(row=14, column=0)
    entry_dcreated.grid(row=14, column=1)
    Label(root, text="Date Modified").grid(row=15, column=0)
    entry_dmod.grid(row=15, column=1)
    Label(root, text="Academic Year").grid(row=16, column=0)
    entry_ayear.grid(row=16, column=1)
    Label(root, text="Student ID").grid(row=17, column=0)
    entry_sid.grid(row=17, column=1)
    Label(root, text="MetaData").grid(row=18, column=0)
    entry_meta.grid(row=18, column=1)
    add_qtr.grid(row=19, column=3)
    done_button.grid(row=20,column=3)
    root.mainloop()

def create_quarter():
    global schdl
    global q
    q = schedule.Quarter()
    createQtr = Tk()
    createQtr.title("add quarter")
    createQtr.geometry("500x500+0+0")
    q.id = StringVar()
    q.title = StringVar()
    q.year = StringVar()
    entry_id = Entry(createQtr, textvariable=q.id, width=25, bg="lightgrey")
    entry_title = Entry(createQtr,textvariable=q.title,width=25, bg="lightgrey")
    entry_year = Entry(createQtr, textvariable=q.year,width=25, bg="lightgrey")
    entry_id.grid(row=1, column=1)
    Label(createQtr, text="Quarter ID").grid(row=1, column=0)
    entry_title.grid(row=2, column=1)
    Label(createQtr, text="Quarter Title").grid(row=2, column=0)
    entry_year.grid(row=3, column=1)
    Label(createQtr, text="Quarter Year").grid(row=3, column=0)
    qtrCreation = Button(createQtr, text="add classes", width=10, height=1, bg="cyan", command=create_course)
    done_button = Button(createQtr, text="done", width=10, height=1, bg="cyan", command=lambda:[schdl.add_quarter(q), createQtr.destroy()])
    qtrCreation.grid(row=4,column=3)
    done_button.grid(row=5, column=3)
    createQtr.mainloop()

def create_course():
    global q
    course = schedule.Course()
    createCourse = Tk()
    createCourse.title("add course")
    createCourse.geometry("500x500+0+0")
    course.id = StringVar()
    course.title = StringVar()
    course.description = StringVar()
    entry_id = Entry(createCourse, textvariable=course.id, width=25, bg="lightgrey")
    entry_title = Entry(createCourse, textvariable=course.title, width=25, bg="lightgrey")
    entry_desc = Entry(createCourse, textvariable=course.description, width=25, bg="lightgrey")
    entry_id.grid(row=1, column=1)
    Label(createCourse, text="Plan Name").grid(row=1, column=0)
    entry_title.grid(row=2, column=1)
    Label(createCourse, text="Course Title").grid(row=2, column=0)
    entry_desc.grid(row=3, column=1)
    Label(createCourse, text="Description").grid(row=3, column=0)
    done_button = Button(createCourse, text="Done", width=10, height=1, bg="cyan", command=lambda:[q.add_course(course), createCourse.destroy()])
    done_button.grid(row=4, column=3)
    createCourse.mainloop()

def save_schedule():
    global schdl
    global pref
    write_json(schdl.id.get() + '_schedule', dump_schedule_stringvars().get_data())
    write_json(schdl.id.get() + '_pref', dump_pref_stringvars().get_data())
    save_notification()

def dump_pref_stringvars():
    '''
        self.__courses = '' # TODO, I don't know if this is right.
        self.__credits = '' # Current credits
        self.__english = '' # English starting
        self.__enrollment = '' # Enrollment Type
        self.__evening = '' # Will you take evening classes?
        self.__job = '' # Are you working full time? Part Time? No
        self.__major = '' # Major to transfer into.
        self.__math = '' # Most advanced math
        self.__quarter = '' # Current Quarter
        self.__quarters = '' # How many quarters before transfer.
        self.__school = '' # What school to transfer to.
        self.__summer = '' # Summer classes?
    '''
    finalP = schedule.Preferences()
    finalP.courses = pref.courses.get()
    finalP.credits = pref.credits.get()
    finalP.english = pref.english.get()
    finalP.enrollment = pref.enrollment.get()
    finalP.evening = pref.evening.get()
    finalP.job = pref.job.get()
    finalP.major = pref.major.get()
    finalP.math = pref.math.get()
    finalP.quarter = pref.quarter.get()
    finalP.quarters = pref.quarters.get()
    finalP.school = pref.school.get()
    finalP.summer = pref.summer.get()
    return finalP

def dump_schedule_stringvars():
    '''
        self.__id = ''
        self.__date_created = ''
        self.__date_modified = ''
        self.__academic_year = ''
        self.__student_id = ''
        self.__metadata = ''
        self.__quarters = []
    '''
    finalS = schedule.Schedule()
    finalS.id = schdl.id.get()
    finalS.date_created = schdl.date_created.get()
    finalS.date_modified = schdl.date_modified.get()
    finalS.academic_year = schdl.academic_year.get()
    finalS.metadata = schdl.metadata.get()
    for quarter in range(0, len(schdl.quarters)):
        new_q = schedule.Quarter()
        new_q.id = schdl.quarters[quarter].id.get()
        new_q.title = schdl.quarters[quarter].title.get()
        new_q.year = schdl.quarters[quarter].year.get()
        for course in range(0, len(schdl.quarters[quarter].courses)):
            new_c = schedule.Course()
            new_c.id = schdl.quarters[quarter].courses[course].id.get()
            new_c.title = schdl.quarters[quarter].courses[course].title.get()
            new_c.description = schdl.quarters[quarter].courses[course].description.get()
            new_q.add_course(new_c)
        finalS.add_quarter(new_q)
    return finalS

def save_notification():
    global schdl
    messagebox.showinfo('schedule saved', 'schedule json saved to:\n')


def write_json(filename, data):
    with open(filename + '.json', 'w+') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    main()
