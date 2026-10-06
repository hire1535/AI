def Tower_of_Hanoi(n,source,helper,destination):
    if(n==1):
        print("move disk 1 from ",source ,"to",destination)
        return
    Tower_of_Hanoi(n-1,source,destination,helper)
    print("Move disk",n ,"from ",source,'To',destination)
    Tower_of_Hanoi(n-1,helper,source,destination)
n=3
Tower_of_Hanoi(n,'A','B','C')