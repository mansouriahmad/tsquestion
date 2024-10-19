from enum import Enum

class CompensationType(Enum):
  """
  Represents compensation rates based on city type and day type.

  - **LOW_TRAVEL:** Compensation for a travel day in a low-cost city (45).
  - **HIGH_TRAVEL:** Compensation for a travel day in a high-cost city (55).
  - **LOW_FULL:** Compensation for a full day in a low-cost city (75).
  - **HIGH_FULL:** Compensation for a full day in a high-cost city (85).
  """
  ZERO = 0
  LOW_TRAVEL = 45
  HIGH_TRAVEL = 55
  LOW_FULL = 75
  HIGH_FULL = 85

  def __add__(self, other):
    """
    Adds two `CompensationType` instances together to determine the combined type.

    Args:
        other (CompensationType): The `CompensationType` instance to add.

    Returns:
        CompensationType: The combined `CompensationType` based on the sum of the values.
        `NotImplemented` if `other` is not a `CompensationType` instance.
    """
    if isinstance(other, CompensationType):
      if other == CompensationType.ZERO:
        return self
      elif self == CompensationType.ZERO:
        return other
      return CompensationType.LOW_FULL if self.value + other.value in [90, 120] else CompensationType.HIGH_FULL
    return NotImplemented
  
  def convert_to_full(self):
    """
    Converts the current `CompensationType` instance to a full-day equivalent.

    If the current `CompensationType` is already `HIGH_FULL` or `LOW_FULL`, it returns the current value.
    Otherwise, it adds the current value to itself to obtain the full-day equivalent.

    Returns:
      CompensationType: The full-day equivalent of the current `CompensationType`.
    """
    return self + self if self not in [CompensationType.HIGH_FULL, CompensationType.LOW_FULL] else self
