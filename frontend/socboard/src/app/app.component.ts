import { Component } from '@angular/core';
import { TimetableService } from './timetable.service'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
    constructor (private timetableService: TimetableService) { }
    title = 'Socboard';

    getTimetable() {
        return this.timetableService.getTimes();
    }
}
