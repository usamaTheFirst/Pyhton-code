"""Author :  Usama Fayyaz
   Date : 15//10/2020
"""


from matplotlib import pyplot as ppt

# function to compute n^2 - 10n
def function_1(n):
    return pow(n, 2) - 10 * n


# function to compute n^2/20
def function_2(n):
    return pow(n, 2) // 20


input_list = []
for i in range(50):
    input_list.append(i)
# function to get values of both function
function_2_output = []
function_1_output = []
for j in input_list:
    function_1_output.append(function_1(j))
    function_2_output.append(function_2(j))
ppt.plot(input_list,function_1_output,label = r"$n^2 - 10n$")
ppt.plot(input_list,function_2_output,label = r"$\frac{n^2}{20}$")
ppt.grid(True, color = "b")
ppt.legend()
ppt.show()
