# Main routine.
# Run this script via:
#     $ python main.py

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
    initDatabase()
    sql.printNumRowsInTable('ipps2011')
    sql.printNumRowsInTable('ipps2012')
    sql.printNumRowsInTable('ipps2013')
    sql.printNumRowsInTable('usdaRestaurants')

