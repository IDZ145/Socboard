# Socboard
## Objective
A dashboard for Socs office. 
Core features:
* Bus notifier
* Next bus from High Street (towards City)
* Next bus to from Anzac Parade (towards City)
* Estimated patronage/queue for both (we can use passenger data)
* Latest news from CSESoc (e.g. events, news, Beta)
* Dev team job listings
 
Extensions:
* Is Socs Open integration
* Miracast/Spotify cast support (will need to be separate application)
* Next bus from High Street (towards Eastern Suburbs)
* Next bus to from Anzac Parade (towards Eastern Suburbs)

## Components
Frontend - Weilon:
* Display and format stuff using API calls to backend
* Make it look good

Backend - Inura: 
* Get data from various sources and process it
* Create set of API endpoints that frontend can call upon

Raspberry Pi:
* Display Socboard to Socs Office TV
