import sys
import csv
import formatting

def isComment(row):
    if row[0].startswith("#"):
        return True
    return False

def parse(csv_file):
    csv_reader = csv.reader(csv_file, delimiter=';')
    validate = formatting.validator()
    formatter = formatting.formatter()

    output = ""

    for row in csv_reader:
        if not isComment(row):
            if row[1]:
                # ship, check data
                if validate.checkShip(row):
                    print formatter.ship(row)
                else:
                    print "In row", csv_reader.line_num, row

            else:
                # group!
                print formatter.group(row)

def main():
    print "csv-to-shiplist.py"
    if ( len(sys.argv) == 2 ) and ( sys.argv[1].endswith("csv") ):
        csv_file = open(sys.argv[1], 'rb')
        parse(csv_file)
    else:
        print "add path to input data as first argument"

if __name__ == "__main__":
    main()