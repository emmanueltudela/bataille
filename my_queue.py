def create(size):
	queue = [0, 3, 3] + [None for i in range(size)]
	# queue[0] => number of elements in queue
	# queue[1] => index of first element in queue
	# queue[2] => index of last element in queue
	return queue

def is_empty(queue):
	empty = queue[0] == 0
	return empty

def is_full(queue):
	full = queue[0] == len(queue) - 3
	return full

def enqueue(queue, value):
	full = is_full(queue)
	assert not full, "Cannot enqueue on full queue"
	last_index = queue[2]
	queue[last_index] = value
	next_index = last_index + 1 if last_index + 1 < len(queue) else 3
	queue[2] = next_index
	queue[0] += 1

def dequeue(queue):
	empty = is_empty(queue)
	assert not empty, "Cannot dequeue on empty queue"
	current_index = queue[1]
	return_value = queue[current_index]
	next_index = current_index + 1 if current_index + 1 < len(queue) else 3
	queue[1] = next_index
	queue[0] -= 1
	return return_value

def next_value(queue):
	next_index = queue[1]
	value = queue[next_index]
	return value