# This is a sample Python script.
import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def buildMatrix(nodes, p):
    mat=np.zeros((nodes,nodes))
    for i in range(nodes):
        for j in range(i):
            n=np.random.rand()
            if n<p:
                mat[i][j]=1
                mat[j][i]=1
    return mat

def connectedComponents(unionArray):
    connectedComponents = []
    for i in range(len(unionArray)):
        if i in unionArray[i]:
            connectedComponents.append(unionArray[i])
    return connectedComponents

def union(i, j, unionArray):
    if i not in unionArray[i]:
        return union(list(unionArray[i])[0], j, unionArray)
    if j not in unionArray[j]:
        return union(i, list(unionArray[j])[0], unionArray)
    unionArray[i] = unionArray[i].union(unionArray[j])
    if unionArray[i] != unionArray[j]:
        unionArray[j] = {i}

def kruskal(mat):
    nodes = mat.shape[0]
    unionArray = list(range(nodes))
    for i in range(nodes):
        unionArray[i] = {i}

    for i in range(nodes):
        for j in range(i):
            if mat[i][j]==1:
                union(i,j, unionArray)
    return connectedComponents(unionArray)

def print_hi(name):
    runtime = []
    n = list(range(1,10))
    for i in range(1,10):
        nodes=i*100
        p= 1/nodes
        adjacencyMatrix = buildMatrix(nodes, p)
        start = time.time()
        print(kruskal(adjacencyMatrix))
        runtime.append(time.time()-start)

    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.arange(1, 50, 1)
    ax.plot(runtime, color='blue')
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
