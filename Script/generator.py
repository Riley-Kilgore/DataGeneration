import sys
import schedule
import json
from optparse import OptionParser

version = 'v1.0'

def main():
    options = parse_options()
    if options.info:
        print('version: ' + version)
        sys.exit()
    while(True):
        create_schedule()
        while(True):
            cont = str(input('would you like to create another schedule (y/n)?\n')).lower()
            if cont == 'y' or cont == 'n':
                break
            print('ERROR: invalid input')
        if cont == 'n':
            break

def parse_options():
    parser = OptionParser()
    parser.add_option('-i', '--info', action='store_true', dest='info', default=False, help='show script info and quit')
    options, _args = parser.parse_args()
    return options

#TODO: expand to allow input for all relevant vars
def create_schedule():
    schdl = schedule.Schedule()
    schdl.student_id = 000
    write_json('test', schdl.get_data())

#TODO: probably need to format data in file differently to adhere with currently used json file format
def write_json(filename, data):
    with open(filename + '.json', 'a+') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    main()