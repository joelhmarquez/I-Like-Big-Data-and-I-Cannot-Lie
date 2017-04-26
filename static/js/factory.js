/**
 * Created by joelmarquez on 4/19/17.
 */
let Factory = function () {
    let http = new HttpClient();

    this.selections = {
        0: 'Rhode Island', 1: 'Mississippi', 2: 'New York', 3: 'Oklahoma', 4: 'Wyoming',
        5: 'Minnesota', 6: 'Illinois', 7: 'Arkansas', 8: 'South Carolina', 9: 'Indiana',
        10: 'Maryland', 11: 'Louisiana', 12: 'Texas', 13: 'New Hampshire', 14: 'Iowa',
        15: 'Wisconsin', 16: 'Arizona', 17: 'South Dakota', 18: 'Kansas', 19: 'Utah',
        20: 'Virginia', 21: 'Oregon', 22: 'Connecticut', 23: 'Montana', 24: 'California',
        25: 'Massachusetts', 26: 'Delaware', 27: 'New Mexico', 28: 'Vermont', 29: 'Georgia',
        30: 'Pennsylvania', 31: 'North Carolina', 32: 'Florida', 33: 'Hawaii', 34: 'Kentucky',
        35: 'Alaska', 36: 'Nebraska', 37: 'West Virginia', 38: 'Missouri', 39: 'Ohio',
        40: 'Alabama', 41: 'Colorado', 42: 'Idaho', 43: 'New Jersey', 44: 'Washington',
        45: 'Maine', 46: 'Tennessee', 47: 'North Dakota', 48: 'Nevada', 49: 'Michigan'
    };

    this.test = {
        'history': {
            '1492646400': 5,
            '1492732800': 20,
            '1492819200': 39,
            '1492905600': 78,
            '1492992000': 83,
            '1493078400': 100
        },
        'percent': {
            'hate': 35,
            'nonHate': 65,
            'average': 2
        }
    };

    this.getScores = () => {
    return new Promise((resolve, reject) => {
        let url = "https://swishertest.site/api/map";

        http.get(url, function(resp) {
            resolve(JSON.parse(resp))
        })
    });
    };

    this.getData = (state) => {
        return new Promise((resolve, reject) => {
            let url = "https://swishertest.site/api/data/" + state;

            http.get(url, function(resp) {
                resolve(JSON.parse(resp)['results'])
            })
        });
    };
};