from copy import deepcopy
from math import inf
from sys import argv

import environment
import heuristics as heur
from task_runner import run


def _bnb_traversal(env, node, path, cost, h, visited):
	global limit
	global best_path

	visited[node] = cost

	if node == env.target:
		best_path = deepcopy(path)
		limit = cost
		return

	for neigh, edge_cost in sorted(env.neighbours[node], key=lambda x: x[1]):
		neigh_cost = cost + edge_cost
		if (neigh in visited and visited[neigh] <=neigh_cost
			or neigh_cost + h(env, neigh) >= limit
		):
			continue

		path.append(neigh)
		_bnb_traversal(env, neigh, path, neigh_cost, h, visited)
		del(path[-1])


def bnb(env, h):
	global limit
	global best_path

	limit = inf
	visited = {}
	best_path = []

	_bnb_traversal(env, env.start, [], 0, h, visited)

	return best_path, visited


def main():
	if len(argv) != 3:
		print(f"Usage: python3 {argv[0]} <input_file> <heuristic>")
		exit(1)

	heuristics = {
		"euclid": heur.euclid,
		"manhattan": heur.manhattan,
		"manhattan_on_steroids": heur.manhattan_on_steroids
	}

	if argv[2] not in heuristics:
		print(f"The available heuristics are: {heuristics.keys()}")
		exit(2)

	run(bnb, "B&B", argv[1], heuristics[argv[2]], argv[2])


if __name__ == "__main__":
	main()
