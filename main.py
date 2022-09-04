class StringCalculator():
    def add(self, numbers=""):
        if len(numbers) == 0:
            return 0
        elif ',' not in numbers:
            return int(numbers)
        else:
            x, y = numbers.split(',')
            return int(x) + int(y)

            numList = map(int, numbers.split(','))
            return sum(numList)