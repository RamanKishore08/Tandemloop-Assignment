#python code
def generate_series(a):
    series = []
    for i in range(1, a * 2, 2):
        series.append(i)
    return series

a = int(input("Enter an integer: "))
result = generate_series(a)
print(", ".join(map(str, result)))