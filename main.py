class StringCalculator():

    def add(self, numbers=""):

        # if '\n' is present in number, it will be replace with ','
        numbers = numbers.replace("\n", ",")

        # To fetch all the negatives in the string the multiple negatives
        negativesList = []

        # if string is empty
        if len(numbers) == 0:
            return 0

        # if there is only number present in the string
        elif ',' not in numbers:
            return int(numbers)

        # if more than one number is present in the string and seperated by delimeter 'comma(,)'
        else:

            # adding all the alphabets in alphaList and getting the value corresponding to each alphabet using its index in alphaList
            alphaList = []
            for i in range(97, 123, 1):
                alphaList.append(chr(i))



            # separating all the numbers or alphabets present in the string and creating a list from it
            numList = numbers.split(',')

            for key, val in enumerate(numList):
                # runs if current element is number and converts the character of string into integer
                try:
                    val = int(val)

                    # if value is greater than 1000 then it should be ignored, so it is set to 0
                    if val > 1000:
                        val = 0

                # runs if the current element is alphabet and takes the index of that alphabet from alphaList and gets the value corresponding to that alphabet
                except:
                    val = alphaList.index(val) + 1

                if val < 0:
                    negativesList.append(str(val))

                # allocates the int value corresponding to the character present at that index
                numList[key] = val

            if len(negativesList) == 0:
                return sum(numList)
            else:
                negativesAll = ', '.join(negativesList)
                raise Exception("\"Negatives not allowed\" - [" + negativesAll + "]")
