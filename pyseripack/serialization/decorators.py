## System Imports
from functools import wraps
from typing import Type


## Application Imports
from pynetway.networking import Direction
from pyseripack.packet.interfaces import PacketInterface
from pyseripack.serialization.interfaces import SerializationSetInterface
from pyseripack.serialization.metaclasses import PROPERTY_ATTRIBUTE_NAME


## Library Imports


def serialization_set(serialization_set_type: Type[SerializationSetInterface]):
	def decorator(serialization_type):
		
		if not hasattr(serialization_set_type, 'serializations'):
			serialization_set.serializations = []
		
		if serialization_type not in serialization_set_type.serializations:
			serialization_set_type.serializations.append(serialization_type)
		
		@wraps(serialization_type)
		def wrapper(*args, **kwargs):
			serialization_type(*args, **kwargs)
		
		return wrapper
	
	return decorator


def route_packet(packet_type: Type[PacketInterface], direction: Direction):
	def decorator(func):
		setattr(func, PROPERTY_ATTRIBUTE_NAME, True)
		setattr(func, 'packet', packet_type)
		setattr(func, 'direction', direction)
		
		# @wraps(func)
		# def func_wrapper(*args, **kwargs):
		# 	return func(func, *args, **kwargs)
		
		return func
	
	return decorator

