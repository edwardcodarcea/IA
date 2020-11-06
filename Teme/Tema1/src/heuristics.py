from math import sqrt

import environment


def manhattan(env, node):
	target = env.nodes[env.target]
	crt = env.nodes[node]

	return abs(crt[0] - target[0]) + abs(crt[1] - target[1])


def euclid(env, node):
	target = env.nodes[env.target]
	crt = env.nodes[node]

	return int(sqrt((crt[0] - target[0])**2 + (crt[1] - target[1])**2))


def manhattan_on_steroids(env, node):
	return manhattan(env, node) * env.min_cost
