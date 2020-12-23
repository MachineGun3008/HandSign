class Number:
    def __init__(self):
        # self.text = text
        self.path = 'data\\number\\'
    def FromTextToNonNegativeCompleteNumber(self, num):
        if num < 20:
            return [self.path + str(num) + '.mp4']
        if num < 100:
            return [self.path + str(num // 10) + '.mp4', self.path + str(num % 10) + '.mp4']
        order = [10 ** 9, 10 ** 6, 10 ** 3, 10 ** 2]
        list_path = []
        for i in order:
            if num // i > 0:
                list_path = list_path + self.FromTextToNonNegativeCompleteNumber(num // i)
                list_path.append(self.path + str(i) + '.mp4')
                num %= i
                # list_path = list_path + self.FromTextToNonNegativeCompleteNumber(num)
                # list_path = list_path + self.FromTextToNonNegativeCompleteNumber(num % i)

        if 0 < num < 20:
            list_path.append(self.path + str(num) + '.mp4')
        elif 0 < num < 100:
            return list_path + [self.path + str(num // 10) + '.mp4', self.path + str(num % 10) + '.mp4']       
        return list_path
    def FromTextToUncompleteNumber(self, num):
        # print(num)
        # list_path = ['' for i in range(len(num))]
        list_path = []
        for i in range(len(num)):
            list_path.append(self.path + num[i] + '.mp4')
        return list_path

    def FromTextToNumber(self, num):
        list_path = []
        start = 0
        if num[0] == '-':
            list_path.append(self.path + '-.mp4')
            start = 1

        end = start
        while end < len(num) and num[end] != '.':
            end += 1

        if end - start < 11:
            list_path = list_path + self.FromTextToNonNegativeCompleteNumber(int(num[start : end]))

        if end != len(num) and num[end] == '.':
            list_path.append('data\\number\\dot.mp4')
            list_path = list_path + self.FromTextToUncompleteNumber(num[end + 1 : len(num)])

        return list_path

# a = Number()
# print(a.FromTextToNonNegativeCompleteNumber(11))