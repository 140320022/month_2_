#binerry search
def binerry_search(a,val):
    N = len(a)
    ResultOk = False
    Pos = 0
    First = 0
    Last = N - 1
    while First < Last:
            Middle = (First+Last) // 2
            if val == a[Middle]:
                First = Middle
                Last = First
                ResultOk = True
                Pos = Middle
            elif val > a[Middle]:
                First = Middle + 1
            else:
                Last = Middle - 1
    if ResultOk == True:
        print(f"Element is find {Pos}")
    else:
        print(f"element is doesn't found")
topic =[1,2,3,4,5,6,7,8,9]
number = 2
binerry_search(topic,number)

#buble sort
def bubble_sort(human):
    for q in range(len(human) - 1):
        for m in range(len(human) - 1 - q):
            if human[m] > human[m + 1]:
                word  = human[m]
                human[m] = human[m + 1]
                human[m + 1] = word
    return human

print(bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))