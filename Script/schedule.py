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

class Preferences:
    def __init__(self):
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
        
    @property
    def courses(self): return self.__courses

    @courses.setter
    def courses(self, value): self.__courses = value
    
    @property
    def credits(self): return self.__credits
    
    @credits.setter
    def credits(self, value): self.__credits = value
    
    @property
    def english(self): return self.__english
    
    @english.setter
    def english(self, value): self.__english = value
    
    @property
    def enrollment(self): return self.__enrollment
    
    @enrollment.setter
    def enrollment(self, value): self.__enrollment = value
    
    @property
    def evening(self): return self.__evening
    
    @evening.setter
    def evening(self, value): self.__evening = value
    
    @property
    def job(self): return self.__job
    
    @job.setter
    def job(self, value): self.__job = value
    
    @property
    def major(self): return self.__major
    
    @major.setter
    def major(self, value): self.__major = value
    
    @property
    def math(self): return self.__math
    
    @math.setter
    def math(self, value): self.__math = value
    
    @property
    def quarter(self): return self.__quarter
    
    @quarter.setter
    def quarter(self, value): self.__quarter = value
    
    @property
    def quarters(self): return self.__quarters
    
    @quarter.setter
    def quarters(self, value): self.__quarters = value
    
    @property
    def school(self): return self.__school
    
    @school.setter
    def school(self, value): self.__school = value
    
    @property
    def summer(self): return self.__summer
    
    @summer.setter
    def summer(self, value): self.__summer = value
    
    def get_data(self):
        return {
            'credits': self.__credits,
            'english': self.__english,
            'enrollment': self.__enrollment,
            'evening': self.__evening,
            'job': self.__job,
            'major': self.__major,
            'math': self.__math,
            'quarter': self.__quarter,
            'quarters': self.__quarters,
            'school': self.__school,
            'summer' : self.__summer
        }
    
class Schedule:
    def __init__(self):
        self.__id = ''
        self.__date_created = ''
        self.__date_modified = ''
        self.__academic_year = ''
        self.__student_id = ''
        self.__metadata = ''
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
    def metadata(self): return self.__metadata
    
    @metadata.setter
    def metadata(self, value): self.__metadata = value

    @property
    def quarters(self): return self.__quarters

    def add_quarter(self, quarter): self.__quarters.append(quarter)

    '''
        self.__id = ''
        self.__date_created = ''
        self.__date_modified = ''
        self.__academic_year = ''
        self.__student_id = ''
        self.__metadata = ''
        self.__quarters = []
    '''
    def get_data(self):
        return {
            'id': self.__id,
            'date_created': self.__date_created,
            'date_modified': self.__date_modified,
            'academic_year': self.__academic_year,
            'student_id': self.__student_id,
            'metadata': self.__metadata,
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
