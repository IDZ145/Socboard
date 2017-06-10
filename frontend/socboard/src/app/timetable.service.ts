import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Rx';
import { Departure }  from './departure';

@Injectable()
export class TimetableService {
    constructor (private http: Http) { }

    private apiUrl: string = "http://localhost:5000";

    getTimes(): Observable<Departure[]> {
        return this.http.get(this.apiUrl + "getbuseshighstreet")
            .map((res: Response) => this.jsonToDeparture(res.json()))
            .catch ((error: any) => Observable.throw(error.json().error || 'Server error'));
    }

    jsonToDeparture(json: JSON): Departure[] {
        return null;
    }
}
