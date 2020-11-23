#!/usr/bin/python3
import math
import sys
import threading

sys.setrecursionlimit(2 * 10 ** 9)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


def isBst(tree, i, mini, maxi):
  if not mini <= tree[i][0] < maxi:
    return False
  if tree[i][1] != -1:
    if not isBst(tree, tree[i][1], mini, tree[i][0]):
      return False
  if tree[i][2] != -1:
    if not isBst(tree, tree[i][2], tree[i][0], maxi):
      return False
  return True

def IsBinarySearchTree(tree):
    return isBst(tree, 0, -math.inf, math.inf)


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if not tree or IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
