## medicare-ipps-analysis

#### Currently under development...


#### Overview
medicare-ipps-analysis allows you to easily extract, compare, and plot data from the following public data sets:
* [Medicare Provider Utilization and Payment Data: Inpatient (2011, 2012, 2013)](https://www.cms.gov/research-statistics-data-and-systems/statistics-trends-and-reports/medicare-provider-charge-data/inpatient.html)
* [U.S. Census Bureau, Vintage 2014 State Population Datasets (2010, 2011, 2012, 2013, 2014)](http://www.census.gov/popest/data/datasets.html)
* [USDA Food Environment Atlas, Restaurant Data (2007, 2012)](http://www.ers.usda.gov/data-products/food-environment-atlas.aspx)


#### Running the program

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
  * Select the `RESTAURANTS` tab.
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
* Run the following command from the terminal: `python main.py --analyze`
* This will run the analysis.


#### Links to data pages
* [Medicare Provider Utilization and Payment Data: Inpatient (2011)](https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Inpatient2011.html)
* [Medicare Provider Utilization and Payment Data: Inpatient (2012)](https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Inpatient2012.html)
* [Medicare Provider Utilization and Payment Data: Inpatient (2013)](https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Inpatient2013.html)
* [U.S. Census Bureau, Vintage 2014 State Population Dataset: Single year of age and sex population estimates (April 1, 2010 to July 1, 2014 - CIVILIAN)](http://www.census.gov/popest/data/state/asrh/2014/SC-EST2014-AGESEX-CIV.html)
* [USDA Food Environment Atlas data, Current Version, Last Updated 8/19/2015](http://www.ers.usda.gov/data-products/food-environment-atlas/data-access-and-documentation-downloads.aspx)

