from compensation_type import CompensationType
from enum import Enum

class CityType(Enum):
  """
  Represents the type of city based on cost.

  - LOW: Indicates a low-cost city.
  - HIGH: Indicates a high-cost city.
  """
  LOW = 1
  HIGH = 2

  def get_travel_compensation(self):
      """
      Returns the travel day compensation type based on the city type.
      """
      if self == CityType.LOW:
          return CompensationType.LOW_TRAVEL
      elif self == CityType.HIGH:
          return CompensationType.HIGH_TRAVEL

  def get_full_day_compensation(self):
      """
      Returns the full day compensation type based on the city type.
      """
      if self == CityType.LOW:
          return CompensationType.LOW_FULL
      elif self == CityType.HIGH:
          return CompensationType.HIGH_FULL

