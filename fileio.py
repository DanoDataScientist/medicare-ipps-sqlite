# Define functions for file I/O.

import csv

def get_state_abbrev(s):
    """Return the two-letter abbreviation associated with a state name.
    An abbreviation is also provided for 'United States'.

    Arguments:
    s (string) -- full name of state with first letter capitalized

    Returns:
    (string) -- two-letter state abbreviation
    """
    abbrev_dict = {'Alabama':'AL',
                   'Alaska':'AK',
                   'Arizona':'AZ',
                   'Arkansas':'AR',
                   'California':'CA',
                   'Colorado':'CO',
                   'Connecticut':'CT',
                   'Delaware':'DE',
                   'District of Columbia':'DC',
                   'Florida':'FL',
                   'Georgia':'GA',
                   'Hawaii':'HI',
                   'Idaho':'ID',
                   'Illinois':'IL',
                   'Indiana':'IN',
                   'Iowa':'IA',
                   'Kansas':'KS',
                   'Kentucky':'KY',
                   'Louisiana':'LA',
                   'Maine':'ME',
                   'Maryland':'MD',
                   'Massachusetts':'MA',
                   'Michigan':'MI',
                   'Minnesota':'MN',
                   'Mississippi':'MS',
                   'Missouri':'MO',
                   'Montana':'MT',
                   'Nebraska':'NE',
                   'Nevada':'NV',
                   'New Hampshire':'NH',
                   'New Jersey':'NJ',
                   'New Mexico':'NM',
                   'New York':'NY',
                   'North Carolina':'NC',
                   'North Dakota':'ND',
                   'Ohio':'OH',
                   'Oklahoma':'OK',
                   'Oregon':'OR',
                   'Pennsylvania':'PA',
                   'Rhode Island':'RI',
                   'South Carolina':'SC',
                   'South Dakota':'SD',
                   'Tennessee':'TN',
                   'Texas':'TX',
                   'United States':'US',
                   'Utah':'UT',
                   'Vermont':'VT',
                   'Virginia':'VA',
                   'Washington':'WA',
                   'West Virginia':'WV',
                   'Wisconsin':'WI',
                   'Wyoming':'WY'}
    return abbrev_dict[s]

def read_ipps_file(fn):
    """Read IPPS CSV file.

    Arguments:
    fn (string) -- name of IPPS data file

    Returns:
    List of tuples (each tuple is a row of data)
    """
    all_rows = []
    i = 0
    f = open(fn, 'rb')
    csv_data = csv.reader(f, delimiter=',', quotechar='"')
    for row in csv_data:
        # Skip first row (contains column names) and empty rows
        if i != 0 and len(row[0]) != 0:
            f0 = row[0]           # drgDefinition
            f1 = int(row[1])      # providerId
            f2 = row[2]           # providerName
            f3 = row[3]           # providerStreetAddress
            f4 = row[4]           # providerCity
            f5 = row[5]           # providerState
            f6 = int(row[6])      # providerZipCode
            f7 = row[7]           # hrrDescription
            f8 = int(row[8])      # totalDischarges
            f9 = float(row[9])    # avgCoveredCharges
            f10 = float(row[10])  # avgTotalPayments
            f11 = float(row[11])  # avgMedicarePayments
            f12 = f10-f11         # avgNonMedicarePayments
            f13 = f9-f10          # avgCoveredChargesMinusTotalPayments
            t = (f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13)
            all_rows.append(t)
        i += 1
    f.close()
    return all_rows

def read_state_pop_est_file(fn):
    """Read state population estimate CSV file.

    Arguments:
    fn (string) -- name of state population estimate data file

    Returns:
    List of tuples (each tuple is a row of data)
    """
    all_rows = []
    i = 0
    f = open(fn, 'rb')
    csv_data = csv.reader(f, delimiter=',', quotechar='"')
    for row in csv_data:
        # Skip first row (contains column names) and empty rows
        if i != 0 and len(row[0]) != 0:
            f0 = row[0]           # sumLev
            f1 = int(row[1])      # region
            f2 = int(row[2])      # division
            f3 = int(row[3])      # state
            f4 = get_state_abbrev(row[4])  # name
            f5 = int(row[5])      # sex
            f6 = int(row[6])      # age
            f7 = int(row[7])      # estBase2010Civ
            f8 = int(row[8])      # popEst2010Civ
            f9 = int(row[9])      # popEst2011Civ
            f10 = int(row[10])    # popEst2012Civ
            f11 = int(row[11])    # popEst2013Civ
            f12 = int(row[12])    # popEst2014Civ
            t = (f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12)
            all_rows.append(t)
        i += 1
    f.close()
    return all_rows

def write_query_results(fn, qs, d):
    """Write SQL query results to a text file.

    Arguments:
    fn (string) -- name of file to which data are written
    qs (string) -- SQL query statement
    d (list of tuples) -- SQL query results
    """
    f = open(fn, 'w')
    f.write('%s\n' % qs)
    for row in d:
        n = len(row)
        for i in range(len(row)):
            f.write('%s' % row[i])
            if i != (n-1):
                f.write(',')
        f.write('\n')
    f.close()

