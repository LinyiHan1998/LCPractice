from dataclasses import dataclass, replace

@dataclass
class TruckPosition:
	x: float
	y: float

@dataclass
class TruckPositionDelta:
	truck_id: int
	delta_x: float
	delta_y: float

class Subscriber:
	def __init__(self, server):
		self.server = server
		self.client_subscription = {}
		self.updates = {}

	def process_update(self, update):
		client_id = []
		for cid,tid in self.client_subscription.items():
			if update.truck_id in tid:
				client_id.append(cid)
		for cid in client_id:
			if cid not in self.updates:
				self.updates[cid].append(update)
        
		
	def subscribe_to_truck(self, truck_id, client_id):
		if client_id not in self.client_subscription:
			self.client_subscription[client_id]=[truck_id]
		else:
			self.client_subscription[client_id].append(truck_id)
		pos = self.server.subscribe_to_truck(truck_id)
		return replace(pos)
	def get_updates(self, client_id):
		updates = self.updates.get(client_id,[])
		self.updates[client_id]=[]
		return updates
		
class Server:
	def __init__(self):
		self.registered_trucks = set()
		self.current_pos = {}
		
	def subscribe_to_truck(self, truck_id):
		self.registered_trucks.add(truck_id)
		return replace(self.current_pos([truck_id]))
		
	def add_position(self, truck_id, pos):
		self.current_pos[truck_id] = pos
		
	def on_update(self,subscriber,update):
		if update.truck_id in self.registered_trucks:
			subscriber.process_update(update)
		pos = self.current_pos[update.truck_id]
		pos.x = update.delta_x
		pos.y = update.delta_y