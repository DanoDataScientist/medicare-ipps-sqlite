# Define functions that are used to retrieve the CMS data files.
# CMS = Centers for Medicare & Medicaid Services

import sys
import urllib
import zipfile

dataRoot = ('https://www.cms.gov/' +
            'Research-Statistics-Data-and-Systems/' +
            'Statistics-Trends-and-Reports/' +
            'Medicare-Provider-Charge-Data/' +
            'Downloads/')
data2011 = 'Inpatient_Data_2011_CSV.zip'
data2012 = 'Inpatient_Data_2012_CSV.zip'
data2013 = 'Inpatient_Data_2013_CSV.zip'
dataDir = 'data/'

def retrieve():
    """Retrieve Medicare data files from cms.gov website.
    """
    print 'Retrieving Medicare data...'
    urllib.urlretrieve(dataRoot+data2011, dataDir+data2011)
    print '2011 Medicare data retrieved.'
    urllib.urlretrieve(dataRoot+data2012, dataDir+data2012)
    print '2012 Medicare data retrieved.'
    urllib.urlretrieve(dataRoot+data2013, dataDir+data2013)
    print '2013 Medicare data retrieved.'

def validateZipFile(fn):
    """Verify that a data file is a valid zip file.

    Arguments:
    fn (string) -- name of zip file to validate
    """
    if not zipfile.is_zipfile(fn):
        print '"%s" is not a valid zip file. Exiting now.' % fn
        sys.exit()
