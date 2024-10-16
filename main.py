from enum import Enum
from datetime import datetime, timedelta

class CityType(Enum):
  LOW = 1
  HIGH = 2

class CompensationType(Enum):
  LOW_TRAVEL = 45
  HIGH_TRAVEL = 55
  LOW_FULL = 75
  HIGH_FULL = 85

  # Define the addition method
  def __add__(self, other):
    if isinstance(other, CompensationType):
      if other.value + self.value == 120 or other.value + self.value == 90:
        return CompensationType.LOW_FULL
      return CompensationType.HIGH_FULL
    return NotImplemented
  
  def convert_to_full(self):
    if self != CompensationType.HIGH_FULL and self != CompensationType.LOW_FULL:
      return self + self
    return self

def to_datetime(date_str):
  return datetime.strptime(date_str, "%m/%d/%Y")


def calculate_compensation(set):
  sorted_set = sorted(set, key=lambda x: (to_datetime(x[1]), to_datetime(x[2])))
  
  days_record = {}
  
  for project in sorted_set:
    # print(project)
    city_type, start_date_str, end_date_str = project
    start_date = to_datetime(start_date_str)
    end_date = to_datetime(end_date_str)


    current_date = start_date
    while current_date <= end_date:
      if current_date == start_date:
        day_before_project_start = current_date - timedelta(days=1)

        if day_before_project_start in days_record: #We don't have a gap
          cur_val = days_record[day_before_project_start]
          full_val = cur_val.convert_to_full()
          days_record[day_before_project_start] = full_val

          default_start_compensation_type = CompensationType.HIGH_FULL if city_type == CityType.HIGH else CompensationType.LOW_FULL
          days_record[current_date] = default_start_compensation_type if current_date not in days_record else default_start_compensation_type + days_record[current_date]
        else: # There is a gap
          default_start_compensation_type = CompensationType.HIGH_TRAVEL if city_type == CityType.HIGH else CompensationType.LOW_TRAVEL
          days_record[current_date] = default_start_compensation_type if current_date not in days_record else default_start_compensation_type + days_record[current_date]
      elif current_date != end_date:
        default_start_compensation_type = CompensationType.HIGH_FULL if city_type == CityType.HIGH else CompensationType.LOW_FULL
        days_record[current_date] = default_start_compensation_type if current_date not in days_record else default_start_compensation_type + days_record[current_date]
      else:
        default_start_compensation_type = CompensationType.HIGH_TRAVEL if city_type == CityType.HIGH else CompensationType.LOW_TRAVEL
        days_record[current_date] = default_start_compensation_type if current_date not in days_record else default_start_compensation_type + days_record[current_date]
      current_date = current_date + timedelta(days=1)
  print(days_record)
  print("------------------")


set_1 = [(CityType.LOW, "09/01/2015", "09/03/2015")]
set_2 = [(CityType.LOW, "09/01/2015", "09/01/2015"), 
        (CityType.HIGH, "09/02/2015", "09/06/2015"), 
        (CityType.LOW, "09/06/2015", "09/08/2015")]

set_3 = [(CityType.LOW, "09/01/2015", "09/03/2015"), 
        (CityType.HIGH, "09/05/2015", "09/07/2015"), 
        (CityType.HIGH, "09/08/2015", "09/08/2015")]

set_4 = [(CityType.LOW, "09/01/2015", "09/01/2015"), 
        (CityType.LOW, "09/01/2015", "09/01/2015"), 
        (CityType.HIGH, "09/02/2015", "09/02/2015"), 
        (CityType.HIGH, "09/02/2015", "09/03/2015")]

sets = [set_1, set_2, set_3, set_4]
# sets = [set_4]


for set in sets:
  calculate_compensation(set)


