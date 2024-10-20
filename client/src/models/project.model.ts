export enum CityType {
  LOW = 1,
  HIGH = 2
}

export interface Project {
  cityType: CityType,
  startDate: string,
  endDate: string
}

export interface SubmitProjectResponse {
  result: number
}