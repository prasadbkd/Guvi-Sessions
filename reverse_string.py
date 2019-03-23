class stringg:
    def reverse(self,string):
        if len(string) == 0:
            return string
        else:
            #print(string)
            return s.reverse(string[1:]) + string[0]
s=stringg()
a = str(input("Enter the string to be reversed: "))
print(s.reverse(a))
