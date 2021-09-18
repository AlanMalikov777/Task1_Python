
def toSwap(listToEnter,x,y):#swaps two variables
    listToEnter[x],listToEnter[y]=listToEnter[y],listToEnter[x]
# toPermute uses a heap's algorithm
def toPermute(list, current, last):#takes a list, starting index and last index
    if last<0:
        print("")
    elif current == last:# if starting and last indexes will equalise then our function will be done
	    print(''.join(list))#changes from list to string
    else:
	    for i in range(current, last + 1):#permutating with recursion
		    toSwap(list,current,i)
		    toPermute(list, current + 1, last)
		    toSwap(list,current,i)

txt=input("Inseart your text: ")
size = len(txt)
list1 = list(txt)
toPermute(list1, 0, size-1)





