class Number:
    def __init__(self):
        # self.text = text
        self.path = 'number\\'
    def FromTextToNonNegativeCompleteNumber(self, num):
        if num < 20:
            return [self.path + str(num)]
        if num < 100:
            return [self.path + str(num // 10), self.path + str(num % 10)]
        order = [10 ** 9, 10 ** 6, 10 ** 3, 10 ** 2]
        list_path = []
        for i in order:
            if num // i > 0:
                list_path = list_path + self.FromTextToNonNegativeCompleteNumber(num // i)
                list_path.append(self.path + str(i))
                num %= i
                # list_path = list_path + self.FromTextToNonNegativeCompleteNumber(num)
                # list_path = list_path + self.FromTextToNonNegativeCompleteNumber(num % i)

        if num < 20:
            return list_path + [self.path + str(num)]
        if num < 100:
            return list_path + [self.path + str(num // 10), self.path + str(num % 10)]       
        return list_path
    def FromTextToUncompleteNumber(self, num):
        list_path = ['' for i in range(len(num))]
        for digit in num:
            list_path.append(self.path + digit)
        return list_path

# a = Number()
# print(a.FromTextToNonNegativeCompleteNumber(11))