class StringCalculator():

    def add(self, numbers=""):
        # if string is empty
        if len(numbers) == 0:
            return 0

        # if there is only number present in the string
        elif ',' not in numbers:
            return int(numbers)

        # if more than one number is present in the string and seperated by delimeter '(,)'
        else:
            numList = map(int, numbers.split(','))

            # adding all the alphabets in alphaList and getting the value corresponding to each alphabet using its index in alphaList
            alphaList = []
            for i in range(97,123,1):
                alphaList.append(chr(i))

            # separating all the values present in the string and creating a new list from it
            numList = numbers.split(',')
            for key, val in enumerate(numList):

                # runs if current value is number and converts the character of string into integer
                try:
                    val = int(val)

                # runs if the current value is alphabet and takes the index of that alphabet from alphaList and gets the value corresponding to that alphabet
                except:
                    val = alphaList.index(val) + 1

                # allocates the intiger value corresponding to the character present at that index
                numList[key] = val

            return sum(numList)