class Symbol:
    def __init__(self):
        self.path = 'symbol\\'
    
    def FromTextToSymbol(self, text):
        list_path = []
        for char in text:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                list_path.append(self.path + char + '.mp4')
            elif char == '.':
                list_path.append(self.path + 'dot.mp4')
            else:
                list_path.append(self.path + char + '.mp4')
    
        return list_path

# t = Symbol()
# print(t.FromTextToSymbol('abc#.-'))