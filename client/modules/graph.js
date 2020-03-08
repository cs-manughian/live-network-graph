
export var graph = (function () {
    return {
        init: function(container, data) {

                // Create a network
                
                var options = {
                  nodes: {
                    shape: "dot",
                    size: 16
                  },
                  physics: {
                    forceAtlas2Based: {
                      gravitationalConstant: -26,
                      centralGravity: 0.005,
                      springLength: 230,
                      springConstant: 0.18
                    },
                    maxVelocity: 146,
                    solver: "forceAtlas2Based",
                    timestep: 0.35,
                    stabilization: { iterations: 150 }
                  }
                };

                const network = new vis.Network(container, data, options);
                return network;
        }
    }
}) ();