/**
 * Created by joelmarquez on 4/17/17.
 */

'use strict';

var HttpClient = function() {
    this.get = function(url, callback) {
        var httpRequest = new XMLHttpRequest();
        httpRequest.onreadystatechange = function() {
            if (httpRequest.readyState == 4 && httpRequest.status == 200)
                callback(httpRequest.responseText);
        };

        httpRequest.open("GET", url, true);
        httpRequest.send(null);
    }
};