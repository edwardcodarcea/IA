from math import sqrt


def manhattan(env, node):
	target = env.nodes[env.target]
	crt = env.nodes[node]

	return abs(crt[0] - target[0]) + abs(crt[1] + target[1])


def euclid(env, node):
	target = env.nodes[env.target]
	crt = env.nodes[node]

	# TODO: calculat cu inv_sqrt? (lab IOCLA anu' 2)
	return int(sqrt((crt[0] - target[0])**2 + (crt[1] - target[1])**2))
