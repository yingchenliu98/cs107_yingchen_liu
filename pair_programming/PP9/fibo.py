# pair programming 9
# team members: Yuxin Xu, Matt Egan, Yingchen Liu

#!/usr/bin/env python3

class Fibonacci():

    def __init__(self, length): 
        self.length = length
        if length == 1:
            sequence = [1]
        else:
            sequence = [1,2]
            if length != 2:
                try:
                    for i in range(2,length):
                        sequence.append(sequence[i-1] + sequence[i-2])
                except IndexError:
                    print("Length has to be a positive integer.")
        self.sequence = sequence

    def __iter__(self):
        return FibonacciIterator(self.sequence) # Returns an instance of the iterator

    def __repr__(self):
        return 'Fibonacci Sequence(%s)' % repr(self.sequence)


class FibonacciIterator(): # has __next__ and __iter__
    def __init__(self, sequence): 
        self.sequence = sequence
        self.index = 0 # Determines the next word to fetch

    def __next__(self): 
        try:
            fib_num = self.sequence[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return fib_num

    def __iter__(self):
        return self # Allows iterators to be used where an iterable is expected

fib = Fibonacci(10) # Create a Fibonacci iterator called fib that contains 10 terms
list(iter(fib)) # Iterate over the iterator and create a list.