


def parse(csv_file):

    hackers_accepted_total = 2000

    try:
        csv_raw = open(csv_file, "rt")
        csv_input = csv.reader(csv_raw)

        for row in csv_input:

            score = row[1] * (row[2]/hackers_accepted_total)

            print str(row[0]) + " -- Score: " + str(score)
