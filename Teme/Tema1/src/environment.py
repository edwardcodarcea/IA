from os.path import expanduser
from math import inf


class Environment:
	def __init__(self, start_x, start_y, target_x, target_y):
		self.__start_x = start_x
		self.__start_y = start_y
		self.__target_x = target_x
		self.__target_y = target_y
		self.graph = {}
		self.nodes = {}
		self.obsts = set()
		self.min_cost = inf
		self.__max_x = -inf
		self.__max_y = -inf

	def add_node(self, id, pos_x, pos_y, obst=False):
		if pos_x == self.__start_x and pos_y == self.__start_y:
			self.start = id
		if pos_x == self.__target_x and pos_y == self.__target_y:
			self.target = id

		if self.__max_x < pos_x:
			self.__max_x = pos_x
		if self.__max_y < pos_y:
			self.__max_y = pos_y

		if obst:
			self.obsts.add((pos_x, pos_y))
		else:
			self.nodes[id] = (pos_x, pos_y)

	def add_edge(self, id1, id2, cost):
		if id1 not in self.nodes or id2 not in self.nodes:
			return

		if cost < self.min_cost:
			self.min_cost = cost

		if id1 in self.graph:
			self.graph[id1].append((id2, cost))
		else:
			self.graph[id1] = [(id2, cost)]

		if id2 in self.graph:
			self.graph[id2].append((id1, cost))
		else:
			self.graph[id2] = [(id1, cost)]

	def get_size(self):
		return (self.__max_x, self.__max_y)


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
