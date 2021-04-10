from abc import ABC, abstractmethod


class Device(ABC):
    @classmethod
    @abstractmethod
    def get_name(cls, data):
        raise NotImplemented


class Unknown(Device):
    @classmethod
    def get_name(cls, data):
        return data.get('product', 'Unknown')


class Memory(Device):
    @classmethod
    def get_name(cls, data):
        return data['description']


class Processor(Device):
    @classmethod
    def get_name(cls, data):
        return data['product']


class Bridge(Device):
    @classmethod
    def get_name(cls, data):
        return data['product']


class Generic(Device):
    @classmethod
    def get_name(cls, data):
        return data['product']