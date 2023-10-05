class Solution(object):
    def reverse(self, x):

        x_string = str(x)

        if len(x_string) > 1:
            x_string = x_string[::-1]
            counter = 0

            while counter < len(x_string):
                if x_string[counter] != "0":
                    break
                counter+=1

            x_string = x_string[counter:]

            if len(x_string) > 0:
                if x_string[-1] == "-":
                    x_string = x_string[-1] + x_string[0:-1]

        if len(x_string):
            x = int(x_string)
            if x >= -2**31 and x <= (2**31)-1:
                return x
            else:
                return 0

