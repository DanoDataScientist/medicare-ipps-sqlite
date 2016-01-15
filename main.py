# Main routine.

import argparse

import analysis
import cmsdata
import fileio
import sql
import usdadata

def retrieveData():
    """Retrieve data.
    """
    cmsdata.retrieve()
    cmsdata.unzipAll()
    usdadata.retrieve()

def initDatabase():
    """Initialize database.

    Actions:
    -- Read data from CSV files
    -- Create SQL tables
    -- Insert data into SQL tables
    """
    ippsFn2011 = "data/Medicare_Provider_Charge_Inpatient_DRG100_FY2011.csv"
    ippsFn2012 = "data/Medicare_Provider_Charge_Inpatient_DRG100_FY2012.csv"
    ippsFn2013 = "data/Medicare_Provider_Charge_Inpatient_DRG100_FY2013.csv"
    ippsData2011 = fileio.readIPPSFile(ippsFn2011)
    ippsData2012 = fileio.readIPPSFile(ippsFn2012)
    ippsData2013 = fileio.readIPPSFile(ippsFn2013)
    sql.initIPPSTable('ipps2011', ippsData2011)
    sql.initIPPSTable('ipps2012', ippsData2012)
    sql.initIPPSTable('ipps2013', ippsData2013)

def purgeDatabase():
    """Purge database.

    Actions:
    -- Drop all SQL tables
    """
    sql.dropTable('ipps2011')
    sql.dropTable('ipps2012')
    sql.dropTable('ipps2013')

def analyze():
    """Run analysis.
    """
    analysis.readConfigFile()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process cmd line args.')
    parser.add_argument('--retrieve', dest='retrieve', action='store_true',
                        default=False)
    parser.add_argument('--init', dest='init', action='store_true',
                        default=False)
    parser.add_argument('--purge', dest='purge', action='store_true',
                        default=False)
    parser.add_argument('--analyze', dest='analyze', action='store_true',
                        default=False)
    args = parser.parse_args()
    if args.retrieve and not args.init and not args.purge and not args.analyze:
        print 'Retrieving data...'
        retrieveData()
        print 'Done.'
    if args.init and not args.retrieve and not args.purge and not args.analyze:
        print 'Initializing database tables...'
        initDatabase()
        print 'Done.'
    if args.purge and not args.retrieve and not args.init and not args.analyze:
        print 'Purging database (dropping all tables)...'
        purgeDatabase()
        print 'Done.'
    if args.analyze and not args.retrieve and not args.init and not args.purge:
        print 'Beginning analysis...'
        analyze()
        print 'Done.'

