
import { graph } from './modules/graph.js';
import { socket } from './modules/socket_client.js';

(function () {

    /*
     * Initialize the graph with empty data
     */
    let root = document.getElementById('root');
    // root.appendChild(graph.init([]));

    root.append(graph.bundleEdges())

    /*
     * Initialize socket connection and message event handler
     */
    const ws = socket.init();

    ws.onmessage = function(event) {

        const data = JSON.parse(event.data);
        console.log('Got reply: ', data);

        // Erase previous render
        // root.innerHTML = '';

        root.appendChild(graph.init(data));

        // TODO: 
        // Trigger update graph functions based on reply without 
        // re-creating entire DOM element
    };

}) ();