## System Imports
from typing import Type


## Application Imports
from pyseripack.packet_set.interfaces import PacketSetInterface


## Library Imports


def packet_set(packet_set_type: Type[PacketSetInterface]):
	
	def decorator(packet_type: Type[PacketSetInterface]):
		
		if not hasattr(packet_set_type, 'packet_types'):
			packet_set_type.packet_types = []
		
		if packet_type not in packet_set_type.packet_types:
			packet_set_type.packet_types.append(packet_type)
		
		# @wraps(packet_type)
		# def func(*args, **kwargs):
		# 	return packet_type
		
		return packet_type
	
	return decorator
