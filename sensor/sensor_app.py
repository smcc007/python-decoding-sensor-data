# Runner script for all modules
from datetime import date, datetime
from load_data import load_sensor_data
from house_info import HouseInfo
from temperature_info import TemperatureData
from humidity_info import HumidityData
from statistics import mean


##############################
# Do not remove these two lines
# They are needed to validate your unittest
data = []
print("Sensor Data App")
##############################

# Module 1 code here:
data = load_sensor_data()
print(f'Loaded records {len(data)}')

#test the date filter
test_date = datetime.strptime("5/9/20", "%m/%d/%y")
test_area = 1

# Module 2 code here:



# Module 3 code here:
house_info = HouseInfo(data)
recs = house_info.get_data_by_area("id", rec_area=test_area)
print(f"Number of sensor records picked up for area {test_area} is {len(recs)}")

recs = house_info.get_data_by_date("id", rec_date=test_date)
print(f"Number of sensor records picked on {test_date.strftime('%m/%d/%y')} is {len(recs)}")
# Module 4 code here:
temperature_data = TemperatureData(data)
recs = temperature_data.get_data_by_area(rec_area=test_area)

print(f"The house temperature sensor records for area: {test_area} is {len(recs)}")
print(f"The Maximum temp is {max(recs)} and the minimum temp is {min(recs)}")

recs = temperature_data.get_data_by_date(rec_date=test_date)
print(f"The house temperature sensor records for temperature: {test_date.strftime('%m/%d/%y')} is {len(recs)}")
print(f"The Maximum temp is {max(recs)} and the minimum temp is {min(recs)}")

# Module 5 code here:
humidity_data = HumidityData(data)
recs = humidity_data.get_data_by_area(rec_area=test_area)

print(f"The humidity sensor has picked up {len(recs)} for a test area of {test_area}")
print(f"The average humidity is {mean(recs)}")

recs = humidity_data.get_data_by_date(rec_date=test_date)
print(f"The humidity sensor has picked up {len(recs)} for a test date of {test_date.strftime('%m/%d/%y')}")
print(f"The average humidity is {mean(recs)}")



