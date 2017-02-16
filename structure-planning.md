#Structure Planning

## Stack structure
Twitter <- Queuing system -> DB <-> Elastic search <- Web interface <- Client

## Twitter API Filtering
Filtering the data to consider racial/hate tweets in the U.S.
+ Static dictionary of terms to filter for
+ Use Geolocation from JSON
  * Use Lat/Long and "Address"
+ Creating map in a block structure (by state)

### Flow of Filtering Data
1. Geolocation
  * Filter by country first
  * Filter by country
2. Body
3. Insert to DB
