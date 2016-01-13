# Main routine.

import argparse

import fileio
import sql

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
    usdaRestaurantsFn = "data/USDA_Restaurants.csv"

    ippsData2011 = fileio.readIPPSFile(ippsFn2011)
    ippsData2012 = fileio.readIPPSFile(ippsFn2012)
    ippsData2013 = fileio.readIPPSFile(ippsFn2013)
    usdaRestaurantsData = fileio.readUSDARestaurantsFile(usdaRestaurantsFn)

    sql.initIPPSTable('ipps2011', ippsData2011)
    sql.initIPPSTable('ipps2012', ippsData2012)
    sql.initIPPSTable('ipps2013', ippsData2013)
    sql.initUSDARestaurantsTable('usdaRestaurants', usdaRestaurantsData)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process cmd line args.')
    parser.add_argument('--init', dest='init', action='store_true',
                        default=False)
    parser.add_argument('--analyze', dest='analyze', action='store_true',
                        default=False)
    args = parser.parse_args()
    if args.init and not args.analyze:
        print 'Initializing database tables...'
        initDatabase()
        print 'Done.'
    if args.analyze and not args.init:
        print 'Beginning analysis...'
        #analyze()
        print 'Done.'

