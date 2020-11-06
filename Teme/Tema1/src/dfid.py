from math import inf
from sys import argv
from time import process_time
import tracemalloc

from environment import init_env, get_next_states, NODE, COST
from plotter import show_results


def dfid_traversal(crt_node, env, visited, cost, limit):
	global global_limit

	if crt_node == env.target:
		return [crt_node]

	for next_node, new_cost in get_next_states(env, crt_node):
		next_cost = cost + new_cost

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

	env = init_env(argv[1])

	# Algoritmul e rulat de 2 ori, deoarece hookurile facute de `tracemalloc`
	# incetinesc algoritmul, ceea ce corupe masuratoarea de timp
	# De asemenea, e necesar ca rularea pentru masurarea memoriei sa se faca
	# prima. In caz contrar, masuratorile vor arata valori mai mici, deoarece
	# se va refolosi o parte din memoria alocata in cadrul primei rulari a
	# algoritmului.
	tracemalloc.start()
	path, costs = dfid(env)
	# Cantitatea maxima de memorie utilizata
	memory = tracemalloc.get_traced_memory()[1]
	tracemalloc.stop()

	start_time = process_time()
	dfid(env)
	end_time = process_time()

	show_results(env, path, costs, end_time - start_time, memory)


if __name__ == "__main__":
	main()
