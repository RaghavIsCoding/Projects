while True:
    n = input("Enter a number or type \"quit\": ")
    if n.lower() == 'raghav'.lower():
        raise ValueError("Raghav is my name")
    try:
        print(int(n))

    except:
        if n == 'quit':
            break