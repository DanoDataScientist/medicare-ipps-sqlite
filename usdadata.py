# Define function used to retrieve the USDA FEA data file.
# USDA = United States Department of Agriculture
# FEA = Food Environment Atlas

import urllib

dataRoot = ('http://www.ers.usda.gov/' +
            'datafiles/' +
            'Food_Environment_Atlas/' +
            'Data_Access_and_Documentation_Downloads/' +
            'Current_Version/')
data = 'DataDownload.xls'
dataDir = 'data/'

def retrieve():
    """Retrieve USDA Food Environment Atlas data file from usda.gov website.
    """
    urllib.urlretrieve(dataRoot+data, dataDir+'USDA_FEA_'+data)
    print 'USDA Food Environment Atlas data retrieved.'

