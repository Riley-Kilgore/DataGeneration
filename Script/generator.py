from tkinter import *
from tkinter import messagebox
from optparse import OptionParser
import schedule
import sys
import os
import json

authors = ['Matt Johnson', 'Will Thomas', 'Riley Kilgore']
version = 'v1.0'

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
    root.geometry('575x500')
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
    heading = Label(root, text="schedule creation", font=("arial", 20, "bold"), fg="steelblue")
    heading.grid(column=0, row=0)
    schdl = schedule.Schedule()
    schdl.plan_name = StringVar()
    schdl.major = StringVar()
    schdl.school = StringVar()
    schdl.time_pref = StringVar()
    schdl.summer_pref = StringVar()
    schdl.start_quarter = StringVar()
    schdl.start_math = StringVar()
    schdl.start_english = StringVar()
    schdl.enroll_type = StringVar()
    schdl.job_type = StringVar()
    schdl.schedule_grade = StringVar()
    schdl.grade_reason = StringVar()
    entry_planName = Entry(root, textvariable= schdl.plan_name, width=25, bg="lightgrey")
    entry_major = Entry(root, textvariable=schdl.major, width=25, bg="lightgrey")
    entry_school = Entry(root, textvariable=schdl.school, width=25, bg="lightgrey")
    entry_tpref = Entry(root, textvariable=schdl.time_pref, width=25, bg="lightgrey")
    entry_spref = Entry(root, textvariable=schdl.summer_pref, width=25, bg="lightgrey")
    entry_sqtr = Entry(root, textvariable= schdl.start_quarter, width=25, bg="lightgrey")
    entry_smath = Entry(root, textvariable=schdl.start_math, width=25, bg="lightgrey")
    entry_senglish = Entry(root, textvariable=schdl.start_english, width=25, bg="lightgrey")
    entry_jtype = Entry(root, textvariable=schdl.job_type, width=25, bg="lightgrey")
    entry_etype = Entry(root, textvariable=schdl.enroll_type, width=25, bg="lightgrey")
    entry_sgrade = Entry(root, textvariable=schdl.schedule_grade, width=25, bg="lightgrey")
    entry_greason = Entry(root, textvariable=schdl.grade_reason, width=25, bg="lightgrey")
    add_qtr = Button(root, text="add quarter", width=10, height=1, bg="cyan", command=create_quarter)
    done_button = Button(root, text="save", width=10, height=1, bg="cyan", command=save_schedule)
    Label(root, text="Plan Name").grid(row=1, column=0)
    entry_planName.grid(row=1, column=1)
    Label(root, text="Major").grid(row=2, column=0)
    entry_major.grid(row=2, column=1)
    Label(root, text="School").grid(row=3, column=0)
    entry_school.grid(row=3, column=1)
    Label(root, text="Time Preference").grid(row=4, column=0)
    entry_tpref.grid(row=4, column=1)
    Label(root, text="Summer Preference").grid(row=5, column=0)
    entry_spref.grid(row=5, column=1)
    Label(root, text="Start Quarter").grid(row=6, column=0)
    entry_sqtr.grid(row=6, column=1)
    Label(root, text="Start Math").grid(row=7, column=0)
    entry_smath.grid(row=7,column=1)
    Label(root, text="Start English").grid(row=8, column=0)
    entry_senglish.grid(row=8, column=1)
    Label(root, text="Enrollment Type").grid(row=9, column=0)
    entry_etype.grid(row=9, column=1)
    Label(root, text="Job Type").grid(row=10, column=0)
    entry_jtype.grid(row=10, column=1)
    Label(root, text="Schedule Grade").grid(row=11, column=0)
    entry_sgrade.grid(row=11, column=1)
    Label(root, text="Grade Reason").grid(row=12, column=0)
    entry_greason.grid(row=12, column=1)
    add_qtr.grid(row=13, column=3)
    done_button.grid(row=14,column=3)
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
    write_json(schdl.plan_name.get(), dump_stringvars().get_data())
    save_notification()

def dump_stringvars():
    final = schedule.Schedule()
    final.plan_name = schdl.plan_name.get()
    final.major = schdl.major.get()
    final.school = schdl.school.get()
    final.time_pref = schdl.time_pref.get()
    final.summer_pref = schdl.summer_pref.get()
    final.start_quarter = schdl.start_quarter.get()
    final.start_math = schdl.start_math.get()
    final.start_english = schdl.start_english.get()
    final.enroll_type = schdl.enroll_type.get()
    final.job_type = schdl.job_type.get()
    final.schedule_grade = schdl.schedule_grade.get()
    final.grade_reason = schdl.grade_reason.get()
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
            new_q.add_course(course)
        final.add_quarter(quarter)
    return final

def save_notification():
    global schdl
    messagebox.showinfo('schedule saved', 'schedule json saved to:\n')


def write_json(filename, data):
    with open(filename + '.json', 'w+') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    main()
