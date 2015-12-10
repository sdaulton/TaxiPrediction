# NYC Taxi Data Prediction

![image](https://github.com/sdaulton/TaxiPrediction/blob/master/figures/2013-24hours.gif)


## The Yellow Taxicab: an NYC Icon

New York City, being the most populous city in the United States, has a vast and complex transportation system, including one of the largest subway systems in the world and a large fleet of more than 13,000 yellow and green taxis, that have become iconic subjects in photographs and movies.

The subway system digests the lion share of NYC's public transport use, but the 54% of NYC's residents that don't own a car and therefore rely on public transportation still take almost 200 million taxi trips per year!

## 440 million taxi trips

Thanks to some FOIL requests, data about these taxi trips has been available to the public since last year, making it a data scientist's dream. We endeavoured to delve into this gold mine using 2.5 years of NYC taxi trip data - around 440 million records - going from January 2013 to June 2015.

### The Data:
* [Raw NYC Taxi Trip Data](http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml) 

## Predicting pickup density

The primary objective of this project was to predict the density of taxi pickups throughout New York City as it changes from day to day and hour to hour.

So, given a specific location, date and time, can we  predict the number of pickups in that location to a reasonably high accuracy?

## To make transportation more efficient

1. **Taxi companies**: Companies can maximize their utilization by diverting the cabs into the locations during specific times
2. **Traffic planning**: Planners can use the model predictions for traffic management on specific day/time/locations. The model can be enhanced in future to incorporate features like weather, holiday etc.
3. **Data scientists**: It is interesting for data scientist to see how we have modeled location data in a simple way and yet able to get reasonably good predictions

## Our Approach

### 1.  Exploratory data analysis
* The data is currently available in Google BigQuery, which allowed us to explore the data directly in Tableau.

#### Number of Pickups in 2013 and 2014
##### throughout the days of the year (horizontal axis) and the hours of the day (vertical axis)
![image](https://github.com/sdaulton/TaxiPrediction/blob/master/figures/pickups-time-heatmap-no-title.jpg)

### 2. Data preparation with Apache Spark on a Amazon Web Services (AWS) Cluster

* We used AWS to setup a 5-node Spark cluster (each machine had 8 cores, 16 GB RAM), and configured the cluster setup to leverage maximum resources by Spark.
* We especially used the cluster to load the 60+ GB of raw data into an Amazon S3 bucket, and to process and prepare the data for input into machine learning algorithms.

#### Data cleansing: ([notebook](https://github.com/sdaulton/TaxiPrediction/blob/master/DataPrepAWSSpark.ipynb))
* We had to parse 440 million records and remove dirty records (e.g. nulls, invalid geographical coordinates, etc.)
* Feature extraction:
  * Location features: We used geohashing to discretize the location data. This is very important because we were able to adjust the granularity of the precision of the location (different size of rectangles) - and make predictions on these locations.
  * We also added additional features like cosine & sine on the time and day of the week fields (see our [notebook](https://github.com/sdaulton/TaxiPrediction/blob/master/DataPrepAWSSpark.ipynb) for more information in our notebooks)
  * We grouped the entire dataset by time of the day(binned), day of the week & location ([geohash](https://github.com/hkwi/python-geohash)).

### 3. Machine learning (Pandas/Scikit learn)
#### Approach 1: Predicting the pickup density for an average day of week and time of day
* We used two models:
  * Random Forest regression: ([notebook](https://github.com/sdaulton/TaxiPrediction/blob/master/Machine%20Learning%20(Random%20Forest).ipynb))
  * k-Nearest Neighbors regression: ([notebook](https://github.com/sdaulton/TaxiPrediction/blob/master/Machine%20Learning%20(kNN).ipynb))
* The main features we used were
  * Discretized latitude/longitude (derived back from geohashes)
  * Discretized time - but encoded in 0 to 1
  * Other features: number of pickups, day of week, etc
* The Random Forest model performed very well with a coefficient of determination (R-squared) on the test data of 0.9505, indicating that variation in the model explains over 95% of the variation in the pickup density distribution.  We attribute this success to:
  * How we modeled the data
  * The abiltiy of the Random Forest algorithm is able to capture the complexities in the above features
 
##### Predicted Density Distribution vs. Actual Density Distribution on a Monday
![image](https://github.com/sdaulton/TaxiPrediction/raw/master/images/Actual-Predicted.gif)

The above image shows the predicted number of pickups on a given Monday using a random forest regressor on the the left and the actual number of pickups on the right.  The sheet number at the top of each image corresponds to the hour of the day.



#### Approach 2: Predicting the pickup density for a specific date and time
* We used Random Forest regression: ([notebook](https://github.com/sdaulton/TaxiPrediction/blob/master/Machine%20Learning%20(Random%20Forest%2C%20train-valid-test).ipynb))



### 4. The Project Team
* [Samuel Daulton](http://github.com/sdaulton)
* [Sethu Raman](http://github.com/rsethur)
* [Tijl Kindt](http://github.com/tijlk)

### 5. Citations/Credit/References
1. Thanks to Harvard CS109 TF's: [Rahul Dave](https://github.com/rahuldave) & Team: we used parts of their code in multiple places: (a) Cluster setup in AWS (b) Machine learning
2. [Geohash.py](https://github.com/hkwi/python-geohash): A nice geohash library
