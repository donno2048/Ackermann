def ack(x, y):
    assert x + y == abs(x + y)
    return y + 1 if not x else (ack(x - 1, 1) if not y else ack(x - 1, ack(x, y - 1)))
