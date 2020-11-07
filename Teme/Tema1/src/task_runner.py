from time import process_time
import tracemalloc

from environment import Environment
from plotter import display_results


def run(alg, alg_name, input_file, heur=None, heur_name=None):
	env = Environment(input_file)

	# Algoritmul e rulat de 2 ori, deoarece hookurile facute de `tracemalloc`
	# incetinesc algoritmul, ceea ce corupe masuratoarea de timp
	# De asemenea, e necesar ca rularea pentru masurarea memoriei sa se faca
	# prima. In caz contrar, masuratorile vor arata valori mai mici, deoarece
	# se va refolosi o parte din memoria alocata in cadrul primei rulari a
	# algoritmului.

	tracemalloc.start()

	if heur:
		path, costs = alg(env, heur)
	else:
		path, costs = alg(env)

	# Cantitatea maxima de memorie utilizata
	memory = tracemalloc.get_traced_memory()[1]
	tracemalloc.stop()

	start_time = process_time()
	if heur:
		path, costs = alg(env, heur)
	else:
		path, costs = alg(env)
	end_time = process_time()

	display_results(alg_name, input_file, env, path, costs,
		end_time - start_time, memory, heur_name)
