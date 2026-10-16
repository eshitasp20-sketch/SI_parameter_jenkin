import sys
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

if __name__ == "main":
    p = int(sys.argv[1])
    r = int(sys.argv[2])
    t = int(sys.argv[3])

print("Simple interest: ",(p,r,t))