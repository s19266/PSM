import math
import sys

factorial_memo = {}

def factorial(n):
  if n in factorial_memo:
    return factorial_memo[n]
  
  if n == 0:
    return 1
  return factorial(n-1) * n

def normalize_x(x: float) -> float:
  m_x = x % (2 * math.pi)

  if m_x <= 0.5 * math.pi:
    return m_x
  if m_x <= math.pi:
    return math.pi - m_x
  if m_x <= 1.5 * math.pi:
    return m_x - 2 * math.pi

  return 2 * math.pi - m_x

def sin_part(x: float, n: int) -> float:
  m = 2 * n -1
  n_sign = -1 if n % 2 == 0 else 1
  num = x ** m
  den = factorial(m)

  return n_sign * (num / den)

def sin(x: float, precision: int) -> float:
  norm_x = normalize_x(x)
  sum = norm_x

  count = 2
  for i in range(count, precision + 1):
    part = sin_part(norm_x, i)
    
    sum += part
  return sum

def format_n(n: float) -> float:
  # return print("{:.14f}".format(round(n, 14))).rjust(16, "0").rjust(17, " ")
  return "{:2.16f}".format(round(n, 16))

def deg_rad(deg: float) -> float:
  return (deg / 180) * math.pi

def parse_inputs():
  input_val = float(sys.argv[1])
  input_unit = sys.argv[2].lower()

  if not (input_unit == "deg" or input_unit == "rad"):
    print(f"Input unit written '{input_unit}' is not accepted: Accepted values: 'deg' or 'rad'")
    print(f"Usage: python3 ./main.py 2.2 rad")
    sys.exit()

  if input_unit == "rad":
    return input_val

  return deg_rad(input_val)

x = parse_inputs()

print()
print(f"x value: {x}")
print(f"╔══════╦════════════════════╦════════════════════╦════════════════════╗")
print(f"║  p   ║     math.sin       ║       Taylor       ║       Delta        ║")
print(f"╠══════╬════════════════════╬════════════════════╬════════════════════╣")
recurrences = 10
for i in range(1, recurrences + 1):
  math_sin = math.sin(x)
  calc_taylor = sin(x, i)
  calc_delta = abs(math_sin - calc_taylor)
  print(f"║  {'{:<2}'.format(i)}  ║ {format_n(math_sin)} ║ {format_n(calc_taylor)} ║ {format_n(calc_delta)} ║")

  print(f"╠══════╬════════════════════╬════════════════════╬════════════════════╣") if i != recurrences else print(f"╚══════╩════════════════════╩════════════════════╩════════════════════╝")
# print(f"║      ║                   ║                   ║                   ║")

