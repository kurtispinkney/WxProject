# WxProject
This is a project that aims to associate various weather phenomenon with their respective storm by relating disparate weather datasets. The end goal would be to create an API interface that end users (students, researchers, etc.) can use to pull storm relative datasets made publicily available through the NOAA Big Data Project, but is largely serving as a means for me to explore AWS services. 

## Table of Contents
1. [Data](#data)
2. [Technology](#technology)
3. [Methodology](#methodology)

## Data
NOAA has provided a wealth of data in an [AWS data registry](https://registry.opendata.aws/) as part of the [NOAA Big Data Project](https://www.noaa.gov/big-data-project). To start I'll work with GOES16 Global Lightning Mapper (GLM) data to relate flashes to their parent storm identified using NEXRAD L2 data.

* [GLM](https://registry.opendata.aws/noaa-goes/)
* [NEXRAD L2](https://registry.opendata.aws/noaa-nexrad/)

## Technology
* [Py-ART](http://arm-doe.github.io/pyart/)
* [TINT](https://github.com/openradar/TINT)
* Jenkins
* PostgreSQL
* Amazon Web Services

## Development
### Explore the data
1. Gain better understanding of what is contained in a GLM file
2. Explore NEXRAD data
  * Generate static ancillary file of radar locations
3. Play with TINT
  * [Read methodology](https://journals.ametsoc.org/doi/abs/10.1175/1520-0426(1993)010%3C0785:TTITAA%3E2.0.CO;2)
  * Understand better how to capture cell identification information
  
### Design the database
1. Develop a database model that relates GLM data to NEXRAD data and storm cells identified by TINT.

### Populate the database
1. Archived data
  * Run a job that will populate the database with historical data
2. Near-real time data
  * Develop executables to be used in AWS Lambda function to update database
  * Want a separate executable for GLM and NEXRAD data
  * Storm identification will be contained within NEXRAD executable 
