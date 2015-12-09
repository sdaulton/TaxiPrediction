# NYC Taxi Data Prediction: Harvard CS109 project


![image](https://github.com/sdaulton/TaxiPrediction/raw/master/images/Actual-Predicted.gif)

The above image shows the predicted number of pickups on a given Monday using a random forest regressor on the the left and the actual number of pickups on the right.  The sheet number at the top of each image corresponds to the hour of the day.

## A NYC icon: the yellow taxicab

New York City, being the most populous city in the United States, has a vast and complex transportation system, including one of the largest subway systems in the world and a large fleet of more than 13,000 yellow and green taxis, that have become iconic subjects in photographs and movies.

The subway system digests the lion share of NYC's public transport use, but the 54% of NYC's residents that don't own a car and therefore rely on public transportation still take almost 200 million taxi trips per year!

## 440 million taxi trips

Thanks to some FOIL requests, data about these taxi trips has been available to the public since last year, making it a data scientist's dream. We endeavoured to delve into this gold mine using 2.5 years of NYC taxi trip data - around 440 million records - going from January 2013 to June 2015.

## Predicting pickup density

The prime objective we had in this project was to predict the density of taxi pickups throughout New York City as it changes from day to day and hour to hour.

So, given a specific location, date and time, can we  predict the number of pickups in that location to a reasonably high accuracy?

## To make transportation more efficient

1. **Taxi companies**: Companies can maximize their utilization by diverting the cabs into the locations during specific times
2. **Traffic planning**: Planners can use the model predictions for traffic management on specific day/time/locations. The model can be enhanced in future to incorporate features like weather, holiday etc.
3. **Data scientists**: It is interesting for data scientist to see how we have modeled location data in a simple way and yet able to get reasonably good predictions

## Our Approach

### 1. Data preparation with Apache Spark on a Amazon Web Services Cluster


* We used AWS to setup a 5 node Spark cluster (each machine had 8 cores, 16 GB RAM), and configured the cluster setup to leverage maximum resources by Spark.
* We especially used the cluster to load the 60+ GB of raw data into an Amazon S3 bucket, and to process and prepare the data for input into the Machine Learning algorithm.

#### Data cleansing: 
* We had to parse 440 million records and remove dirty records (e.g. nulls, invalid geographical coordinates, etc.)
* Feature extraction:
  * Location features: We used geohashing to discretize the location data. This is very important because we were able to adjust the granularity of the precision of the location (different size of rectangles) - and make predictions on these locations.
  * We also added additional features like cosine & sine on some of the data fields (more information in our notebooks)
  * We grouped the entire dataset by time of the day(binned), day of the week & location (geohash).

### 2.  Exploratory data analysis
* The data is currently available in Google BigQuery, which allowed us to explore the data directly in Tableau.

### 3. Machine learning (Pandas/Scikit learn)
* We used Random Forest based regression
* The main features we used were
  * discretized latitude/longitude (derived back from geohashes)
  * discretized time - but encoded in 0 to 1
  * other features: number of pickups, day of week etc
* The model performed very well with a RMSE on test data of 0.9505: we attribute this success to how we modeled the data - and importantly to how the Random Forest algorithm is able to capture the complexities in the above features and come out with a great predictor.

### 4. The Project Team
* [Samuel Daulton](http://github.com/sdaulton)
* [Sethu Raman](http://github.com/rsethur)
* [Tijl Kindt](http://github.com/tijlk)

### 5. Citations/Credit/References
1. Thanks to Harvard CS109 TF's: [Rahul Dave](https://github.com/rahuldave) & Team: we used parts of their code in multiple places: (a) Cluster setup in AWS (b) Machine learning
2. [Geohash.py](https://github.com/hkwi/python-geohash): A nice geohash library
