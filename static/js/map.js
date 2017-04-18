/**
 * Created by joelmarquez on 4/16/17.
 */

'use strict';

(function () {
    var chart;
    google.charts.load('current', {'packages': ['geochart']});
    google.charts.setOnLoadCallback(init);

    function init() {
        var url = "https://swishertest.site/api/map";
        var http = new HttpClient();

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
            console.log(chart.getSelection())
        });
    }

})();
