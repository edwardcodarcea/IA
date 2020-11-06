import matplotlib.pyplot as plt


def _get_real_path(path, env):
	return " -> ".join([f"{env.nodes[node]}" for node in path])


def _plot_costs(axis, map_size, env, costs):
	visited_costs = {env.nodes[node]: cost for node, cost in costs.items()}
	cost_map = [[visited_costs.get((c, r), 0)
		for r in range(map_size[0])] for c in range(map_size[1])]

	for r in range(map_size[0]):
		for c in range(map_size[1]):
			if (c, r) in env.obsts:
				cost_map[c][r] = -2

	axis.set_title("Costurile gasite de agent")
	axis.imshow(cost_map, cmap="gist_heat", interpolation="nearest",
		origin="lower")


def _plot_path(axis, map_size, env, path):
	visited = set(env.nodes[node] for node in path)
	cost_map = [[0 if (c, r) in env.obsts else 20 \
		for r in range(map_size[0])] for c in range(map_size[1])]

	for r in range(map_size[0]):
		for c in range(map_size[1]):
			if (c, r) in visited:
				cost_map[c][r] = 40

	cost_map[env.nodes[env.target][0]][env.nodes[env.target][1]] = 60
	cost_map[env.nodes[env.start][0]][env.nodes[env.start][1]] = 30

	axis.set_title("Calea agentului pana la tinta")
	axis.imshow(cost_map, cmap="gist_heat", interpolation="nearest",
		origin="lower")


def display_results(alg, input_file, env, path, costs, time, memory,
	heur_name=None
):
	print(f"Path nodes:\n{path}")
	print(f"Path positions:\n{_get_real_path(path, env)}")

	print(f"Cost to target: {costs[env.target]}")
	print(f"Running time: {time} seconds")
	print(f"Used memory: {memory / 2**10} KB")

	map_size = env.get_size()
	fig, axes = plt.subplots(1, 2)
	if heur_name:
		fig.suptitle(f"Costs and best path for {alg} with heuristic "
			f"'{heur_name}' on file {input_file}")
	else:
		fig.suptitle(f"Costs and best path for {alg} on file {input_file}")

	_plot_costs(axes[0], map_size, env, costs)
	_plot_path(axes[1], map_size, env, path)

	fig.tight_layout()
	plt.show()
