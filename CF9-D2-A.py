yakko_points, wakko_points = map(int, input().split())
higher_points_amount = yakko_points if yakko_points > wakko_points else wakko_points
numerator = 6 - higher_points_amount + 1
denominator = 6
if numerator % 2 == 0:
    numerator //= 2
    denominator //= 2
if numerator % 3 == 0:
    numerator //= 3
    denominator //= 3
print(f'{numerator}/{denominator}')
