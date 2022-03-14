## System Imports
import logging
from typing import List, Union


## Application Imports
from pyseripack.packet.interfaces import PacketInterface
from pyseripack.serialization.interfaces import SerializationSetInterface
from pyseripack.serialization.metaclasses import PacketSerializationMeta, PACKET_FUNCTIONS_LIST_NAME


## Library Imports


class PacketSerialization(metaclass=PacketSerializationMeta):
	
	def __init__(self, serialization_set_group: List[SerializationSetInterface]):
		self.serialization_set_group: List[SerializationSetInterface] = serialization_set_group
	
	def ResolvePacket(self, packet: Union[PacketInterface, bytes], outgoing: bool):
		resolved_message = self.Resolve(packet, outgoing)
		
		return resolved_message
	
	def Resolve(self, message: bytes, outgoing: bool):
		if outgoing:
			return self.Serialize(message)
		else:
			packet = self.Deserialize(message)
			return packet
	
	def ResolveAndRoute(self, message: bytes):
		packet = self.Deserialize(message)
		
		# TODO: Perhaps there should only be 2 groups, incoming and outgoing, so instead of having a list
		# TODO: Have a packet set variable for each direction and check if packet type is in the correct direction
		found = False
		for packet_group in self.packet_set_groups:
			if type(packet) not in packet_group.packet_types:
				found = True
				break
		
		if not found:
			logging.error(f"Received unregistered packet in current packet scope {type(packet)}, ignoring")
			return
		
		function_found = False
		for packet_function in getattr(self, PACKET_FUNCTIONS_LIST_NAME):
			if packet_function.packet == type(packet):
				packet_function(self, packet)
				function_found = True
		
		if not function_found:
			logging.info(f'Received valid packet {packet.__class__.__name__} but its not bound to any route')
	
	def Serialize(self, message: bytes):
		joined_ordered_serialization_sets = []
		
		for serialization_set in self.serialization_set_group:
			for serialization in serialization_set.serializations:
				joined_ordered_serialization_sets.append(serialization)
		
		processing_message = message
		
		for serialization in joined_ordered_serialization_sets:
			processing_message = serialization.Serialize(processing_message)
		
		return processing_message
	
	def Deserialize(self, message: bytes):
		joined_ordered_serialization_sets = []
		
		for serialization_set in reversed(self.serialization_set_group):
			for serialization in reversed(serialization_set.serializations):
				joined_ordered_serialization_sets.append(serialization)
		
		processing_message = message
		
		for serialization in joined_ordered_serialization_sets:
			processing_message = serialization.Deserialize(processing_message)
		
		return processing_message
