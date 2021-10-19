Train/Test
|Feature|Type|Dataset|Description|
|---|---|---|---|
|**Id**|*int*|test.csv|the id of the record|
|**Date**|*datetime*|train.csv/test.csv|date that the WNV test is performed|
|**Address**|*object*|train.csv/test.csv|approximate address of the location of trap. This is used to send to the GeoCoder.|
|**Species**|*object*|train.csv/test.csv|the species of mosquitos|
|**Block**|*int*|train.csv/test.csv|block number of address|
|**Street**|*object*|train.csv/test.csv|street name|
|**Trap**|*object*|train.csv/test.csv|Id of the trap|
|**AddressNumberAndStreet**|*object*|train.csv/test.csv|approximate address returned from GeoCoder|
|**Latitude**|*float*|train.csv/test.csv|Latitude returned from GeoCoder|
|**Longitude**|*float*|train.csv/test.csv|Longitude returned from GeoCoder|
|**AddressAccuracy**|*int*|train.csv/test.csv|accuracy returned from GeoCoder|
|**NumMosquitos**|*int*|train.csv|number of mosquitoes caught in this trap|
|**WnvPresent**|*int*|train.csv|whether West Nile Virus was present in these mosquitos. 1 means WNV is present, and 0 means not present.|

Spray Data
|Feature|Type|Dataset|Description|
|---|---|---|---|
|**Date**|*datetime*|spray.csv|the date of the spray|
|**Time**|*datetime*|spray.csv|the time of the spray|
|**Latitude**|*float*|spray.csv|Latitude of the spray|
|**Longitude**|*float*|spray.csv|Longitude of the spray|

Weather Data
|Feature|Type|Dataset|Description|
|---|---|---|---|
|**Station**|*int*|weather.csv|Station 1: CHICAGO O'HARE INTERNATIONAL AIRPORT Lat: 41.995 Lon: -87.933 Elev: 662 ft. above sea level <br>Station 2: CHICAGO MIDWAY INTL ARPT Lat: 41.786 Lon: -87.752 Elev: 612 ft. above sea level|
|**Date**|*datetime*|weather.csv|Date of record|
|**Tmax**|*int*|weather.csv|Maximum temperature|
|**Tmin**|*int*|weather.csv|Minimum temperature|
|**Tavg**|*object*|weather.csv|Average temperature|
|**Depart**|*object*|weather.csv|Departure from normal|
|**DewPoint**|*int*|weather.csv|Average dew point: Average temperature air needs to be cooled to in order to achieve relative humidity of 100%|
|**WetBulb**|*object*|weather.csv|Average wet bulb temperature: Average lowest temperature which air can be cooled by evaporation of water into air at constant pressure|
|**Heat**|*object*|weather.csv|Heating degree days|
|**Cool**|*object*|weather.csv|Cooling degree days|
|**Sunrise**|*datetime*|weather.csv|Calculated time of sunrise|
|**Sunset**|*datetime*|weather.csv|Calculated time of sunset|
|**CodeSum**|*object*|weather.csv|Code of weather phenomena|
|**Depth**|*object*|weather.csv|Depth of snow/ice in inches|
|**Water1**|*object*|weather.csv|Water equivalent of depth|
|**SnowFall**|*object*|weather.csv|Snowfall in inches|
|**PrecipTotal**|*object*|weather.csv|Precipitation in inches|
|**StnPressure**|*object*|weather.csv|Average station pressure|
|**SeaLevel**|*object*|weather.csv|Average sea level pressure|
|**ResultSpeed**|*float*|weather.csv|Resultant wind speed|
|**ResultDir**|*int*|weather.csv|Resultant direction of wind in degrees|
|**AvgSpeed**|*object*|weather.csv|Average speed|
