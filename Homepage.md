# NYC Taxi Data Prediction: Harvard CS109 project

Welcome to our Data Science project page. 

![image](https://github.com/sdaulton/TaxiPrediction/raw/master/images/Actual-Predicted.gif)

The above image shows the Actual Vs Predicted number of pickups at different locations & times during any given Monday

## 1. What we did
1. We analyzed around 2.5 years of NYC taxi trip data - around 440 million records. We used spark to pre-process and cleanse the data, and ran our machine learning models. 
2. We wanted to answer the question : **"Given a specific location, day of the week, and time slot, can we  predict the number of pickups?"**. And **we were able to perform this prediction with a reasonably high accuracy**: our RMSE on test data was 0.9505

## 2. Why it is interesting
1. Taxi companies: Companies can maximize their utilization by diverting the cabs into the locations during specific times
2. Traffic planning: Planners can use the model predictions for traffic management on specific day/time/locations. The model can be enhanced in future to incorporate features like weather, holiday etc.
3. Data scientists: It is interesting for data scientist to see how we have modeled location data in a simple way and yet able to get reasonably good predictions

## 3. How we did

### 3.1 Cluster setup & software tools/frameworks used
* We used AWS to setup a 5 node Spark cluster (each machine had 8 cores, 16 GB RAM). We also configured the cluster setup to leverage maximum resources by Spark.
* We loaded our data (60+ GB) into S3 in amazon.

### 3.2 Data prep (using Apache Spark)
* Data cleansing: We had to parse 440 million records and remove dirty records (e.g. nulls, invalid lat/long etc)
* Feature extraction
  * Location features: We used geohashing to discretize the location data. This is very important because we were able to adjust the granularity of the precision of the location (different size of rectangles) - and make predictions on these locations.
  * We also added additional features like cosine & sine on some of the data fields (more information in our notebooks)
  * We grouped the entire dataset by time of the day(binned), day of the week & location (geohash).

### 3.3 Exploratory data analysis
* Our exploratory data analysis was primarily done using Tableau

### 3.4 Machine learning (Pandas/Scikit learn)
* We used Random Forest based regression
* The main features we used were
  * discretized latitude/longitude (derived back from geohashes)
  * discretized time - but encoded in 0 to 1
  * other features: number of pickups, day of week etc
* The model performed very well with a RMSE on test data of 0.9505: we attribute this success to how we modeled the data - and importantly to how the Random Forest algorithm is able to capture the complexities in the above features and come out with a great predictor.

### 4. The Project Team
* Samuel Daulton
* Sethu Raman
* Tijl Kind


## 5. Citations/Credit/References
1. Thanks to Harvard CS109 TF's: [Rahul Dave](https://github.com/rahuldave) & Team: we used parts of their code in multiple places: (a) Cluster setup in AWS (b) Machine learning
2. [Geohash.py](https://github.com/hkwi/python-geohash): A nice geohash library
