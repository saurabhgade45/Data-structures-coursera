# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
                # Replace this code with a faster implementation
                maxheight = 0
                heights = [0] * len(self.parent)
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        if (heights[vertex]!=0):
                                continue
                        while i!= -1:
                                if (heights[i]!=0):
                                        height += heights[i]
                                        break
                                height += 1
                                i = self.parent[i]
                        maxheight = max(maxheight,height)
                        i = vertex
                        while i != -1:
                                if (heights[i]!=0):
                                        break
                                heights[i] = height
                                height -= 1
                                i = self.parent[i]
                return maxheight

                                 


def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
