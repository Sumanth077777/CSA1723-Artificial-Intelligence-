import itertools

def calculate_distance(points):
    total_distance = 0
    num_points = len(points)
    for i in range(num_points):
        total_distance += distance(points[i], points[(i+1) % num_points])
    return total_distance

def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5

def traveling_salesman_brute_force(points):
    min_distance = float('inf')
    best_path = None
    num_points = len(points)
    
    for perm in itertools.permutations(points):
        current_distance = calculate_distance(perm)
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = perm
            
    return best_path, min_distance

# Get input from the user
num_cities = int(input("Enter the number of cities: "))
points = []
for i in range(num_cities):
    x, y = map(int, input(f"Enter coordinates for city {i+1} (x y): ").split())
    points.append((x, y))

# Calculate TSP solution
best_path, min_distance = traveling_salesman_brute_force(points)

# Output the result
print("Best Path:", best_path)
print("Minimum Distance:", min_distance)
