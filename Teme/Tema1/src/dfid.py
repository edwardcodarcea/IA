from math import inf
from sys import argv

import environment
from task_runner import run


def _dfid_traversal(env, node, visited, crt_cost, limit):
	global global_limit

	if node == env.target:
		return [node]

	for neigh, new_cost in env.neighbours[node]:
		neigh_cost = crt_cost + new_cost

		if neigh in visited and neigh_cost >= visited[neigh]:
			continue

		visited[neigh] = neigh_cost

		if neigh_cost <= limit:
			next_path = _dfid_traversal(env, neigh, visited,
				neigh_cost, limit)

			if next_path:
				return [node] + next_path
		elif neigh_cost < global_limit:
			global_limit = neigh_cost

	return []


def dfid(env):
	global global_limit

	global_limit = 0
	best_path = []
	visited = {}

	while not best_path and global_limit != inf:
		limit = global_limit
		global_limit = inf
		visited = {env.start: 0}

		best_path = _dfid_traversal(env, env.start, visited, 0, limit)

	return best_path, visited


def main():
	if len(argv) != 2:
		print(f"Usage: python3 {argv[0]} <input_file>")
		exit(1)

	run(dfid, "DFID", argv[1])


if __name__ == "__main__":
	main()
