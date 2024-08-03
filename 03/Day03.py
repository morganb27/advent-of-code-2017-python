PUZZLE = 312051

def spiral_matrix(n):
    layers = []
    for i in range(1, 300):
        layer = []
        high = (2 * i + 1)**2
        low = (2 * i - 1)**2
        if n <= high and n >= low + 1:
            print(low, high, i)
        for num in range(low + 1, high + 1):
            layer.append(num)
        layers.append(layer)
        if n in layer:
            print("i", i)


print(spiral_matrix(PUZZLE))