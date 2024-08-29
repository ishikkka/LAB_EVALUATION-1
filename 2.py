list = []

def addItem(list, item1) :
    list.append(item1)

def displayList(list):
    print("List :", list)

def removeItem(list, item1):
    if(item1 not in list):
        print("Not present")
        return
    list.remove(item1)

def searchItem(list, item1):
    if(item1 in list):
        return True
    else :
        return False

consent = 'y'
while (consent != 'n') :
    consent = input("Do you want to add items : ")
    if(consent == 'y'):
        n = int(input("How many items you want to add : "))
        i = 0
        while (i<n) :
            str = input("Enter item : ")
            addItem(list, str)
            i += 1
        displayList(list)
        consent = input("Do you want to add more items : ") 
    else :
        break

consent = 'y'
while (consent != 'n') :
    consent = input("Do you want to remove item : ")
    if(consent == 'y'):
        x = input("Enter item you want to remove : ")
        removeItem(list, x)
        displayList(list)
        consent = input("Do you want to remove more items : ") 
    else :
        break

consent = 'y'
while (consent != 'n') :
    consent = input("Do you want to search item : ")
    if(consent == 'y'):
        s = input("Enter item you want to search : ")
        print(searchItem(list,s))
        consent = input("Do you want to search more item : ")
    else :
        break

def binarySearch(begin, end, list, item1):
    
    list.sort()
    q = False
    size = (begin + end) // 2
    if(list[size] > item1) :
        binarySearch(begin, size -1, list, item1)
    elif(list[size] == item1):
        q = True
    else :
        binarySearch(size + 1, end, list, item1)
    
    if(q):
        s = ""
        for i in range(-1,-len(item1)-1,-1) :
            s += item1[i]
        print("Present")
        print("Reversed string is : ",s)
         
st = input("Enter item you want to search : ")
print(binarySearch(0,len(list),list,st))
