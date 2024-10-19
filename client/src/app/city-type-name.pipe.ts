import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'cityTypeName'
})
export class CityTypeNamePipe implements PipeTransform {

  // Map numeric values to CityType names
  transform(value: number): string {
    switch (value) {
      case 1:
        return 'LOW';
      case 2:
        return 'HIGH';
      default:
        return 'Unknown';
    }
  }
}