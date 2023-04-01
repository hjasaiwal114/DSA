class Solution:

    def mergeArray(self, a,b,n,m):
        new = []
        i = 0
        j = 0
        prev = None
        while i<n and j<m:
            if a[i] < b[j]:
                if (a[i] != prev):
                    new.append(b[j])
                    prev = b[j]
                i += 1
            elif (b[j] < a[i]):
                if b[j] != prev:
                    new.append(b[j])
            else:
                if(a[i] != prev):
                    new.append(a[i])
                    prev = b[j]
                j += 1 
            while i < n:
                if (a[i] !=prev):
                    new.append(a[i])
                    prev = a[i]
                i +=1 
            while j<m :
                if (b[j] != prev):
                    new.append(b[j])
                    prev = b[j]
                j += 1
            return new 
