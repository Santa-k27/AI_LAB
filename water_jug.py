from collections import deque

def water_jug_BFS(x, y, z):
    visited = set()
    queue = deque([(0, 0, "")])  
    while queue:
        jug_a, jug_b, path = queue.popleft()  
        
        if jug_a == z or jug_b == z or jug_a + jug_b == z:
            print(f'Steps:\n {path}')  
            return True

        if (jug_a, jug_b) in visited:
            continue

        visited.add((jug_a, jug_b))

        # Fill jug A
        if jug_a < x:
            queue.append((x, jug_b, path + "Fill jug A\n ")) 

        # Fill jug B
        if jug_b < y:
            queue.append((jug_a, y, path + "Fill jug B\n ")) 

        # Empty jug A
        if jug_a > 0:
            queue.append((0, jug_b, path + "Empty jug A\n"))  

        # Empty jug B
        if jug_b > 0:
            queue.append((jug_a, 0, path + "Empty jug B\n "))  

        # Pour from A to B
        if jug_a + jug_b >= y:
            queue.append((jug_a - (y - jug_b), y, path + "Pour from A to B\n ")) 
        else:
            queue.append((0, jug_a + jug_b, path + "Pour from A to B\n "))  

        # Pour from B to A
        if jug_a + jug_b >= x:
            queue.append((x, jug_b - (x - jug_a), path + "Pour from B to A\n ")) 
        else:
            queue.append((jug_a + jug_b, 0, path + "Pour from B to A\n "))  

    return False

x = int(input("Enter the capacity of the first jug: "))
y = int(input("Enter the capacity of the second jug: "))
z = int(input("Enter the required amount of water: "))

if water_jug_BFS(x, y, z):
    print(f'You can measure {z} liters of water using {x}-liter and {y}-liter jugs.')
else:
    print(f'You cannot measure {z} liters of water using {x}-liter and {y}-liter jugs.')
