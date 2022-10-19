# Task 1 create a geometric progression generator

def geometric_progression(current_number, denominator):
    while True:
        yield current_number
        current_number *= denominator


progression = geometric_progression(current_number=5, denominator=4)
for i in range(10):
    print(next(progression))
