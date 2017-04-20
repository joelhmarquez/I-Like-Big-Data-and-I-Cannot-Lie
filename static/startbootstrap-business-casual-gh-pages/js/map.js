/**
 * Created by joelmarquez on 4/16/17.
 */

'use strict';

(function () {
    var chart;
    var factory = new Factory();
    var d3 = new d3charts();
    google.charts.load('current', {'packages': ['geochart']});
    google.charts.setOnLoadCallback(init);

    function init() {
        var url = "https://swishertest.site/api/map";
        var http = new HttpClient();

        http.get(url, function(resp) {
            //TODO: Write http call to get initial chart data and have this func be in callback
            d3.draw(null, null);

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
            d3.draw(factory.selections[chart.getSelection()[0].row]);
            document.getElementById('visualization').scrollIntoView();
        });
    }

})();
