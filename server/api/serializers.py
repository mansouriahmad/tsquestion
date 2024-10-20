from rest_framework import serializers
from models.city_type import CityType
from datetime import datetime

class ProjectSerializer(serializers.Serializer):
    cityType = serializers.IntegerField()
    startDate = serializers.CharField()  # Keep as CharField to manually handle date parsing
    endDate = serializers.CharField()    # Keep as CharField to manually handle date parsing

    def validate(self, data):
        """
        Custom validation for the dates to handle %m/%d/%Y format.
        """
        try:
            # Parse startDate in %m/%d/%Y format
            data['startDate'] = datetime.strptime(data['startDate'], "%m/%d/%Y")
        except ValueError:
            raise serializers.ValidationError("Start date must be in the format MM/DD/YYYY.")

        try:
            # Parse endDate in %m/%d/%Y format
            data['endDate'] = datetime.strptime(data['endDate'], "%m/%d/%Y")
        except ValueError:
            raise serializers.ValidationError("End date must be in the format MM/DD/YYYY.")

        return data