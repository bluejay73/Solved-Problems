class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        arr=[]
        d=dict()
        for i in range(len(A)):
            st=A[i]
            st=''.join(sorted(st))
            if st in d:
                d[st].append(i+1)
            else:
                d[st]=[i+1]
        for i in d:
            arr.append(d[i])
        return arr