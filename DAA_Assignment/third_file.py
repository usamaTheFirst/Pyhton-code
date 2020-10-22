"""Author :  Usama Fayyaz
   Date : 15//10/2020
"""


from matplotlib import pyplot as ppt


# function to compute 3n^2 -25n
def function_1(n):
    return 3 * pow(n, 2) - 25 * n


# function to compute value of 9.n^2 /50
def function_2(n):
    return (9 * pow(n, 2)) // 50


input_list = []
for i in range(50):
    input_list.append(i)
# function to get values of both function
function_2_output = []
function_1_output = []
for j in input_list:
    function_1_output.append(function_1(j))
    function_2_output.append(function_2(j))
ppt.plot(input_list, function_1_output, label=r"$3n^2 - 25n$")
ppt.plot(input_list, function_2_output, label=r"$\frac{9n^2}{50}$")
ppt.grid(True, color="b")
ppt.legend()
ppt.show()
