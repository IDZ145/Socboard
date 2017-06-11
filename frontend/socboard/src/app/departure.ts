
export class Departure {
    route_id: string;
    stop_name: string;
    stop_location_coords: number[];
    planned_depart_time: Date;
    estimated_depart_time: Date;
    description: string;
    crowded_level: number;
}
