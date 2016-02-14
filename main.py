# Main routine.

import argparse

import analysis
import censusdata
import cmsdata
import fileio
import sql

def retrieveData():
    """Retrieve data.
    """
    cmsdata.retrieve()
    cmsdata.unzipAll()
    censusdata.retrieve()

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
    statePopEstFn = 'data/SC-EST2014-AGESEX-CIV.csv'
    ippsData2011 = fileio.readIPPSFile(ippsFn2011)
    ippsData2012 = fileio.readIPPSFile(ippsFn2012)
    ippsData2013 = fileio.readIPPSFile(ippsFn2013)
    statePopEstData = fileio.readStatePopEstFile(statePopEstFn)
    sql.initIPPSTable('ipps2011', ippsData2011)
    sql.initIPPSTable('ipps2012', ippsData2012)
    sql.initIPPSTable('ipps2013', ippsData2013)
    sql.initStatePopEstTable('statePopEst', statePopEstData)

def purgeDatabase():
    """Purge database.

    Actions:
    -- Drop all SQL tables
    """
    sql.dropTable('ipps2011')
    sql.dropTable('ipps2012')
    sql.dropTable('ipps2013')
    sql.dropTable('statePopEst')

def query():
    """Execute SQL queries.
    """
    analysis.readConfigFile()
    fnId = 1
    for qs in analysis.sqlQueries:
        results = sql.query(qs)
        fn = 'results/q' + str(fnId) + '_results'
        fileio.writeQueryResults(fn, qs, results)
        fnId += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process cmd line args.')
    parser.add_argument('--retrieve', dest='retrieve', action='store_true',
                        default=False)
    parser.add_argument('--init', dest='init', action='store_true',
                        default=False)
    parser.add_argument('--purge', dest='purge', action='store_true',
                        default=False)
    parser.add_argument('--query', dest='query', action='store_true',
                        default=False)
    args = parser.parse_args()
    if args.retrieve and not args.init and not args.purge and not args.query:
        print 'Retrieving data...'
        retrieveData()
        print 'Done.'
    if args.init and not args.retrieve and not args.purge and not args.query:
        print 'Initializing database tables...'
        initDatabase()
        print 'Done.'
    if args.purge and not args.retrieve and not args.init and not args.query:
        print 'Purging database (dropping all tables)...'
        purgeDatabase()
        print 'Done.'
    if args.query and not args.retrieve and not args.init and not args.purge:
        print 'Execute SQL queries...'
        query()
        print 'Done.'

