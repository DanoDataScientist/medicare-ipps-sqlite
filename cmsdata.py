# Define functions that are used to retrieve the CMS data files.
# CMS = Centers for Medicare & Medicaid Services

import sys
import urllib
import zipfile

data_root = ('https://www.cms.gov/' +
            'Research-Statistics-Data-and-Systems/' +
            'Statistics-Trends-and-Reports/' +
            'Medicare-Provider-Charge-Data/' +
            'Downloads/')
data2011 = 'Inpatient_Data_2011_CSV.zip'
data2012 = 'Inpatient_Data_2012_CSV.zip'
data2013 = 'Inpatient_Data_2013_CSV.zip'
data_dir = 'data/'

def retrieve():
    """Retrieve Medicare data files from cms.gov website.
    """
    urllib.urlretrieve(data_root+data2011, data_dir+data2011)
    print '2011 Medicare data retrieved.'
    urllib.urlretrieve(data_root+data2012, data_dir+data2012)
    print '2012 Medicare data retrieved.'
    urllib.urlretrieve(data_root+data2013, data_dir+data2013)
    print '2013 Medicare data retrieved.'

def validate_zip_file(fn):
    """Verify that a data file is a valid zip file.

    Arguments:
    fn (string) -- name of zip file to validate
    """
    if not zipfile.is_zipfile(fn):
        print '"%s" is not a valid zip file. Exiting now.' % fn
        sys.exit()

def unzip(fn, fe):
    """Unzip a zip file and extract files with a specific extension.

    Arguments:
    fn (string) -- name of file to unzip
    fe (string) -- file extension of file to extract (ex: '.csv')
    """
    validate_zip_file(fn)
    z = zipfile.ZipFile(fn)
    for am in z.namelist():
        if fe in am:
            z.extract(am, data_dir)
    z.close()

def unzip_all():
    """Unzip the PDF file (from the 2011 dataset) and all CSV data files.
    """
    unzip(data_dir+data2011, '.pdf')
    unzip(data_dir+data2011, '.csv')
    unzip(data_dir+data2012, '.csv')
    unzip(data_dir+data2013, '.csv')
    # Verify md5 or sha sums of files...

