import sys
import re
import csv

def isComment(row):
    if row[0].startswith("#"):
        return True
    return False

def parse(csv_file):
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        if not isComment(row):
            print row


def main():
    print "csv-to-shiplist.py"
    if ( len(sys.argv) == 2 ) and ( sys.argv[1].endswith("csv") ):
        csv_file = open(sys.argv[1], 'rb')
        parse(csv_file)
    else:
        print "add path to input data as first argument"

if __name__ == "__main__":
    main()