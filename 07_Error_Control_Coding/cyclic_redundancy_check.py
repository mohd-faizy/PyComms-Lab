def xor_division(dividend, divisor):
    dividend = list(map(int, dividend))
    divisor = list(map(int, divisor))
    work = dividend[:]
    n = len(divisor)

    for i in range(len(dividend) - n + 1):
        if work[i] == 1:
            for j in range(n):
                work[i + j] ^= divisor[j]
    return "".join(map(str, work[-(n - 1) :]))


def encode_crc(data, generator):
    padded = data + "0" * (len(generator) - 1)
    remainder = xor_division(padded, generator)
    return data + remainder, remainder


def main():
    data = "1101011011"
    generator = "10011"
    codeword, remainder = encode_crc(data, generator)
    check = xor_division(codeword, generator)

    print(f"Data:      {data}")
    print(f"Generator: {generator}")
    print(f"Remainder: {remainder}")
    print(f"Codeword:  {codeword}")
    print(f"Receiver remainder: {check}")


if __name__ == "__main__":
    main()
