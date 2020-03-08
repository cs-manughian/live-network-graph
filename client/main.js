
import { graph } from './modules/graph.js';
import { socket } from './modules/socket_client.js';

(function () {

    let root = document.getElementById('root');

    const ws = socket.init();

    ws.onmessage = function(event) {
        const data = JSON.parse(event.data);
        console.log('Got reply: ', data);

        // Erase previous render
        // root.innerHTML = '';

        root.appendChild(
            graph.init(data)
        );

        // TODO: 
        // Trigger update graph functions based on reply without 
        // re-creating entire DOM element
    };

}) ();