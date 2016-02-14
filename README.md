medicare-ipps-sqlite allows you to execute SQL queries for the Inpatient Medicare Provider Utilization and Payment data and U.S. Census Bureau state population data.

Main data pages:
* [Medicare Provider Utilization and Payment Data: Inpatient (2011, 2012, 2013)](https://www.cms.gov/research-statistics-data-and-systems/statistics-trends-and-reports/medicare-provider-charge-data/inpatient.html)
* [U.S. Census Bureau, Vintage 2014 State Population Datasets (2010, 2011, 2012, 2013, 2014)](http://www.census.gov/popest/data/datasets.html)


## Development and testing environment

* Python 2.7
* Linux Ubuntu 12.04 and 14.04


## Running the program

##### Retrieve data
* Run the following command from the terminal: `python main.py --retrieve`
* The Medicare data files will be downloaded and extracted into the `data/` directory.
* The U.S. Census Bureau data file will be downloaded into the `data/` directory.

##### Initialize database
* You must retrieve the data files before you can initialize the database.
* Run the following command from the terminal: `python main.py --init`
* This will insert the data into a SQLite database.

##### Purge database (if needed)
* You must initialize the database before you can purge the database.
* Run the following command from the terminal: `python main.py --purge`
* This will purge data from the SQLite database (all tables are dropped).

##### Execute SQL queries
* You must initialize the database before you can execute SQL queries.
* Add your SQL query statement(s) to the `query_list` file.
* Each SQL query statement needs a unique identifier (`q1`, `q2`, `q3`, etc).
* Run the following command from the terminal: `python main.py --query`
* The results of your SQL queries will be written to the `query_results` directory.


## Database schema

##### Medicare data tables
* Refer to the `data/Medicare_Hospital_Inpatient_PUF_Methodology_2014-05-30.pdf` file for detailed descriptions of the data.
* Refer to `data/drgDefinitions_ipps2011`, `data/drgDefinitions_ipps2012`, and `data/drgDefinitions_ipps2013` for lists of the DRG definitions for each year.
* Table names: `ipps2011`, `ipps2012`, `ipps2013`
* Table columns:
  * drgDefinition text
  * providerId integer
  * providerName text
  * providerStreetAddress text
  * providerCity text
  * providerState text
  * providerZipCode integer
  * hrrDescription text
  * totalDischarges integer
  * avgCoveredCharges real
  * avgTotalPayments real
  * avgMedicarePayments real
  * avgNonMedicarePayments real
  * avgCoveredChargesMinusTotalPayments real

##### U.S. Census Bureau data table
* Refer to the [state population estimate file layout PDF](http://www.census.gov/popest/data/state/asrh/2014/files/SC-EST2014-AGESEX-CIV.pdf) for detailed descriptions of the data.
* Table name: `statePopEst`
* Table columns:
  * sumLev text
  * region integer
  * division integer
  * state integer
  * name text
  * sex integer
  * age integer
  * estBase2010Civ integer
  * popEst2010Civ integer
  * popEst2011Civ integer
  * popEst2012Civ integer
  * popEst2013Civ integer
  * popEst2014Civ integer


## Links to data pages
* [Medicare Provider Utilization and Payment Data: Inpatient (2011)](https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Inpatient2011.html)
* [Medicare Provider Utilization and Payment Data: Inpatient (2012)](https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Inpatient2012.html)
* [Medicare Provider Utilization and Payment Data: Inpatient (2013)](https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Inpatient2013.html)
* [U.S. Census Bureau, Vintage 2014 State Population Dataset: Single year of age and sex population estimates (April 1, 2010 to July 1, 2014 - CIVILIAN)](http://www.census.gov/popest/data/state/asrh/2014/SC-EST2014-AGESEX-CIV.html)

