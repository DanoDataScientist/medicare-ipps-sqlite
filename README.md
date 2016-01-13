## medicare-ipps-analysis

#### Overview
medicare-ipps-analysis allows you to easily extract, compare, and plot data from the following public data sets:
* [Medicare Provider Utilization and Payment Data: Inpatient (2011, 2012, 2013)](https://www.cms.gov/research-statistics-data-and-systems/statistics-trends-and-reports/medicare-provider-charge-data/inpatient.html)
* [USDA Food Environment Atlas (2007, 2012)](http://www.ers.usda.gov/data-products/food-environment-atlas.aspx)

Currently, this project focuses on analysis of only the restaurant data from the USDA Food Environment Atlas.

#### Data download instructions

###### Medicare 2011 data
* Go to the [data webpage](https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Inpatient2011.html)
* Select the link for "Inpatient Charge Data, FY2011, Comma Separated Values (CSV) version"
* This will prompt you to download "Inpatient_Data_2011_CSV.zip"
* Unzip this file:
```bash
unzip Inpatient_Data_2011_CSV.zip
```
* This will extract a PDF file and a CSV data file named "Medicare_Provider_Charge_Inpatient_DRG100_FY2011.csv"

###### Medicare 2012 data
* Go to the [data webpage](https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Inpatient2012.html)
* Select the link for "Inpatient Charge Data, FY2012, Comma Separated Values (CSV) version"
* This will prompt you to download "Inpatient_Data_2012_CSV.zip"
* Unzip this file:
```bash
unzip Inpatient_Data_2012_CSV.zip
```
* This will extract a PDF file and a CSV data file named "Medicare_Provider_Charge_Inpatient_DRG100_FY2012.csv"

###### Medicare 2013 data
* Go to the [data webpage](https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Inpatient2013.html)
* Select the link for "Inpatient Charge Data, FY2013, Comma Separated Values (CSV) version"
* This will prompt you to download "Inpatient_Data_2013_CSV.zip"
* Unzip this file:
```bash
unzip Inpatient_Data_2013_CSV.zip
```
* This will extract a CSV data file named "Medicare_Provider_Charge_Inpatient_DRG100_FY2013.csv"

###### USDA food environment atlas data
* Go to the [data webpage](http://www.ers.usda.gov/data-products/food-environment-atlas/data-access-and-documentation-downloads.aspx)
* In the "Data Set" column, under "Current Version", select the "Data Download" link (last updated 8/19/2015)
* This will prompt you to download a Microsoft Excel file named "DataDownload.xls"
* After opening the file, you can find the restaurant data in the "RESTAURANTS" tab

