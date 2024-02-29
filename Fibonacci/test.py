import time
from fibonacci import *
import json


def time_elapsed(fun, argument:int):
    start=time.time()
    result=fun(argument)
    end=time.time()
    time_elapsed=end-start
    return result,time_elapsed

def run_test(fun, argument:int):
    result,time_exec = time_elapsed(fun, argument)
    return result,time_exec


def generate_answers():
    answers=[]
    for i in range(0,501):
        answers.append(matrix(i))
    json.dump(answers, open("answers.json", "w"))

def test(answers,fun):
    times=[]
    if fun==recursive:
        for i in range(0,20):
            result,time_exec = run_test(fun, i)
            if result != answers[i]:
                print(f"Error: {i} -> {result} != {answers[i]}")
            times.append(time_exec)
        return range(0,20), times
    elif fun==eigen_vector_method:
        for i in range(0,501):
            # The eigen vector method needs some adjusting
            result,time_exec = run_test(fun, i-1)
            if result != answers[i]:
                print(f"Error: method eigenvector {i} -> {result} != {answers[i]}")
            times.append(time_exec)
        return range(0,501), times
    else:
        for i in range(0,501):
            result,time_exec = run_test(fun, i)
            if result != answers[i]:
                print(f"Error: {fun} {i} -> {result} != {answers[i]}")
            times.append(time_exec)
        return range(0,501), times