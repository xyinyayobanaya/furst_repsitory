class EvenNumbers:
    def __init__(self, start=0, end=1):
        if start >= end:
            raise ValueError("Start value must be less than end value")
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end or self.start % 2 != 0:
            raise StopIteration

        current_value = self.start
        self.start += 2
        return current_value

en = EvenNumbers(10, 25)
for i in en:
    print(i)