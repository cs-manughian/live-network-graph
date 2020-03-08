
import { graph } from './modules/graph.js';
import { socket } from './modules/socket_client.js';

socket.init();
document.body.innerHTML = graph;