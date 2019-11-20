from prometheus_client import Counter, Gauge

messages_received_counter = Counter("incoming_messages", "Messages received from Receptor Peers")
connected_peers_gauge = Gauge("connected_peers", "Number of active peer connections")
work_counter = Counter("work_events", "A count of the number of work events that have been received")
active_work_gauge = Gauge("active_work", "Amount of work currently being performed")
route_counter = Counter("route_events", "A count of the number of messages that have been routed elsewhere in the mesh")
