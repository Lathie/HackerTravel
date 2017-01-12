
import csv
import sys

school_dict = {} #counts hackers accepted from schools
total_accepted = 0
school_dict_total = {} #counts hackers applied from schools
total_applied = 0
school_bus_requests = {}
bus_requests = 0

def extract():
    try:
        csv_raw = open("hackerdata.csv", "rt")
        csv_input = csv.reader(csv_raw)

        csv_input.next() #Skip column names

        for row in csv_input:
            #print str(row[15])
            #START COUNTING THINGS NOW :DDD
            if row[15].upper() not in school_dict:
                school_dict[row[15].upper()] = 0
            if row[4] == "ACCEPTED":
                school_dict[row[15].upper()] += 1
                total_accepted += 1

            if row[15].upper() not in school_bus_requests:
                school_bus_requests[row[15].upper()] = 0
            if row[4] == "ACCEPTED":
                if "BUS" in row[9]:
                    print row[9]
                    school_bus_requests[row[15].upper()] += 1
                    bus_requests += 1

            if row[15].upper() not in school_dict_total:
                school_dict_total[row[15].upper()] = 0
            school_dict_total[row[15].upper()] += 1
            total_applied += 1

            #THATS ALL FOLKS
        csv_raw.close()

        for thing in school_dict:
            print thing + "," + str(school_dict[thing]) + "," + str(school_dict_total[thing]) + "," + str(school_bus_requests[row[15].upper()])

        print "accepted: " + str(total_accepted)
        print "applied: " + str(total_applied)
        print "bus requests: " + str(bus_requests)



    except IOError as error:
        print "NO CSV FILE"
        sys.exit(1)

extract()
