
import { graph } from './modules/graph.js';
import { socket } from './modules/socket_client.js';

(function () {

    const ws = socket.init();

    console.log(ws)

    ws.onmessage = function(event) {
        const data = JSON.parse(event.data);
        console.log('Got reply: ', data);

        document.body.append(
            graph.init(data)
        );
    };

}) ();