## ◇ Scenario 1: Vignan Campus Map
'''
Context: Each building in a college campus is a node, and walkable paths are edges.
* Represent the campus map using an adjacency list.
* Check if there's a path from the Library to the Auditorium using BFS.
* List all buildings that are directly connected to the Admin Block.
* Use DFS to visit all reachable buildings from the Main Gate.
* Find if there are any disconnected buildings (buildings not connected to campus).
'''
campus={
    "Main Gate" : ["Admin Block"],
    "Admin Block" : ["Main Gate","Library","Canteen","Engineering Block"],
    "Library" : ["Admin Block","Auditorium"],
    "Canteen" : ["Admin Block","Hostel"],
    "Auditorium" : ["Library"],
    "Engineering Block" : ["Admin Block","Science Block"], # Corrected 'Admin block' to 'Admin Block'
    "Science Block" : ["Engineering Block"],
    "Hostel" : ["Canteen"]
}

def bfs(start, target):
    visited = set()
    queue = [start]
    while queue:
        b = queue.pop(0)
        if b == target:
            return True
        if b not in visited:
            visited.add(b) # Corrected visited.pop(b) to visited.add(b)
            for neighbor in campus[b]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return False

def dfs(start, visited=None):
    if visited is None:
        visited = set()
    if start in visited:
        return
    print(start, end= ' ')
    visited.add(start)
    for neighbor in campus[start]: # Corrected campus(start) to campus[start]
        dfs(neighbor, visited)

def disconnected():
    visited = set()
    if campus: # Ensure there's at least one building in the campus
        # Start DFS from the first building in the campus to check connectivity
        dfs(next(iter(campus)), visited)
    return set(campus.keys()) - visited

# --- Execution of Scenario Tasks ---

# 1. Adjacency List
print("1. Campus Map (Adjacency List):")
for building, neighbors in campus.items():
    print(f"{building}: {neighbors}")

# 2. Path from Library to Auditorium using BFS
print("\n2. Is there a path from Library to Auditorium?")
print("Yes" if bfs("Library", "Auditorium") else "No")

# 3. Directly connected to Admin Block
print("\n3. Buildings directly connected to Admin Block:")
print(campus["Admin Block"])

# 4. DFS from Main Gate
print("\n4. DFS from Main Gate (all reachable buildings):")
dfs("Main Gate")

# 5. Disconnected buildings
print("\n\n5. Disconnected buildings in campus:")
d=disconnected()
print(d if d else "None, campus is fully connected")