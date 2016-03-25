# Main routine.

import argparse
import ConfigParser

import censusdata
import cmsdata
import fileio
import sql

# Global variables
sql_queries = []

def retrieve_data():
    """Retrieve data.
    """
    cmsdata.retrieve()
    cmsdata.unzip_all()
    censusdata.retrieve()

def init_database():
    """Initialize database.

    Actions:
    -- Read data from CSV files
    -- Create SQL tables
    -- Insert data into SQL tables
    """
    ipps_fn_2011 = "data/Medicare_Provider_Charge_Inpatient_DRG100_FY2011.csv"
    ipps_fn_2012 = "data/Medicare_Provider_Charge_Inpatient_DRG100_FY2012.csv"
    ipps_fn_2013 = "data/Medicare_Provider_Charge_Inpatient_DRG100_FY2013.csv"
    state_pop_est_fn = 'data/SC-EST2014-AGESEX-CIV.csv'
    ipps_data_2011 = fileio.read_ipps_file(ipps_fn_2011)
    ipps_data_2012 = fileio.read_ipps_file(ipps_fn_2012)
    ipps_data_2013 = fileio.read_ipps_file(ipps_fn_2013)
    state_pop_est_data = fileio.read_state_pop_est_file(state_pop_est_fn)
    sql.init_ipps_table('ipps2011', ipps_data_2011)
    sql.init_ipps_table('ipps2012', ipps_data_2012)
    sql.init_ipps_table('ipps2013', ipps_data_2013)
    sql.init_state_pop_est_table('statePopEst', state_pop_est_data)

def purge_database():
    """Purge database.

    Actions:
    -- Drop all SQL tables
    """
    sql.drop_table('ipps2011')
    sql.drop_table('ipps2012')
    sql.drop_table('ipps2013')
    sql.drop_table('statePopEst')

def read_query_list():
    """Read the query_list file.
    """
    config = ConfigParser.RawConfigParser()
    config.read('query_list')
    for i in config.options('sql'):
        sql_queries.append(config.get('sql', i))

def query():
    """Execute SQL queries.
    """
    read_query_list()
    fn_id = 1
    for qs in sql_queries:
        results = sql.query(qs)
        fn = 'query_results/q' + str(fn_id) + '_results'
        fileio.write_query_results(fn, qs, results)
        fn_id += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='medicare-ipps-sqlite')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--retrieve', dest='retrieve', action='store_true',
                        default=False)
    group.add_argument('--init', dest='init', action='store_true',
                        default=False)
    group.add_argument('--purge', dest='purge', action='store_true',
                        default=False)
    group.add_argument('--query', dest='query', action='store_true',
                        default=False)
    args = parser.parse_args()
    if args.retrieve:
        print 'Retrieving data...'
        retrieve_data()
        print 'Done.'
    if args.init:
        print 'Initializing database tables...'
        init_database()
        print 'Done.'
    if args.purge:
        print 'Purging database (dropping all tables)...'
        purge_database()
        print 'Done.'
    if args.query:
        print 'Execute SQL queries...'
        query()
        print 'Done.'

