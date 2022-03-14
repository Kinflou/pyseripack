## System Imports
from functools import wraps
from typing import Type


## Application Imports
from pyseripack.packet.interfaces import PacketInterface
from pyseripack.packet_set.interfaces import PacketSetInterface


## Library Imports


def packet(packet_set_type: Type[PacketInterface]):
	
	def decorator(packet_type: Type[PacketSetInterface]):
		
		if not hasattr(packet_set_type, 'packet_types'):
			packet_set_type.packet_types = []
		
		if packet_type not in packet_set_type.packet_types:
			packet_set_type.packet_types.append(packet_type)
		
		@wraps
		def func(f_args, f_kwargs):
			return f_args, f_kwargs
		
		return func
	
	return decorator
