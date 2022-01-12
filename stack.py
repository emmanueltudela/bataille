def create(size):
	stack = [0] + [None for i in range(size)]
	# stack[0] => last value index (if 0 : none)
	return stack

def is_empty(stack):
	empty = stack[0] == 0
	return empty

def is_full(stack):
	full = stack[0] == len(stack) - 1
	return full

def push(stack, value):
	full = is_full(stack)
	assert not full, "Cannot push on full stack"
	last_index = stack[0]
	next_index = last_index + 1
	stack[next_index] = value
	stack[0] += 1

def pop(stack):
	empty = is_empty(stack)
	assert not empty, "Cannot pop on empty stack"
	last_index = stack[0]
	return_value = stack[last_index]
	stack[0] -= 1
	return return_value

def top_value(stack):
	top_index = stack[0]
	value = stack[top_index]
	return value