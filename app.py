from fastapi import FastAPI
import math

app = FastAPI()

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

def is_fibonacci(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

def next_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        a, b = b, a + b
    return a

@app.get("/fibonacci/{n}")
def read_item(n: int):
    if is_fibonacci(n):
        return {"Number": n, "isFibonacci": True, "Next Fibonacci": next_fibonacci(n)}
    else:
        return {"Number": n, "isFibonacci": False, "Message": "Not a Fibonacci number"}

