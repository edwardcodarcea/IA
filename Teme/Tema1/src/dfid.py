from math import inf
from sys import argv

from environment import get_next_states
from task_runner import run


def dfid_traversal(crt_node, env, visited, crt_cost, limit):
	global global_limit

	if crt_node == env.target:
		return [crt_node]

	for next_node, new_cost in get_next_states(env, crt_node):
		next_cost = crt_cost + new_cost

		if next_node in visited and next_cost >= visited[next_node]:
			continue

		visited[next_node] = next_cost

		if next_cost <= limit:
			next_path = dfid_traversal(next_node, env, visited,
				next_cost, limit)

			if next_path:
				return [crt_node] + next_path
		elif next_cost < global_limit:
			global_limit = next_cost

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

		best_path = dfid_traversal(env.start, env, visited, 0, limit)

	return best_path, visited


def main():
	if len(argv) != 2:
		print(f"Usage: python3 {argv[0]} <input_file>")
		exit(1)

	run(dfid, "DFID", argv[1])


if __name__ == "__main__":
	main()
