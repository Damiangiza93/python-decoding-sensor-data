from load_data import load_sensor_data
from house_info import HouseInfo
from temperature_info import TemperatureData

from datetime import date, datetime
# Runner script for all modules


##############################
# Do not remove these two lines
# They are needed to validate your unittest
data = []
print("Sensor Data App")
##############################

# Module 1 code here:
data = load_sensor_data()
print(f"Loaded records: {len(data)}")

# Module 2 code here:
house_info = HouseInfo(data)
test_area = 1
recs = house_info.get_data_by_area("id", rec_area=test_area)
print(f"\nHouse sensor records for area: {test_area} = {len(recs)}")

test_date = datetime.strptime("5/9/20", "%m/%d/%y")
recs = house_info.get_data_by_date("id", rec_date=test_date)
print(f"House sensor records for date: {test_date.strftime('%m/%d/%y')} = {len(recs)}")

# Module 3 code here:
temperature_data = TemperatureData(data)
recs = temperature_data.get_data_by_area(rec_area=test_area)
print(f"\nHouse Temperature sensor records for area: {test_area} = {len(recs)}")
print(f"\tMaximum: {max(recs)}, Minimum: {min(recs)} temperatures")

recs = temperature_data.get_data_by_date(rec_date=test_date)
print(f"\nHouse Temperature sensor record for date: {test_date.strftime('%m/%d/%y')} = {len(recs)}")
print(f"\tMaximum: {max(recs)}, Minimum: {min(recs)} temperatures")

# Module 4 code here:

# Module 5 code here: