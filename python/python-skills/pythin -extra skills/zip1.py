nums1=[1,2,3,4,5]
nums2=['one','two','three','four','five']
zipped=list(zip(nums1,nums2))     #zipping means collecting two lists
print(zipped)
unzipped=list(zip(*zipped))         # unzipping the two collected lists
print(unzipped)

# zipped k anadar ki list k elements ko access krnay ka tareeka

for (l1,l2) in zip(nums1,nums2):
    print(l1)
    print(l2)

#example of zipp function 

items=['apples',"bananas","mangoes"]
counts=[5,6,9]
prices=[1.2,3.9,2.88]

sentences=[]
for (items,counts,prices) in zip(items,counts,prices):
    (items,counts,prices)=str(items),str(counts),str(prices)
    sentence="I bought" + counts +"  " + items +" at "+prices+"  dollars each."
    sentences.append(sentence)
print(sentences)