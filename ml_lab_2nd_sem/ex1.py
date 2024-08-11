#Candidate Elimination Algorithm
a =[['sunny', 'warm', 'normal', 'strong', 'warm', 'same', 'Yes'],
   ['sunny', 'warm', 'high', 'strong', 'warm', 'same', 'Yes'],
   ['rainy', 'cold', 'high', 'strong', 'warm', 'change', 'No'],     
   ['sunny', 'warm', 'high', 'strong', 'cool', 'change', 'Yes']]
print(a[0])
num_attributes = len(a[0])
print(num_attributes)

s = ['0'] * num_attributes
g = ['?'] * num_attributes
print(s , g)    

# used to store the first line individualley
for j in range (0, num_attributes ):
    s[j] = a[0][j] ;


temp = []
for i in range (0, len(a)) :  
    if a[i][num_attributes-1] == 'yes' :
        for j in range (0, num_attributes) :
           if a[i][j] != s[j] : 
               s[j] = '?'
        for j in range (0, num_attributes) :
            for k in range (1, len (temp)) :
                if temp [k][j] != '?' and  temp[k][j]!=s[j] :
                    del temp[k]
        print("----------------------------------------------------------------------------- ")
        print(" For Training Example No :{0} the hypothesis is S{0} ".format(i+1),s)
        if (len(temp)==0):
            print(" For Training Example No :{0} the hypothesis is G{0} ".format(i+1),g)
        else:
            print(" For  Positive Training Example No :{0} the hypothesis is G{0}".format(i+1),temp)
    if a[i][num_attributes-1]=='No':
        for j in range(0,num_attributes):
            if s[j] != a[i][j] and s[j]!= '?':
                g[j]=s[j]
                temp.append(g)
                g = ['?'] * num_attributes
        print("----------------------------------------------------------------------------- ")
        print(" For Training Example No :{0} the hypothesis is S{0} ".format(i+1),s)
        print(" For Training Example No :{0} the hypothesis is G{0}".format(i+1),temp)