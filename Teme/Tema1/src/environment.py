from os.path import expanduser
from math import inf


class Environment:
	def __init__(self, input_file):
		self.neighbours = {}
		self.nodes = {}
		self.obsts = set()
		self.min_cost = inf
		self.__max_x = -inf
		self.__max_y = -inf

		delim = ", "
		obst = "obstacle"

		with open(expanduser(input_file)) as f:
			self.__mouse_x, self.__mouse_y = \
				[int(x) for x in next(f).split(delim)]
			self.__cheese_x, self.__cheese_y = \
				[int(x) for x in next(f).split(delim)]

			num_nodes = int(next(f))

			for _ in range(num_nodes):
				node = next(f).strip().split(delim)

				if obst not in node:
					self.add_node(*list(map(int, node)))
				else:
					self.add_node(*list(map(int, node[:-1])), True)

			num_edges = int(next(f))
			for _ in range(num_edges):
				self.add_edge(*list(map(int, next(f).strip().split(delim))))

	def add_node(self, id, pos_x, pos_y, obst=False):
		if pos_x == self.__mouse_x and pos_y == self.__mouse_y:
			self.start = id
		if pos_x == self.__cheese_x and pos_y == self.__cheese_y:
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

		if id1 in self.neighbours:
			self.neighbours[id1].append((id2, cost))
		else:
			self.neighbours[id1] = [(id2, cost)]

		if id2 in self.neighbours:
			self.neighbours[id2].append((id1, cost))
		else:
			self.neighbours[id2] = [(id1, cost)]

	def get_size(self):
		return (self.__max_x, self.__max_y)


# Functii inutile pentru rezolvare, dar 5p sunt 5p...
def init_env(input_file):
	return Environment(input_file)


def get_next_states(env, state):
	return env.neigbours[state]


def apply_action(env, state, action):
	pass
