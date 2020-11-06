from math import inf
from sys import argv

from environment import get_next_states
import heuristics as heur
from task_runner import run


def ida_traversal(crt_node, env, visited, crt_cost, limit, h):
	global global_limit

	if crt_node == env.target:
		return [crt_node]

	for next_node, new_cost in get_next_states(env, crt_node):
		real_next_cost = crt_cost + new_cost
		pred_next_cost = real_next_cost + h(env, next_node)

		if next_node in visited and real_next_cost >= visited[next_node]:
			continue

		visited[next_node] = real_next_cost

		if pred_next_cost <= limit:
			next_path = ida_traversal(next_node, env, visited, real_next_cost,
				limit, h)

			if next_path:
				return [crt_node] + next_path
		elif pred_next_cost < global_limit:
			global_limit = pred_next_cost

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

		best_path = ida_traversal(env.start, env, visited, 0, limit, h)

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
