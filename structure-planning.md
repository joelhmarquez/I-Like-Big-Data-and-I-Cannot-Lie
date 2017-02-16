#Structure Planning

## Stack structure
Twitter <- Queuing system -> DB <-> Elastic search <- Web interface <- Client

### Stack technologies
+ Twitter API
 * REST API (JSON)
+ Queuing system
 * Storm
+ DB
 * Cassandra
 * Dynamo?
+ Elastic search
+ Web interface
 * AWS EC2
+ Client
 * PHP
 * JS
 * Elm

## Twitter API filtering
Filtering the data to consider racial/hate tweets in the U.S.
+ Static dictionary of terms to filter for
+ Use Geolocation from JSON
  * Use Lat/Long and "Address"
+ Creating map in a block structure (by state)

### Flow of filtering data
1. Geolocation
  * Filter by country first
  * Filter by country
2. Body
3. Insert to DB

### Questions
+ Does there need to be a pre-processor for filtering?
