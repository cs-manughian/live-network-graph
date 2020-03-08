# Live Network Graph

Generate a live network graph representing process interaction using d3.js and web sockets

## Setup

### Client
To run this locally, you will need to set up a local testing server. 

1. Verify Python >= 3.6.1 is installed.
2. `cd` into the client directory and run the command `python3 -m http.server <port>`
   * This command should output: 
   `Serving HTTP on 0.0.0.0 port <port> ...`
3. Navigate to `localhost:<port>` to see the app running in the browser!

### Server

1. Install and activate your Python virtual environment:
```sh
pip install virtualenv
virtualenv env
.\path\to\env\Scripts\activate
```
2. Install websockets: `pip install websockets`
3. Freeze your installed packages: `pip freeze > requirements.txt`
4. Start the web socket server: `python3 socket_server.py`

### Troubleshooting

If your socket server immediately returns, please verify that the `websockets` python module is being imported.