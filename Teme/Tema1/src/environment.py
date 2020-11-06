from os.path import expanduser


NODE = 0
COST = 1


class Environment:
	def __init__(self, start_x, start_y, target_x, target_y):
		self.__start_x = start_x
		self.__start_y = start_y
		self.__target_x = target_x
		self.__target_y = target_y
		self.graph = {}
		self.nodes = {}
		self.obsts = set()

	def add_node(self, id, pos_x, pos_y, obst=False):
		if pos_x == self.__start_x and pos_y == self.__start_y:
			self.start = id
		if pos_x == self.__target_x and pos_y == self.__target_y:
			self.target = id

		if obst:
			self.obsts.add((pos_x, pos_y))
		else:
			self.nodes[id] = (pos_x, pos_y)

	def add_edge(self, id1, id2, cost):
		if id1 not in self.nodes or id2 not in self.nodes:
			return

		if id1 in self.graph:
			self.graph[id1].append((id2, cost))
		else:
			self.graph[id1] = [(id2, cost)]

		if id2 in self.graph:
			self.graph[id2].append((id1, cost))
		else:
			self.graph[id2] = [(id1, cost)]

	def get_size(self):
		return (
			max(c for c, _ in self.nodes.values()),
			max(r for r, _ in self.nodes.values())
		)


def init_env(input_file):
	delim = ", "
	obst = "obstacle"

	with open(expanduser(input_file)) as f:
		mouse_x, mouse_y = [int(x) for x in next(f).split(delim)]
		cheese_x, cheese_y = [int(x) for x in next(f).split(delim)]

		env = Environment(mouse_x, mouse_y, cheese_x, cheese_y)
		num_nodes = int(next(f))

		for _ in range(num_nodes):
			node = next(f).strip().split(delim)

			if obst not in node:
				env.add_node(*list(map(int, node)))
			else:
				env.add_node(*list(map(int, node[:-1])), True)

		num_edges = int(next(f))
		for _ in range(num_edges):
			env.add_edge(*list(map(int, next(f).strip().split(delim))))

		return env

def get_next_states(env, node):
	return env.graph[node]

def apply_action(env, node):
	pass
