/**
 * Created by joelmarquez on 4/16/17.
 */

'use strict';

(function () {
    let chart;
    let factory = new Factory();
    let d3 = new d3charts();
    google.charts.load('current', {'packages': ['geochart']});
    google.charts.setOnLoadCallback(init);

    function init() {
        factory.getScores().then((resp) => {
            // factory.getData('total').then((resp2) => {
            //     d3.draw(null, resp2);
            //     drawRegionsMap(resp);
            //     document.getElementById('content').style.visibility='visible';
            //     document.getElementById('loader').style.visibility='hidden';
            // });

            d3.draw(null, factory.test);

            drawRegionsMap(resp);
            document.getElementById('content').style.visibility='visible';
            document.getElementById('loader').style.visibility='hidden';
        });
    }

    function drawRegionsMap(values) {
        let data = google.visualization.arrayToDataTable(values.values);

        let options = {
            region: "US",
            resolution: "provinces",
            colorAxis: {colors: ['#1ab2ff', '#9b0000'], values: [0, 100]},
            defaultColor: '#606060',
            backgroundColor: '#F8F8F8'
        };

        chart = new google.visualization.GeoChart(document.getElementById('geochart'));
        chart.draw(data, options);

        google.visualization.events.addListener(chart, 'select', () => {
            let state = factory.selections[chart.getSelection()[0].row];
            factory.getData(state).then((resp) => {
                d3.draw(state, resp);
                document.getElementById('visualization').scrollIntoView();
            });
        });
    }

})();
