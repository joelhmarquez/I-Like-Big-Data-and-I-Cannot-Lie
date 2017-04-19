/**
 * Created by joelmarquez on 4/19/17.
 */
'use strict';

(function () {
    var pie = new d3pie("pieChart", {
        "header": {
            "title": {
                "text": "Colorado",
                "fontSize": 24,
                "font": "open sans"
            },
            // "subtitle": {
            //     "text": "A full pie chart to show off label collision detection and resolution.",
            //     "color": "#999999",
            //     "fontSize": 12,
            //     "font": "open sans"
            // },
            "titleSubtitlePadding": 9
        },
        "footer": {
            "color": "#999999",
            "fontSize": 10,
            "font": "open sans",
            "location": "bottom-left"
        },
        "size": {
            "canvasWidth": 555,
            "pieOuterRadius": "90%"
        },
        "data": {
            "sortOrder": "value-desc",
            "content": [
                {
                    "label": "Hate Tweets",
                    "value": 30,
                    "color": "#9b0000"
                },
                {
                    "label": "Non-Hate Tweets",
                    "value": 70,
                    "color": "#1ab2ff"
                }
            ]
        },
        "labels": {
            "outer": {
                "pieDistance": 32
            },
            "inner": {
                "hideWhenLessThanPercentage": 3
            },
            "mainLabel": {
                "fontSize": 11
            },
            "percentage": {
                "color": "#ffffff",
                "decimalPlaces": 0
            },
            "value": {
                "color": "#adadad",
                "fontSize": 11
            },
            "lines": {
                "enabled": true
            },
            "truncation": {
                "enabled": true
            }
        },
        "effects": {
            "pullOutSegmentOnClick": {
                "effect": "linear",
                "speed": 400,
                "size": 8
            }
        },
        "misc": {
            "gradient": {
                "enabled": true,
                "percentage": 100
            }
        }
    });
})();