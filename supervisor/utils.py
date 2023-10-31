from functools import wraps
import time


def raise_not_implemented(obj):
	"""Raise NotImplementedError"""

	@wraps(obj)
	def __inner(*args, **kwargs):
		raise NotImplementedError("{0.__name__} '{1.__name__}' not implemented!".format(type(obj), obj))

	return __inner

def time_machine(frame_time):
	"""Create a frame timer"""
	last_frame = time.time()

	while True:
		current_time = time.time()
		delta_time = current_time - last_frame

		if delta_time < frame_time:
			time_to_sleep = frame_time - delta_time
			time.sleep(time_to_sleep)

		last_frame = time.time()
		yield