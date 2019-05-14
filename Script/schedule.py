import sys
from optparse import OptionParser

author = 'Matt Johnson'
version = 'v1.0'

def main():
    print('\nATTENTION: this file is not meant to be run\n')
    options = parse_options()
    if options.info:
        print('author: ' + author)
        print('version: ' + version)
        sys.exit()

def parse_options():
    parser = OptionParser()
    parser.add_option('-i', '--info', action='store_true', dest='info', default=False, help='show script info and quit')
    options, _args = parser.parse_args()
    return options

class Schedule:
    def __init__(self):
        self.__id = ''
        self.__date_created = ''
        self.__date_modified = ''
        self.__academic_year = ''
        self.__student_id = ''
        self.__plan_name = ''
        self.__major = ''
        self.__school = ''
        self.__time_pref = ''
        self.__summer_pref = ''
        self.__start_quarter = ''
        self.__start_math = ''
        self.__start_english = ''
        self.__enroll_type = ''
        self.__job_type = ''
        self.__schedule_grade = ''
        self.__grade_reason = ''
        self.__quarters = []

    @property
    def id(self): return self.__id

    @id.setter
    def id(self, value): self.__id = value

    @property
    def date_created(self): return self.__date_created

    @date_created.setter
    def date_created(self, value): self.__date_created = value

    @property
    def date_modified(self): return self.__date_modified

    @date_modified.setter
    def date_modified(self, value): self.__date_modified = value

    @property
    def academic_year(self): return self.__academic_year

    @academic_year.setter
    def academic_year(self, value): self.__academic_year = value

    @property
    def student_id(self): return self.__student_id

    @student_id.setter
    def student_id(self, value): self.__student_id = value

    @property
    def grade_reason(self): return self.__grade_reason

    @grade_reason.setter
    def grade_reason(self, value): self.__grade_reason = value

    @property
    def plan_name(self): return self.__plan_name

    @plan_name.setter
    def plan_name(self, value): self.__plan_name = value

    @property
    def major(self): return self.__major

    @major.setter
    def major(self, value): self.__major = value

    @property
    def school(self): return self.__school

    @school.setter
    def school(self, value): self.__school = value

    @property
    def time_pref(self): return self.__time_pref

    @time_pref.setter
    def time_pref(self, value): self.__time_pref = value

    @property
    def summer_pref(self): return self.__summer_pref

    @summer_pref.setter
    def summer_pref(self, value): self.__summer_pref = value

    @property
    def start_quarter(self): return self.__start_quarter

    @start_quarter.setter
    def start_quarter(self, value): self.__start_quarter = value

    @property
    def start_math(self): return self.__start_math

    @start_math.setter
    def start_math(self, value): self.__start_math = value

    @property
    def start_english(self): return self.__start_english

    @start_english.setter
    def start_english(self, value): self.__start_english = value

    @property
    def enroll_type(self): return self.__enroll_type

    @enroll_type.setter
    def enroll_type(self, value): self.__enroll_type = value

    @property
    def job_type(self): return self.__job_type

    @job_type.setter
    def job_type(self, value): self.__job_type = value

    @property
    def schedule_grade(self): return self.__schedule_grade

    @schedule_grade.setter
    def schedule_grade(self, value): self.__schedule_grade = value

    @property
    def quarters(self): return self.__quarters

    def add_quarter(self, quarter): self.__quarters.append(quarter)

    '''
    NOTE: metadata for script if needed for get_data() return
    'id' : self.__id,
    'date_created' : self.__date_created,
    'date_modifieid' : self.__date_modified,
    'academic_year' : self.__academic_year,
    'student_id' : self.__student_id,
    '''
    def get_data(self):
        return {
            'plan_name': self.__plan_name,
            'major': self.__major,
            'school': self.__school,
            'time_preference': self.__time_pref,
            'summer_preference': self.__summer_pref,
            'starting_quarter': self.__start_quarter,
            'starting_math': self.__start_math,
            'starting_english': self.__start_english,
            'enrollment_type': self.__enroll_type,
            'job_type': self.__job_type,
            'schedule_grade' : self.__schedule_grade,
            'grade_reason' : self.__grade_reason,
            'quarters' : [quarter.get_data() for quarter in self.__quarters]
        }

class Quarter:
    def __init__(self):
        self.__id = ''
        self.__year = ''
        self.__title = ''
        self.__courses = []

    @property
    def id(self): return self.__id

    @id.setter
    def id(self, value): self.__id = value

    @property
    def year(self): return self.__year

    @year.setter
    def year(self, value): self.__year = value

    @property
    def title(self): return self.__title

    @title.setter
    def title(self, value): self.__title = value

    @property
    def courses(self): return self.__courses

    def add_course(self, course): self.__courses.append(course)

    def get_data(self):
        return {
            'id' : self.__id,
            'year' : self.__year,
            'title' : self.__title,
            'courses' : [course.get_data() for course in self.__courses]
        }

class Course:
    def __init__(self):
        self.__id = ''
        self.__title = ''
        self.__description = ''

    @property
    def id(self): return self.__id

    @id.setter
    def id(self, value): self.__id = value

    @property
    def title(self): return self.__title

    @title.setter
    def title(self, value): self.__title = value

    @property
    def description(self): return self.__description

    @description.setter
    def description(self, value): self.__description = value

    def get_data(self):
        return {
            'id' : self.__id,
            'title' : self.__title,
            'description' : self.__description
        }

if __name__ == '__main__':
    main()
