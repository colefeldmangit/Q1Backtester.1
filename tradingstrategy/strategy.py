from abc import ABCMeta, abstractmethod


class Strategy(object):
    """ General strategy class. Implement a specific strategy that inherits
    from the strategy class. Call function produces dictionary of scalar values
    for assets given"""
    
    __metaclass__ = ABCMeta

    @abstractmethod
    def __call__(self, dt):
        raise NotImplementedError("Implement call function")




