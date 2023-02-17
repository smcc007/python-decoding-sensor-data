# Runner script for all modules
from datetime import date, datetime
from load_data import load_sensor_data
from house_info import HouseInfo


##############################
# Do not remove these two lines
# They are needed to validate your unittest
data = []
print("Sensor Data App")
##############################

# Module 1 code here:
data = load_sensor_data()
print(f'Loaded records {len(data)}')
# Module 2 code here:

# Module 3 code here:

# Module 4 code here:

# Module 5 code here:

house_info = HouseInfo(data)

#TEST the area filter
test_area = 1
recs = house_info.get_data_by_area("id", rec_area=test_area)

print(f"Number of sensor records picked up for area {test_area} is {len(recs)}")

#test the date filter
test_date = datetime.strptime("5/9/20", "%m/%d/%y")
recs = house_info.get_data_by_date("id", rec_date=test_date)

print(f"Number of sensor records picked on {test_date.strftime('%m/%d/%y')} is {len(recs)}")

