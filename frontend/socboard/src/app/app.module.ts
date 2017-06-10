import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { TimetableService } from './timetable.service';
import { Departure } from './departure';

import {
    MdToolbarModule,
    MdCheckboxModule,
    MdGridListModule,
    MdCardModule } from '@angular/material';
@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    MdToolbarModule,
    MdCheckboxModule,
    MdGridListModule,
    MdCardModule,
  ],
  providers: [
      TimetableService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
