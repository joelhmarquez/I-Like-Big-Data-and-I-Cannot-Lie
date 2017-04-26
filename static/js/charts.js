/**
 * Created by joelmarquez on 4/19/17.
 */
'use strict';

let d3charts = function(){
    this.draw = function (state, data) {
        let dates = ['x'];
        let vals = ['data1'];

        // console.log("state" + state);
        // console.log("data" + data);

        if(data.history){
            for(let key in data.history){
                if(data.history[key] != 0){
                    let d = new Date(0);
                    dates.push(d.setUTCSeconds(parseFloat(key)));
                    vals.push(data.history[key]);
                    console.log(d)
                }
            }
        }

        let chart1 = c3.generate({
            bindto: '#chart1',
            data: {
                x: 'x',
                columns: [
                    dates,
                    vals
                ],
                // type: 'spline',
                colors: {
                    data1: '#9b0000'
                },
                names: {
                    data1: 'Hate (%)'
                },
                xFormat: '%Y-%m-%d %H:%M:%S'
            },
            axis: {
                x: {
                    label: { // ADD
                        text: 'Date',
                        position: 'outer-middle'
                    },
                    padding: {
                        left: 40,
                        right: 80
                    },
                    type: 'timeseries',
                    tick: {
                        count: 2,
                        format: '%d-%m'
                        // outer: false
                    }
                },
                y: {
                    label: { // ADD
                        text: 'Hate (%)',
                        position: 'outer-middle'
                    }
                }
            },
            title: {
                text: state? state + ' hate over time': 'Total hate over time'
            },
            padding: {
                right: 20,
                left: 35
            },
        });

        let chart2 = c3.generate({
            bindto: '#chart2',
            data: {
                columns: [
                    ['data1', data.percent.percent],
                    ['data2', 100-data.percent.percent]
                ],
                colors: {
                    data1: '#9b0000',
                    data2: '#1ab2ff'
                },
                names: {
                    data1: 'Hate Tweets',
                    data2: 'Non-Hate Tweets'
                },
                type : 'donut'
            },
            donut: {
                title: state || "Total"
            }
        });
        let chart3 = c3.generate({
            bindto: '#chart3',
            data: {
                columns: [
                    ['data1', 2.69],
                    ['data2', state? data.percent.percent : null]
                ],
                type: 'bar',
                colors: {
                    data1: '#9975b9',
                    data2: '#9b0000'
                },
                names: {
                    data1: 'Average Hate Tweets',
                    data2: state ? state + ' Hate Tweets': null
                },
                axis: {
                    y: {
                        label: {
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
                }
            },
            title: {
                text: state? state + ' vs Average': 'Average',
            },
            bar: {
                width: {
                    ratio: 0.25
                }
            }

        });
    };
};

