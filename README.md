## medicare-ipps-analysis

medicare-ipps-analysis allows you to easily extract, compare, and plot data from the following public data sets:
* [Medicare Provider Utilization and Payment Data: Inpatient (2011, 2012, 2013)](https://www.cms.gov/research-statistics-data-and-systems/statistics-trends-and-reports/medicare-provider-charge-data/inpatient.html)
* [U.S. Census Bureau, Vintage 2014 State Population Datasets (2010, 2011, 2012, 2013, 2014)](http://www.census.gov/popest/data/datasets.html)
* [USDA Food Environment Atlas, Restaurant Data (2007, 2012)](http://www.ers.usda.gov/data-products/food-environment-atlas.aspx)


## Current features
* Retrieve Medicare, U.S. Census Bureau, and USDA data files from their respective websites.
* Create a SQLite database and a table for each dataset.
* Insert data into their respective tables.
* Purge the SQLite database (all tables are dropped) if needed.
* Execute all SQL query statements in the `analysis.config` file and write the results of each query to a separate file in the `results` directory.


## Future features
* Perform comparisons of data from different datasets.
* Create plots of data from one or more datasets.


## Running the program

This program was developed and tested using:
* Linux Ubuntu 14.04
* Python 2.7
* LibreOffice Calc 4.2

##### Retrieve data
* Run the following command from the terminal: `python main.py --retrieve`
* The Medicare data files will be downloaded and extracted into the `data/` directory.
* The U.S. Census Bureau data file will be downloaded into the `data/` directory.
* The USDA data file will be downloaded into the `data/` directory.
* Save the USDA data in CSV format:
  * Open the `data/USDA_FEA_DataDownload.xls` file in LibreOffice Calc.
  * Select the `RESTAURANTS` sheet.
  * Go to "File" > "Save As...".
  * Save the CSV file as `USDA_FEA_DataDownload.csv` in the `data/` directory.
  * Specify: File type = "Text CSV"
  * Specify: Character set = "Unicode (UTF-8)"
  * Specify: Field delimiter = `,` (comma)
  * Specify: Text delimiter = `"` (double quote)
  * Select checkbox for: "Save cell content as shown"
  * Leave other checkboxes unselected.

##### Initialize database
* You must retrieve the data files before you can initialize the database.
* Run the following command from the terminal: `python main.py --init`
* This will insert the data into a SQLite database.

##### Purge database (if needed)
* You must initialize the database before you can purge the database.
* Run the following command from the terminal: `python main.py --purge`
* This will purge data from the SQLite database (all tables are dropped).

##### Run analysis
* You must initialize the database before you can run the analysis.
* Add your SQL query statement(s) to the `analysis.config` file.
* Each SQL query statement needs a unique identifier (`q1`, `q2`, `q3`, etc).
* Run the following command from the terminal: `python main.py --analyze`
* This will run the analysis.


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

##### USDA data table
* Refer to the "Variable List" sheet in the `data/USDA_FEA_DataDownload.xls` file for detailed descriptions of the data.
* Table name: `usdaRestaurants`
* Table columns:
  * fips text
  * state text
  * county text
  * ffr07 integer
  * ffr12 integer
  * pch_ffr_07_12 real
  * ffrpth07 real
  * ffrpth12 real
  * pch_ffrpth_07_12 real
  * fsr07 integer
  * fsr12 integer
  * pch_fsr_07_12 real
  * fsrpth07 real
  * fsrpth12 real
  * pch_fsrpth_07_12 real
  * pc_ffrsales02 real
  * pc_ffrsales07 real
  * pc_fsrsales02 real
  * pc_fsrsales07 real


## Links to data pages
* [Medicare Provider Utilization and Payment Data: Inpatient (2011)](https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Inpatient2011.html)
* [Medicare Provider Utilization and Payment Data: Inpatient (2012)](https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Inpatient2012.html)
* [Medicare Provider Utilization and Payment Data: Inpatient (2013)](https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Inpatient2013.html)
* [U.S. Census Bureau, Vintage 2014 State Population Dataset: Single year of age and sex population estimates (April 1, 2010 to July 1, 2014 - CIVILIAN)](http://www.census.gov/popest/data/state/asrh/2014/SC-EST2014-AGESEX-CIV.html)
* [USDA Food Environment Atlas data, Current Version, Last Updated 8/19/2015](http://www.ers.usda.gov/data-products/food-environment-atlas/data-access-and-documentation-downloads.aspx)

