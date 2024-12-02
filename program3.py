#python code
def generate_series(a):
    if a <= 2:
        return [1]
    else:
        return [i for i in range(1, 2*a, 2)]

a = int(input("Enter an integer: "))
result = generate_series(a)
print(", ".join(map(str, result)))
