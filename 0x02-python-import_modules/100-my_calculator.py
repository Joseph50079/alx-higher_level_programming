#!/usr/bin/python3

import calculator_1 as cal

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == "+":
        val = cal.add(a, b)
    elif sys.argv[2] == "-":
        val = cal.sub(a, b)
    elif sys.argv[2] == "*":
        val = cal.mul(a, b)
    elif sys.argv[2] == "/":
        val = cal.div(a, b)
    else:
        print(f"Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{:d} {} {:d} = {:d}".format(a, sys.argv[2], b, val))
