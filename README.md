# tcp_ip_python
Connection between Kuka and RPLidar, tcp/ip communication implementation

TCP/IP socket communication with "threading" python module.

In this code :
- 1 server => handle client connections
- 1 client Sensor => send data to the server
- 1 client Robot => receive data from the server

Run the server, then run and connect the two clients.
The sensor client simulate the position of the RPLidar in the space.
The robot client receive the position in fact => His own simulate position.
(If you don't have feedback robot position.)
