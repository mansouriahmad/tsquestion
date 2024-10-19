from enum import Enum
from datetime import datetime, timedelta
from compensation_type import CompensationType
from city_type import CityType

def to_datetime(date_str):
  """
  Converts a date string in the format "mm/dd/yyyy" to a datetime object.

  Args:
    date_str: The date string to convert.

  Returns:
    A datetime object representing the parsed date.
  """
  return datetime.strptime(date_str, "%m/%d/%Y")


def return_compensations_by_date(set):
  """
  Calculates compensation based on a list of projects.

  Args:
    projects (list): A list of tuples, where each tuple represents a project.
      The tuple should contain three elements:
      - `CityType`: The type of city for the project.
      - `start_date_str`: The start date of the project in the format "mm/dd/yyyy".
      - `end_date_str`: The end date of the project in the format "mm/dd/yyyy".
  """
  sorted_set = sorted(set, key=lambda x: (to_datetime(x[1]), to_datetime(x[2])))
  
  compensation_by_date = {}
  
  for project in sorted_set:
    
    city_type, start_date_str, end_date_str = project
    start_date = to_datetime(start_date_str)
    end_date = to_datetime(end_date_str)

    current_date = start_date

    while current_date <= end_date:
      is_start_day = current_date == start_date
      is_end_day = current_date == end_date

      if is_start_day:
        day_before_project_start = current_date - timedelta(days=1)

        if current_date not in compensation_by_date:
          if day_before_project_start in compensation_by_date: #We don't have a gap between this project and previous projects (so far)
            compensation_by_date[day_before_project_start] = compensation_by_date[day_before_project_start].convert_to_full()
            compensation_by_date[current_date] = city_type.get_full_day_compensation()
          else:
            compensation_by_date[current_date] = city_type.get_travel_compensation()
        else: # There is a overlap
          default_start_compensation_type = city_type.get_travel_compensation()
          compensation_by_date[current_date] = compensation_by_date.get(current_date, CompensationType.ZERO) + default_start_compensation_type
      elif not is_end_day:
        default_start_compensation_type = city_type.get_full_day_compensation()
        compensation_by_date[current_date] = compensation_by_date.get(current_date, CompensationType.ZERO) + default_start_compensation_type
      else:
        default_start_compensation_type = city_type.get_travel_compensation()
        compensation_by_date[current_date] = compensation_by_date.get(current_date, CompensationType.ZERO) + default_start_compensation_type
      
      current_date = current_date + timedelta(days=1)
  
  return compensation_by_date

def main():
    # Define your sets
    set_1 = [(CityType.LOW, "09/01/2015", "09/03/2015")]
    set_2 = [
        (CityType.LOW, "09/01/2015", "09/01/2015"),
        (CityType.HIGH, "09/02/2015", "09/06/2015"),
        (CityType.LOW, "09/06/2015", "09/08/2015")
    ]
    set_3 = [
        (CityType.LOW, "09/01/2015", "09/03/2015"),
        (CityType.HIGH, "09/05/2015", "09/07/2015"),
        (CityType.LOW, "09/08/2015", "09/08/2015")
    ]
    set_4 = [
        (CityType.LOW, "09/01/2015", "09/01/2015"),
        (CityType.LOW, "09/01/2015", "09/01/2015"),
        (CityType.HIGH, "09/02/2015", "09/02/2015"),
        (CityType.HIGH, "09/02/2015", "09/03/2015")
    ]
    set_5 = [
        (CityType.LOW, "09/01/2015", "09/02/2015"),
        (CityType.HIGH, "09/02/2015", "09/04/2015"),
        (CityType.HIGH, "09/06/2015", "09/06/2015")
    ]
    set_6 = [
        (CityType.HIGH, "09/01/2015", "09/03/2015"),
        (CityType.LOW, "09/05/2015", "09/05/2015")
    ]

    # Combine sets into a list
    sets = [set_1, set_2, set_3, set_4, set_5, set_6]

    # Iterate over each set
    for index, current_set in enumerate(sets):
        compensation_by_date = return_compensations_by_date(current_set)

        print(f"Compensations for Set {index + 1}:")
        for date, compensation in compensation_by_date.items():
            print(f"Date: {date}, Compensation: {compensation.name}")

        total_compensation = sum(compensation.value for compensation in compensation_by_date.values())
        print("Total Compensation for this set is:", total_compensation)
        print("=======================================================================")

if __name__ == "__main__":
    main()