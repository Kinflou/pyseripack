## System Imports
from abc import ABCMeta


# Application modules


# Library modules


PROPERTY_ATTRIBUTE_NAME = "_property"
PACKET_FUNCTIONS_LIST_NAME = "_packet_functions"


class PacketSerializationMeta(type):
	
	@classmethod
	def __prepare__(mcs, name: str, bases: tuple):
		return super(PacketSerializationMeta, mcs).__prepare__(name, bases)
	
	def __new__(mcs, name: str, bases: tuple, dct):
		if len(bases) > 0:
			mcs.__determine_property(dct)
		
		return super(PacketSerializationMeta, mcs).__new__(mcs, name, bases, dct)
	
	@staticmethod
	def __determine_property(dct: dict):
		if PACKET_FUNCTIONS_LIST_NAME not in dct:
			dct[PACKET_FUNCTIONS_LIST_NAME] = []
		
		for attr, val in dct.items():
			if hasattr(val, PROPERTY_ATTRIBUTE_NAME):
				dct[PACKET_FUNCTIONS_LIST_NAME].append(val)


PacketSerializationMetaInterfaceMixin = type('PacketSerializationMetaInterfaceMixin',
                                             (ABCMeta, PacketSerializationMeta), {})
