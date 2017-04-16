/**
 * Created by joelmarquez on 4/16/17.
 */

'use strict';

(function () {
    google.charts.load('current', {'packages':['geochart']});
    google.charts.setOnLoadCallback(drawRegionsMap);
    var states = {
        'Alabama': 1, 'Alaska': 100, 'Arizona': 100, 'Arkansas': 100, 'California': 100,
        'Colorado': 100, 'Connecticut': 100, 'Delaware': 100, 'Florida': 100, 'Georgia': 100,
        'Hawaii': 100, 'Idaho': 100, 'Illinois': 100, 'Indiana': 100, 'Iowa': 100,
        'Kansas': 100, 'Kentucky': 100, 'Louisiana': 100, 'Maine': 100, 'Maryland': 100,
        'Massachusetts': 100, 'Michigan': 100, 'Minnesota': 100, 'Mississippi': 100, 'Missouri': 100,
        'Montana': 100, 'Nebraska': 100, 'Nevada': 100, 'New Hampshire': 100, 'New Jersey': 100,
        'New Mexico': 100, 'New York': 100, 'North Carolina': 100, 'North Dakota': 100, 'Ohio': 100,
        'Oklahoma': 100, 'Oregon': 100, 'Pennsylvania': 100, 'Rhode Island': 100, 'South Carolina': 100,
        'South Dakota': 100, 'Tennessee': 100, 'Texas': 100, 'Utah': 100, 'Vermont': 100,
        'Virginia': 100, 'Washington': 100, 'West Virginia': 100, 'Wisconsin': 100, 'Wyoming': 100
    };
    var chart;

    function drawRegionsMap() {
        var array = [['State', 'Score']];
        getValues(array);

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

    var getValues = function (array) {
        for (var key in states) {
            if (states.hasOwnProperty(key)) {
                array.push([key, states[key]])
            }
        }
    }

})();