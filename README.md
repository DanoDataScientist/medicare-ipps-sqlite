## medicare-ipps-analysis

#### Currently under development...


#### Overview
medicare-ipps-analysis allows you to easily extract, compare, and plot data from the following public data sets:
* [Medicare Provider Utilization and Payment Data: Inpatient (2011, 2012, 2013)](https://www.cms.gov/research-statistics-data-and-systems/statistics-trends-and-reports/medicare-provider-charge-data/inpatient.html)
* [USDA Food Environment Atlas, Restaurant Data (2007, 2012)](http://www.ers.usda.gov/data-products/food-environment-atlas.aspx)


#### Running the program

This program was developed and tested using Python 2.7 in a Linux Ubuntu 14.04 environment.

To run this program, use `python` to run the `main.py` file using one of the following command-line arguments:
* `--retrieve  (download Medicare data files into the data/ directory)`
* `--init      (read the Medicare CSV data and insert into a SQLite database)`
* `--purge     (drop all tables in the SQLite database)`
* `--analyze   (process the analysis.config file and run the analysis)`

Note that:
* You must run `python main.py --retrieve` before running `python main.py --init`
* You must run `python main.py --init` before running `python main.py --purge`
* You must run `python main.py --init` before running `python main.py --analyze`


#### USDA food environment atlas data
* Go to the [data webpage](http://www.ers.usda.gov/data-products/food-environment-atlas/data-access-and-documentation-downloads.aspx)
* In the "Data Set" column, under "Current Version", select the "Data Download" link (last updated 8/19/2015)
* This will prompt you to download a Microsoft Excel file named "DataDownload.xls"
* After opening the file, you can find the restaurant data in the "RESTAURANTS" tab

