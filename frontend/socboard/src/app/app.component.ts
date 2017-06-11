import { Component, OnInit } from '@angular/core';
import { TimetableService } from './timetable.service'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
    constructor (private timetableService: TimetableService) { }
    title: string = 'Socboard';
    timetableHighSt: JSON = null;

    ngOnInit(): void {
        this.getTimetableHighSt();
    }

    getTimetableHighSt(): void {
        this.timetableService.getTimetableHighSt().subscribe(res => {
            this.timetableHighSt = res;
            console.log("Response: " + this.timetableHighSt);
        });
    }

    timetableHighStToHtml(): string {
        if (this.timetableHighSt != null) {
            return JSON.stringify(this.timetableHighSt);
        }
        return "";
    }
}
