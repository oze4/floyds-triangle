"""
Recreate Floyds triangle with lambdas only
"""
print_row = lambda y: print(y+1,end=" ")
make_row = lambda p: list(map(print_row, range(p)))
make_point = lambda l: [make_row(l), print("\n")]
make_triangle_top = lambda w: list(map(make_point, range(w)))
make_triangle_bottom = lambda w: list(map(make_point, range(w)[::-1]))
make_triangle = lambda t: [make_triangle_top(t), make_triangle_bottom(t)]

"""
If you want to allow input, uncomment the two lines below
    and comment out the line below them.....
"""
#  print("Enter a number: ", end="")
#  make_triangle(int(input("")))


make_triangle(10)


""" OUTPUT
1

1 2

1 2 3

1 2 3 4

1 2 3 4 5

1 2 3 4 5 6

1 2 3 4 5 6 7

1 2 3 4 5 6 7 8

1 2 3 4 5 6 7 8 9

1 2 3 4 5 6 7 8 9

1 2 3 4 5 6 7 8

1 2 3 4 5 6 7

1 2 3 4 5 6

1 2 3 4 5

1 2 3 4

1 2 3

1 2

1
"""
