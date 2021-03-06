import sys
import csv
import formatting

def isComment(row):
    if row[0].startswith("#"):
        return True
    return False

def hasContent(row):
    for element in row:
        if element:
            return True
    return False

def parse(input, output):
    csv_reader = csv.reader(input, delimiter=';')
    validate = formatting.validator()
    formatter = formatting.formatter()

    try:
        for row in csv_reader:
            if hasContent(row):
                if not isComment(row):
                    if row[1]:
                        # ship, check data
                        if validate.checkShip(row):
                            formatter.ship(row)
                        else:
                            print "In row", csv_reader.line_num, row

                    else:
                        # group!
                        formatter.group(row)
        formatter.end()

        output.write(formatter.output)
    
    except ValueError as e:
        print "Error on Line {}: {}".format(csv_reader.line_num, e)


def main():
    print "csv-to-shiplist.py"
    if ( len(sys.argv) == 2 ) and ( sys.argv[1].endswith("csv") ):
        csv_file = open(sys.argv[1], 'rb')
        outfile = open("output.txt", "wb")
        parse(csv_file, outfile)
    else:
        print "add path to input data as first argument"

if __name__ == "__main__":
    main()