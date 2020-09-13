from abc import ABC, abstractmethod
from typing import List
import functools

from ..util.operation import Operation
import functools


class ComputationStrategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions of some algorithm.
    The Context (in this case from controller) uses this interface to call the algorithm defined by Concrete Computationational Strategies.
    """
    @abstractmethod
    def compute_algorithm(self, num):
        pass

# Fibonacci strategy
class FibonacciStrategy(ComputationStrategy):

    def __init__(self):
        self.result = []

    def compute_algorithm(self, num):
        self.result = [self.fib(n) for n in range(num)]
        #self.fib(num)
        modified_arr = [ n for n in self.result if n < num and n > 1]
        return Operation.combinations_backtracking(self, num, modified_arr)

    @functools.lru_cache(maxsize=100)
    def fib(self, num):
        if num < 2:
            return 1
        return self.fib(num-1) + self.fib(num-2)

# Another strategy for factorial number
class FactorialStrategy(ComputationStrategy):
    def compute_algorithm(self, num):
        pass


class ComputationContext():
    def __init__(self, strategy:ComputationStrategy):
        self._strategy = strategy
    
    def do_computation(self, num):
        return self._strategy.compute_algorithm(num)
