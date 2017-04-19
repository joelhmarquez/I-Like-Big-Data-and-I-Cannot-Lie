/**
 * Created by joelmarquez on 4/19/17.
 */
'use strict';

var d3charts = function(){
    var chart1;
    var chart2;
    var chart3;
    this.draw = function (state, data) {
        chart1 = c3.generate({
            bindto: '#chart1',
            data: {
                columns: [
                    ['Hate(%)', 5, 20, 46, 60, 75, 100]
                ],
                type: 'spline'
            },
            axis: {
                y: {
                    label: { // ADD
                        text: 'Hate (%)',
                        position: 'outer-middle'
                    }
                },
                x: {
                    label: { // ADD
                        text: 'Date',
                        position: 'outer-middle'
                    }
                }
            },
            title: {
                text: 'Hate over time'
            }
        });

        chart2 = c3.generate({
            bindto: '#chart2',
            data: {
                columns: [
                    ['Hate Tweets', 30],
                    ['Non-Hate Tweets', 70]
                ],
                type : 'donut',
                onclick: function (d, i) { console.log("onclick", d, i); },
                onmouseover: function (d, i) { console.log("onmouseover", d, i); },
                onmouseout: function (d, i) { console.log("onmouseout", d, i); }
            },
            donut: {
                title: state || "Total"
            }
        });

        chart3 = c3.generate({
            bindto: '#chart3',
            data: {
                columns: [
                    [state + '(%)', 5, 20, 46, 60, 75, 100],
                    ['Avg(%)', 10, 40, 56, 78, 83, 100]
                ],
                type: 'spline'
            },
            axis: {
                y: {
                    label: { // ADD
                        text: 'Hate (%)',
                        position: 'outer-middle'
                    }
                },
                x: {
                    label: { // ADD
                        text: 'Date',
                        position: 'outer-middle'
                    }
                }
            },
            title: {
                text: state? state + ' vs Average': 'Average'
            }
        });
    };

    // this.update= function (state) {
    //     this.init(state, null)
    // }
};

