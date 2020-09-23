import fileinput

class stack:

    def __init__(self, size):
         self.array_size_ = size
         self.count_ = 0
         self.l = [None for i in range (size)]

    def pushed(self, value):
        if (self.array_size_ == self.count_):

                print("overflow")
                return
        self.l[self.count_] = value
        self.count_=self.count_+1

    def empty(self):
        return (self.count_ == 0)

    def print(self):
        print(*self.l[:self.count_])


    def pop(self):
        self.count_=self.count_-1

    def top(self):
        return self.l[self.count_-1]

count = None
flag = False
st = None

for string in fileinput.input():
    if string!="\n":
        if flag == False:
            size = None
            num = ""
            if (string[0:9]=="set_size " and st is None):
                num = string[9:]
                try:
                    size = int(num)
                except(ValueError):
                    size = None

            if (size!=None and st is None):
                count = size
                st = stack(count)
                flag = True
                continue
            elif(st is None and size is None):
                print("error")
                continue
        else:

            if (string[0:4]=="pop\n"): #pop
                if (st.empty()):
                    print("underflow")
                else:
                    k=st.top()
                    print(k)
                    st.pop()
            elif string[0:5]=="push " :#push
                value = string[5:]
                value = value.replace('\n', '')
                is_valid = value.find(" ")
                if (is_valid==-1):
                    st.pushed(value)
                else:
                    print("error")
            elif (string[0:6]=="print\n"): #print
                if (st.empty()):
                    print ("empty")
                else:
                    st.print()
            else:
                print("error")
    else:
        continue
