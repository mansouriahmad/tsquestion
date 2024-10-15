from enum import Enum
from datetime import datetime

class CityType(Enum):
    LOW = 1
    HIGH = 2

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
  print("----------------------------")