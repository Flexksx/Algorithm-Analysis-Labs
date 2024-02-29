from test import *
from fibonacci import *
import matplotlib.pyplot as plt
import json

functions = [dynamic, iterative, matrix, eigen_vector_method, binet,recursive]
names = ["Dynamic", "Iterative", "Matrix", "Eigenvectors", "Binet","Recursive"]
generate_answers()
answers = json.load(open("answers.json"))


for i in range(len(functions)):
    x,y=test(answers,functions[i])
    plt.plot(x,y)
    plt.title(f"Time for {names[i]} method")
    plt.xlabel("n-th Fibonacci number")
    plt.ylabel("Time (s)")
    plt.savefig(f"{names[i]}.png")
    plt.close()

for i in range(len(functions)):
    x,y=test(answers,functions[i])
    plt.plot(x,y)
    plt.xlabel("n-th Fibonacci number")
    plt.ylabel("Time (s)")
plt.title("Time for all methods")
plt.legend(names)
plt.savefig("fib.png")
plt.close()





print("All tests passed")


