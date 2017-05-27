# Socboard
## Objective
A dashboard for Socs office. 
Core features:
* Bus notifier
* Next bus to Central
* Next bus to Town Hall
* Estimated patronage/queue for both (we can use passenger data)
* Latest news from CSESoc (e.g. events, news, Beta)
* Dev team job listings
 
Extensions:
* Is Socs Open integration
* Miracast/Spotify cast support (will need to be separate application)

## Components
Frontend - Weilon:
* Display and format stuff using API calls to backend
* Make it look good
Backend - Inura: 
* Get data from various sources and process it
* Create set of API endpoints that frontend can call upon
Raspberry Pi:
* Display Socboard to Socs Office TV
