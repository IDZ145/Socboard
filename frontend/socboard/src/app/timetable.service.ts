import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Rx';
import { Departure }  from './departure';

@Injectable()
export class TimetableService {
    constructor (private http: Http) { }

    private apiUrl: string = "http://localhost:5000/";

    getTimetableHighSt(): Observable<JSON> {
        return this.http.get(this.apiUrl + "getbuseshighst")
            .map((res: Response) => res.json())
            .catch ((error: any) => Observable.throw(error.json().error || 'Server error'));
    }
}
