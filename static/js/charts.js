/**
 * Created by joelmarquez on 4/19/17.
 */
'use strict';

let d3charts = function(){
    this.draw = function (state, data) {
        let dates = [];
        let vals = [];
        for(let key in data.history){
            dates.push(key);
            vals.push(data.history[key]);
        }

        console.log(dates)
        console.log(vals)

        let chart1 = c3.generate({
            bindto: '#chart1',
            data: {
                x: 'x',
                columns: [
                    ['x'] + dates,
                    ['data1'] + vals
                ],
                // type: 'spline',
                colors: {
                    data1: '#9b0000'
                },
                names: {
                    data1: 'Hate (%)'
                }
            },
            axis: {
                x: {
                    label: { // ADD
                        text: 'Date',
                        position: 'outer-middle'
                    },
                    type: 'timeseries',
                    tick: {
                        values: ['2017-01-01', '2017-02-01', '2017-03-01']
                        // format: '%m-%d'
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
            }
        });

        let chart2 = c3.generate({
            bindto: '#chart2',
            data: {
                columns: [
                    ['data1', data.percent.hate],
                    ['data2', data.percent.nonHate]
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
                    ['data1', data.percent.average],
                    ['data2', state? data.percent.hate : null]
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

