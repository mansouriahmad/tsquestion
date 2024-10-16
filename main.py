from enum import Enum
from datetime import datetime

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

def to_datetime(date_str):
  return datetime.strptime(date_str, "%m/%d/%y")

set_1 = [(CityType.HIGH, "9/1/15", "9/3/15")]
set_2 = [(CityType.LOW, "9/1/15", "9/1/15"), 
        (CityType.HIGH, "9/2/15", "9/6/15"), 
        (CityType.LOW, "9/6/15", "9/8/15")]

set_3 = [(CityType.LOW, "9/1/15", "9/3/15"), 
        (CityType.HIGH, "9/5/15", "9/7/15"), 
        (CityType.HIGH, "9/8/15", "9/8/15")]

set_4 = [(CityType.LOW, "9/1/15", "9/1/15"), 
        (CityType.LOW, "9/1/15", "9/1/15"), 
        (CityType.HIGH, "9/2/15", "9/2/15"), 
        (CityType.HIGH, "9/2/15", "9/3/15")]

sets = [set_1, set_2, set_3, set_4]

projects = [
            (CityType.LOW, "9/1/15", "9/3/15"),
            (CityType.HIGH, "9/2/15", "9/6/15"),
            (CityType.LOW, "9/6/15", "9/8/15"),
            (CityType.HIGH, "9/1/15", "9/4/15"),
            (CityType.LOW, "9/1/15", "9/2/15"),
          ]

for set in sets:
  sorted_set = sorted(set, key=lambda x: (to_datetime(x[1]), to_datetime(x[2])))

for project in sorted_set:
  print(project)
print("----------------------------" )


A = CompensationType.HIGH_FULL
B = CompensationType.HIGH_TRAVEL
C = CompensationType.LOW_FULL
D = CompensationType.LOW_TRAVEL

for item1 in [A,B,C,D]:
  for item2 in [A,B,C,D]:
    print(item1, item2, item1 + item2)