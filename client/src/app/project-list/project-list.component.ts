import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { CityType, Project, SubmitProjectResponse } from 'src/models/project.model';

@Component({
  selector: 'app-project-list',
  templateUrl: './project-list.component.html',
  styleUrls: ['./project-list.component.css']
})
export class ProjectListComponent {
  projects: Project[] = [];
  showDialog = false;
  totalCompensation: number | null = null;

  constructor(private http: HttpClient) { }

  newProject: Project = {
    cityType: CityType.LOW,
    startDate: '',
    endDate: ''
  };

  CityType = CityType;

  openAddProjectDialog() {
    this.showDialog = true;
  }

  closeDialog() {
    this.showDialog = false;
  }

  formatDateToMMDDYYYY(date: string): string {
    const [year, month, day] = date.split('-');
    return `${month}/${day}/${year}`;
  }

  addProject() {
    const startDate = new Date(this.newProject.startDate);
    const endDate = new Date(this.newProject.endDate);

    if (endDate >= startDate) {
      this.projects.push({
        ...this.newProject,
        startDate: this.formatDateToMMDDYYYY(this.newProject.startDate),
        endDate: this.formatDateToMMDDYYYY(this.newProject.endDate),
      });
      this.resetNewProject();
      this.closeDialog();
    } else {
      console.log('End date must be greater than or equal to the start date.');
      alert('End date must be greater than or equal to the start date.');
    }
  }

  resetNewProject() {
    this.newProject = {
      cityType: CityType.LOW,
      startDate: '',
      endDate: ''
    };
  }

  deleteProject(index: number) {
    this.projects.splice(index, 1);
    this.totalCompensation = null;
  }

  clearProjects() {
    this.projects = [];
    this.totalCompensation = null;
  }

  submitProjects() {
    this.http.post<SubmitProjectResponse>('http://localhost:8000/api/submit-projects', this.projects)
      .subscribe({
        next: (response: SubmitProjectResponse) => {
          this.totalCompensation = response.result
        },
        error: (error) => {
          console.error('Error submitting projects:', error);
          this.totalCompensation = null;
        }
      });
  }
}
