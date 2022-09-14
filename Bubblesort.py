A = ["Didrik","Unni","Anders","Lars","Christian"]

for i in range(len(A)):
     
    
    sortet=False
    while sortet==False:
        sortet=True 
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
                sortet=False     
   

print ("Sortet array")
for i in range(len(A)):
    print(A[i],end=" ")



