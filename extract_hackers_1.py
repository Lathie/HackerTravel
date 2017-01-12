
import csv
import sys
import pprint


def extract():
    try:
        csv_raw = open("hackerdata.csv", "rt")
        csv_input = csv.reader(csv_raw)

        csv_input.next() #Skip column names

        global school_dict
        global school_dict_total
        global school_bus_requests

        school_dict = {} #counts hackers accepted from schools
        school_dict_total = {} #counts hackers applied from schools
        school_bus_requests = {}

        global total_accepted
        global bus_requests
        global total_applied

        total_accepted = 0
        bus_requests = 0
        total_applied = 0
        for row in csv_input:

            cur_school = row[15].upper()
            cur_school = cur_school.replace(',', '')

            #START COUNTING THINGS NOW :DD

            if cur_school not in school_dict:
                school_dict[cur_school] = 0
            if row[4] == "ACCEPTED":
                school_dict[cur_school] += 1
                total_accepted += 1

            if cur_school not in school_bus_requests:
                school_bus_requests[cur_school] = 0
            if row[4] == "ACCEPTED":
                if "BUS" in row[9]:
                    #print row[9]
                    school_bus_requests[cur_school] += 1
                    bus_requests += 1

            if cur_school not in school_dict_total:
                school_dict_total[cur_school] = 0
            school_dict_total[cur_school] += 1
            total_applied += 1

            #THATS ALL FOLKS
        csv_raw.close()

        #for thing in school_dict:
        #    print thing + "," + str(school_dict[thing]) + "," + str(school_dict_total[thing]) + "," + str(school_bus_requests[thing])

        #print "accepted: " + str(total_accepted)
        #print "applied: " + str(total_applied)
        #print "bus requests: " + str(bus_requests)

        #pprint.pprint(school_bus_requests, width=1)

    except IOError as error:
        print "NO CSV FILE"
        sys.exit(1)


def model():
    global results
    results = {}

    for thing in school_dict:
        multi = float(school_dict[thing])/float(total_accepted)
        results[thing] = 100 * float(school_bus_requests[thing]) * multi

    for thing in results:
        if results[thing] == 0:
            continue
        print thing + "," + str(results[thing])


if __name__ == "__main__":
    extract()
    model()
