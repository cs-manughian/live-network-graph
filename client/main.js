
import { graph } from './modules/graph.js';
import { socket } from './modules/socket_client.js';

(function () {

    const ws = socket.init();
    
    graph.setRootElId('root');
    graph.init();

    ws.onmessage = function(event) {
        const data = JSON.parse(event.data);
        console.log('Got reply: ', data);

        graph.update({ graph: data });

        // TODO: 
        // Trigger update graph functions based on reply without 
        // re-creating entire DOM element
    };

}) ();