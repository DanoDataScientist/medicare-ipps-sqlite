# Define functions that are used to retrieve the CMS data files.
# CMS = Centers for Medicare & Medicaid Services

import urllib

dataRoot = ('https://www.cms.gov/' +
            'Research-Statistics-Data-and-Systems/' +
            'Statistics-Trends-and-Reports/' +
            'Medicare-Provider-Charge-Data/' +
            'Downloads/')
data2011 = 'Inpatient_Data_2011_CSV.zip'
data2012 = 'Inpatient_Data_2012_CSV.zip'
data2013 = 'Inpatient_Data_2013_CSV.zip'

def retrieve():
    """Retrieve Medicare data files from cms.gov website.
    """
    print 'Retrieving Medicare data...'
    urllib.urlretrieve(dataRoot+data2011, 'data/'+data2011)
    print '2011 Medicare data retrieved.'
    urllib.urlretrieve(dataRoot+data2012, 'data/'+data2012)
    print '2012 Medicare data retrieved.'
    urllib.urlretrieve(dataRoot+data2013, 'data/'+data2013)
    print '2013 Medicare data retrieved.'

