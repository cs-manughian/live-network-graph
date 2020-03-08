
export var socket = (function () {
    return {
        init: function () {
            const websocket = new WebSocket('ws://localhost:8001/');
            
            websocket.onopen = function() {
                console.log('Socket opening...');
                websocket.send('Sending package from client...');
            };

            websocket.onclose = function() {
                console.log('Socket client closed...');
            };

            window.onbeforeunload = function() {
                websocket.close();
            }

            return websocket;
        }
    };
}) ();