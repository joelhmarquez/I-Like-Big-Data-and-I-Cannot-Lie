#Structure Planning

Document to outline the stack structure as well as the storage structure

## Stack structure
Twitter <- Queuing system -> DB <-> Elastic search <- Web interface <- Client

### Stack technologies
+ Twitter API
 * REST API (JSON)
+ Queuing system
 * Storm
+ DB
 * Cassandra -> NoSQL
 * Dynamo?
+ Elastic search
+ Web interface
 * AWS EC2
+ Client
 * PHP
 * JS
 * Elm
 * Google Maps API

## Twitter API filtering
Filtering the data to consider racial/hate tweets in the U.S.
+ Static dictionary of terms to filter for
+ Use Geolocation from JSON
  * Use Lat/Long and "Address"
+ Creating map in a block structure (by state)

### Flow of filtering data
1. Geolocation
  * Filter by country first
  * Filter by state
2. Filter by tweet body
3. Queuing system
4. Insert to DB
5. Send through elastic search
6. Google charts
7. Web interface
8. Cycle 5-7

### Data storage structure

State | Count | Score -> Timeblock (days || time from epoch) -> Tweets
#### Fields

| State        | City     | Score | Username      | Tweet MSG ID  | Timestamp  |
| :----------: | :------: | :---: | :-----------: | :-----------: | :--------: |
| Colorado     | Denver   | 7     | Person        | somekeyID     | 2017-06-01 |

### Questions
+ Does there need to be a pre-processor for filtering?
