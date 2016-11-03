#!/usr/bin/env python3
import time, sys

#Merge sort algorithm
def merge_sort(L):
    if len(L) <= 1:
        return L
    else:
        half = int(len(L) / 2)
        return merge(merge_sort(L[:half]), 
					 merge_sort(L[half:]))

def merge(A, B):
    S = []
    ai = 0
    bi = 0
    while ai < len(A) and bi < len(B):
        if A[ai] <= B[bi]:
            x = A[ai]
            ai += 1
        else:
            x = B[bi]
            bi += 1
        S.append(x)
    return S + A[ai:] + B[bi:]

def main():
    text = []
    sample = []

    file = open('beowulf.txt')
    n = input("Enter value for n: ")
    
    with file as fh:
        if(fh):
            for i in fh:
                text.append(i.strip())
    
    for k in range(int(n)):
        sample.append(text[k])
    
    for j in range(10):
        print(j+1, ' ' , sample[j])

    print('\nmerge sort...')
    print('Sorted:')
    
    start = time.perf_counter()
    sorted_text = merge_sort(sample)
    end = time.perf_counter()

    for j in range(10):
        print(j+1, ' ' , sorted_text[j])


    print('\nElapsed time:' +str(end-start)+ ' seconds')

if __name__ == '__main__':
    main()
