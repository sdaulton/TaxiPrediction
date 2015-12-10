from pyspark.sql.types import *
#from pyspark.sql import *

def getYellowCabSchema():
	yCabHeader = "cab_company,vendor_id,pickup_datetime,dropoff_datetime,passenger_count,trip_distance,pickup_longitude,pickup_latitude,rate_code_id,store_and_fwd_flag,dropoff_longitude,dropoff_latitude,payment_type,fare_amount,extra,mta_tax,tip_amount,tolls_amount,improvement_surcharge,total_amount"

	#schemaString = header
	fields = [StructField(field_name, StringType(), True) for field_name in yCabHeader.split(',')]
	print "# of columns: ", len(fields)

	#cab_company: StringType (i.e. no change reqd)

	#vendor_id: StringType (i.e. no change reqd)

	#tpep_pickup_datetime
	fields[2].dataType = TimestampType()

	#tpep_dropoff_datetime
	fields[3].dataType = TimestampType()

	#passenger_count
	fields[4].dataType = IntegerType()

	#trip_distance
	fields[5].dataType = FloatType()

	#pickup_longitude
	fields[6].dataType = FloatType()	

	#pickup_latitude
	fields[7].dataType = FloatType()	

	#RateCodeID: StringType (i.e. no change reqd)
	#store_and_fwd_flag: StringType (i.e. no change reqd)

	#dropoff_longitude
	fields[10].dataType = FloatType()

	#dropoff_latitude
	fields[11].dataType = FloatType()

	#payment_type : StringType (i.e. no change reqd)

	#fare_amount
	fields[13].dataType = FloatType()

	#extra
	fields[14].dataType = FloatType()

	#mta_tax
	fields[15].dataType = FloatType()

	#tip_amount
	fields[16].dataType = FloatType()

	#tolls_amount
	fields[17].dataType = FloatType()

	#improvement_surcharge
	fields[18].dataType = FloatType()

	#total_amount
	fields[19].dataType = FloatType()

	yCabSchema = StructType(fields)
	return yCabSchema

def getGreenCabSchema():
	gCabHeader = "cab_company,vendor_id,pickup_datetime,dropoff_datetime,store_and_fwd_flag,rate_code_id,pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude,passenger_count,trip_distance,fare_amount,extra,mta_tax,tip_amount,tolls_amount,ehail_fee,improvement_surcharge,total_amount,payment_type,trip_type"

	#schemaString = header
	fields = [StructField(field_name, StringType(), True) for field_name in gCabHeader.split(',')]
	print "# of columns: ", len(fields)

	#cab_company: StringType (i.e. no change reqd)

	#vendor_id: StringType (i.e. no change reqd)

	#pickup_datetime
	fields[2].dataType = TimestampType()

	#dropoff_datetime: 
	fields[3].dataType = TimestampType()

	#store_and_fwd_flag: StringType (i.e. no change reqd): 4

	#rate_code_id: StringType (i.e. no change reqd): 5

	#pickup_longitude
	fields[6].dataType = FloatType()	

	#pickup_latitude
	fields[7].dataType = FloatType()	

	#dropoff_longitude
	fields[8].dataType = FloatType()

	#dropoff_longitude
	fields[9].dataType = FloatType()

	#passenger_count
	fields[10].dataType = IntegerType()

	#trip_distance
	fields[11].dataType = FloatType()

	#fare_amount
	fields[12].dataType = FloatType()

	#extra
	fields[13].dataType = FloatType()

	#mta_tax
	fields[14].dataType = FloatType()

	#tip_amount
	fields[15].dataType = FloatType()

	#tolls_amount
	fields[16].dataType = FloatType()

	#ehail_fee
	fields[17].dataType = FloatType()

	#improvement_surcharge
	fields[18].dataType = FloatType()

	#total_amount
	fields[19].dataType = FloatType()

	#payment_type: StringType (i.e. no change reqd)

	#trip_type: StringType (i.e. no change reqd)

	gCabSchema = StructType(fields)
	
	return gCabSchema