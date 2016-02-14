# Define function used to retrieve the U.S. Census Bureau data file for
# the Vintage 2014 State Population Dataset: Single year of age and
# sex population estimates (April 1, 2010 to July 1, 2014 - CIVILIAN).

import urllib

data_root = ('http://www.census.gov/' +
             'popest/' +
             'data/' +
             'state/' +
             'asrh/' +
             '2014/' +
             'files/')
data = 'SC-EST2014-AGESEX-CIV.csv'
data_dir = 'data/'

def retrieve():
    """Retrieve U.S. Census Bureau data file from census.gov website.
    """
    urllib.urlretrieve(data_root+data, data_dir+data)
    print 'U.S. Census Bureau data retrieved.'

