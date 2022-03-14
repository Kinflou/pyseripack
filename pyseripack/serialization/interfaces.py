## System Imports
from typing import List
from abc import ABC, abstractmethod


## Application Imports


## Library Imports


class SerializationInterface(ABC):
	
	@staticmethod
	@abstractmethod
	def Serialize(raw_message: bytes):
		pass
	
	@staticmethod
	@abstractmethod
	def Deserialize(packed_message: bytes):
		pass


class SerializationSetInterface(ABC):
	
	@property
	@abstractmethod
	def serializations(self) -> List[SerializationInterface]:
		pass
	
