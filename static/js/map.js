/**
 * Created by joelmarquez on 4/16/17.
 */

'use strict';

(function () {
    var chart;

    init();

    function init() {
        var url = "http://swishertest.site/api/map";
        var http = new HttpClient();

        http.get(url,function (resp) {
            initMap(resp);
            // console.log(resp)
        })
    }

    var initMap = function drawRegionsMap(values) {
        google.charts.load('current', {'packages':['geochart']});
        google.charts.setOnLoadCallback(drawRegionsMap);

        var array = ['State', 'Score'];

        var data = google.visualization.arrayToDataTable(array);

        var options = {
            region: "US",
            resolution: "provinces",
            colorAxis: {colors: ['#0044bd', '#9b0000']},
            defaultColor: '#606060'
        };

        chart = new google.visualization.GeoChart(document.getElementById('geochart'));
        chart.draw(data, options);

        google.visualization.events.addListener(chart, 'select', function getSelection() {
            console.log(chart.getSelection())
        });
    }

})();