/**
 * Created by joelmarquez on 4/16/17.
 */

'use strict';

(function () {
    var selections = {
            0: 'Alabama', 1: 'Alaska', 2: 'Arizona', 3: 'Arkansas', 4: 'California',
            5: 'Colorado', 6: 'Connecticut', 7: 'Delaware', 8: 'Florida', 9: 'Georgia',
            10: 'Hawaii', 11: 'Idaho', 12: 'Illinois', 13: 'Indiana', 14: 'Iowa',
            15: 'Kansas', 16: 'Kentucky', 17: 'Louisiana', 18: 'Maine', 19: 'Maryland',
            20: 'Massachusetts', 21: 'Michigan', 22: 'Minnesota', 23: 'Mississippi', 24: 'Missouri',
            25: 'Montana', 26: 'Nebraska', 27: 'Nevada', 28: 'New Hampshire', 29: 'New Jersey',
            30: 'New Mexico', 31: 'New York', 32: 'North Carolina', 33: 'North Dakota', 34: 'Ohio',
            35: 'Oklahoma', 36: 'Oregon', 37: 'Pennsylvania', 38: 'Rhode Island', 39: 'South Carolina',
            40: 'South Dakota', 41: 'Tennessee', 42: 'Texas', 43: 'Utah', 44: 'Vermont',
            45: 'Virginia', 46: 'Washington', 47: 'West Virginia', 48: 'Wisconsin', 49: 'Wyoming'
    };
    var chart;
    var charts = new d3charts();
    google.charts.load('current', {'packages': ['geochart']});
    google.charts.setOnLoadCallback(init);

    function init() {
        var url = "https://swishertest.site/api/map";
        var http = new HttpClient();

        //TODO: Write http call to get initial chart data and have this func be in callback
        charts.draw(null, null);

        http.get(url, function(resp) {
            drawRegionsMap(JSON.parse(resp));
             document.getElementById('content').style.visibility='visible'; 
            document.getElementById('loader').style.visibility='hidden';
        })
    }

    function drawRegionsMap(values) {
        var data = google.visualization.arrayToDataTable(values.values);

        var options = {
            region: "US",
            resolution: "provinces",
            colorAxis: {colors: ['#1ab2ff', '#9b0000']},
            defaultColor: '#606060',
            backgroundColor: '#F8F8F8'
        };

        chart = new google.visualization.GeoChart(document.getElementById('geochart'));
        chart.draw(data, options);

        google.visualization.events.addListener(chart, 'select', function getSelection() {
            charts.draw(selections[chart.getSelection()[0].row]);
            document.getElementById('visualization').scrollIntoView();
        });
    }

})();
