class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A=sorted(A)
        d=dict()
        if len(A)==3:
            return sum(A)
        for i in range(len(A)-2):
            if A[i]==A[i-1] and i>0:
                continue
            pt1=i+1
            pt2=len(A)-1
            while pt1<pt2:
                summ=A[i]+A[pt1]+A[pt2]
                diff=abs(summ-B)
                d[diff]=summ
                if pt1<pt2 and summ<B:
                    pt1+=1
                elif pt1<pt2 and summ>B:
                    pt2-=1
                else:
                    return summ
        return d[min(d)]
