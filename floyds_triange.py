"""
Recreate Floyds triangle with lambdas only
"""
print_row = lambda y: print(y+1,end=" ")
make_row = lambda p: list(map(print_row, range(p)))
make_point = lambda l: [make_row(l), print("\n")]
make_triangle_top = lambda w: list(map(make_point, range(w)))
make_triangle_bottom = lambda w: list(map(make_point, range(w)[::-1]))
make_triangle = lambda t: [make_triangle_top(t), make_triangle_bottom(t)]


make_triangle(10)


#  If you want to allow input.....
#  print("Enter a number: ", end="")
#  make_triangle(int(input("")))
