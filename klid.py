import math

# Noktalar listesinin tanımlanması
points = [(1, 2), (3, 4), (6, 8), (7, 1)]

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Mesafelerin saklanacağı liste
distances = []

# Tüm nokta çiftleri arasındaki mesafelerin hesaplanması
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Her çifti bir kez hesaplamak için
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)

# Sonuçların yazdırılması
print(f"Noktalar: {points}")
print(f"Mesafeler: {distances}")
print(f"Minimum mesafe: {min_distance}")
