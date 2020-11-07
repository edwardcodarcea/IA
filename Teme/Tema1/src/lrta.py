from math import inf
from sys import argv

import environment
import heuristics as heur
from task_runner import run


def _get_H(node, H, h, env):
	if node not in H:
		H[node] = h(env, node)

	return H[node]


def _lrta_traversal(env, node, H, h, path, costs):
	while node != env.target:
		l = [cost + _get_H(neigh, H, h, env)
			for neigh, cost in env.neighbours[node]]

		best_neigh, best_cost = env.neighbours[node][l.index(min(l))]
		H[node] = best_cost + H[best_neigh]
		path.append(best_neigh)

		new_neigh_cost = best_cost + costs[node]
		if best_neigh not in costs or costs[best_neigh] > new_neigh_cost:
			costs[best_neigh] = new_neigh_cost

		node = best_neigh


def lrta(env, h):
	H = {env.start: h(env, env.start)}
	costs = {env.start: 0}

	old_path = [0]
	new_path = [-1]

	while old_path != new_path:
		old_path = new_path
		path = [env.start]

		_lrta_traversal(env, env.start, H, h, path, costs)
		new_path = path

	return (new_path, costs)


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

	run(lrta, "LRTA*", argv[1], heuristics[argv[2]], argv[2])


if __name__ == "__main__":
	main()
