# Define functions used to run the analysis.

import ConfigParser

sqlQueries = []

def readConfigFile():
    """Read the analysis.config file.
    """
    config = ConfigParser.RawConfigParser()
    config.read('analysis.config')
    for i in config.options('sql'):
        sqlQueries.append(config.get('sql', i))

