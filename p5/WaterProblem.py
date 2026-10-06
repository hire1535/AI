from collections import deque
def water(jug1,jug2,Targer):
    queue=deque([(0,0)])
    visited=set()
    while queue:
        a,b=queue.popleft()
        if (a,b) in visited:
            continue
        visited.add((a,b))
        print("current state",(a,b))
        if(a==Targer or b==Targer):
            print("Target Fourd")
            return
        states=[
            (jug1,b),
            (a,jug2),
            (0,b),
            (a,0),
            (
                a-min(a,jug2-b),
                b+min(a,jug2-b)
            ),
            
             (
                            a+min(b,jug1-a),
                            b-min(b,jug1-a)
           )
           
        ]
        for state in states:
            if state not in visited:
                queue.append(state)
        
    
water(4,3,2)