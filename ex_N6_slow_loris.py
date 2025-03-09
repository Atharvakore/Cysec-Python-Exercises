def slow_loris(message: str, chunksize: int) -> str:
    result = ""
    for chunkstart in range(0, len(message), chunksize):
        chunk = message[chunkstart:chunkstart+chunksize]
        result += f"{len(chunk):x}\n{chunk}\n"
    result += "0"
    return result

if __name__ == '__main__':
    assert slow_loris("Hello World", 2) == '2\nHe\n2\nll\n2\no \n2\nWo\n2\nrl\n1\nd\n0'
    assert slow_loris("Hello World", 10) == 'a\nHello Worl\n1\nd\n0'