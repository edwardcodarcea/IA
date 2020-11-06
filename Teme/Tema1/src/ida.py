from math import inf
from sys import argv
from time import process_time
import tracemalloc

from environment import get_next_states, init_env
from heuristics import euclid, manhattan
from plotter import display_results


def ida_traversal(crt_node, env, visited, crt_cost, limit, heur):
	global global_limit

	if crt_node == env.target:
		return [crt_node]

	for next_node, new_cost in get_next_states(env, crt_node):
		real_next_cost = crt_cost + new_cost
		pred_next_cost = real_next_cost + heur(env, next_node)

		if next_node in visited and real_next_cost >= visited[next_node]:
			continue

		visited[next_node] = real_next_cost

		if pred_next_cost <= limit:
			next_path = ida_traversal(next_node, env, visited, real_next_cost,
				limit, heur)

			if next_path:
				return [crt_node] + next_path
		elif pred_next_cost < global_limit:
			global_limit = pred_next_cost

	return []


def ida(env, heur):
	global global_limit

	global_limit = heur(env, env.start)
	best_path = []
	visited = {}

	while not best_path and global_limit != inf:
		limit = global_limit
		global_limit = inf
		visited = {env.start: 0}

		best_path = ida_traversal(env.start, env, visited, 0, limit, heur)

	return best_path, visited


def main():
	if len(argv) != 2:
		print(f"Usage: python3 {argv[0]} <input_file>")
		exit(1)

	env = init_env(argv[1])

	# Algoritmul e rulat de 2 ori, deoarece hookurile facute de `tracemalloc`
	# incetinesc algoritmul, ceea ce corupe masuratoarea de timp
	# De asemenea, e necesar ca rularea pentru masurarea memoriei sa se faca
	# prima. In caz contrar, masuratorile vor arata valori mai mici, deoarece
	# se va refolosi o parte din memoria alocata in cadrul primei rulari a
	# algoritmului.
	tracemalloc.start()
	path, costs = ida(env, euclid)
	# Cantitatea maxima de memorie utilizata
	memory = tracemalloc.get_traced_memory()[1]
	tracemalloc.stop()

	start_time = process_time()
	ida(env, euclid)
	end_time = process_time()

	display_results("IDA*", argv[1], env, path, costs, end_time - start_time,
		memory)


if __name__ == "__main__":
	main()
