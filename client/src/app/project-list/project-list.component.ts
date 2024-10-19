import { Component } from '@angular/core';
import { CityType, Project } from 'src/models/project.model';

@Component({
  selector: 'app-project-list',
  templateUrl: './project-list.component.html',
  styleUrls: ['./project-list.component.css']
})
export class ProjectListComponent {
  projects: Project[] = [];
  showDialog = false;

  newProject: Project = {
    cityType: CityType.LOW,
    startDate: '',
    endDate: ''
  };

  CityType = CityType; // Expose enum to the template

  // Opens the dialog
  openAddProjectDialog() {
    this.showDialog = true;
  }

  // Closes the dialog without saving
  closeDialog() {
    this.showDialog = false;
  }

  formatDateToMMDDYYYY(date: string): string {
    const [year, month, day] = date.split('-'); // Split the date into year, month, day (input type="date" returns yyyy-mm-dd)
    return `${month}/${day}/${year}`;
  }

  addProject() {
    if (this.newProject.startDate && this.newProject.endDate) {
      this.projects.push({
        cityType: this.newProject.cityType,  // store numeric value (1 for LOW, 2 for HIGH)
        startDate: this.formatDateToMMDDYYYY(this.newProject.startDate),
        endDate: this.formatDateToMMDDYYYY(this.newProject.endDate),
      });
      this.resetNewProject();
      this.closeDialog();
    }
  }


  // Resets the new project form
  resetNewProject() {
    this.newProject = {
      cityType: CityType.LOW,
      startDate: '',
      endDate: ''
    };
  }

  // Deletes a project
  deleteProject(index: number) {
    this.projects.splice(index, 1);
  }

  // Clears all projects
  clearProjects() {
    this.projects = [];
  }

  // Submits the projects to the backend
  submitProjects() {
    // Perform your HTTP POST here to send data to Django
    console.log(this.projects);
  }
}
