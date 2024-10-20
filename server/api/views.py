from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
from datetime import datetime, timedelta
from models.compensation_type import CompensationType
from models.city_type import CityType



def to_datetime(date_str):
  """
  Converts a date string in the format "mm/dd/yyyy" to a datetime object.

  Args:
    date_str: The date string to convert.

  Returns:
    A datetime object representing the parsed date.
  """
  return datetime.strptime(date_str, "%m/%d/%Y")


def return_compensations(set):
  """
  Calculates compensation based on a list of projects.

  Args:
    projects (list): A list of tuples, where each tuple represents a project.
      The tuple should contain three elements:
      - `CityType`: The type of city for the project.
      - `start_date_str`: The start date of the project in the format "mm/dd/yyyy".
      - `end_date_str`: The end date of the project in the format "mm/dd/yyyy".
  """
  sorted_set = sorted(set, key=lambda x: (x[1], x[2]))
  
  compensation_by_date = {}
  
  for project in sorted_set:
    
    city_type, start_date, end_date = project

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
  
  total_compensation = sum(compensation.value for compensation in compensation_by_date.values())
  return total_compensation


@api_view(['POST'])
def submit_projects(request):
    serializer = ProjectSerializer(data=request.data, many=True)
    if serializer.is_valid():
      formatted_data = []
      for project in serializer.validated_data:
        print(project['startDate'])
        city_type = CityType(project['cityType'])  # Convert integer to CityType enum
        print(city_type)
        formatted_data.append((city_type, project['startDate'], project['endDate']))

      total = return_compensations(formatted_data)
      # total = sum([project['cityType'] for project in serializer.validated_data])
      return Response({"result": total})  # Example: return total of cityType values
    return Response(serializer.errors, status=400)