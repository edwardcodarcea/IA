from math import inf
from sys import argv

import environment
import heuristics as heur
from task_runner import run


def _ida_traversal(env, node, visited, crt_cost, limit, h):
	global global_limit

	if node == env.target:
		return [node]

	for neigh, neigh_cost in env.neighbours[node]:
		real_neigh_cost = crt_cost + neigh_cost
		pred_neigh_cost = real_neigh_cost + h(env, neigh)

		if neigh in visited and real_neigh_cost >= visited[neigh]:
			continue

		visited[neigh] = real_neigh_cost

		if pred_neigh_cost <= limit:
			next_path = _ida_traversal(env, neigh, visited, real_neigh_cost,
				limit, h)

			if next_path:
				return [node] + next_path
		elif pred_neigh_cost < global_limit:
			global_limit = pred_neigh_cost

	return []


def ida(env, h):
	global global_limit

	global_limit = h(env, env.start)
	best_path = []
	visited = {}

	while not best_path and global_limit != inf:
		limit = global_limit
		global_limit = inf
		visited = {env.start: 0}

		best_path = _ida_traversal(env, env.start, visited, 0, limit, h)

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

	run(ida, "IDA*", argv[1], heuristics[argv[2]], argv[2])


if __name__ == "__main__":
	main()
