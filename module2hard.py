def generate_password(n):

    pairs = []

    for i in range(1, 11):
        for j in range(i, 20):

            if n % (i + j) == 0 and i < j:
                pairs.append((i, j))

    result = ''.join(f"{i}{j}" for i, j in pairs)

    return result

n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    result = generate_password(n)
    print(f"Нужный пароль: {result}")
else:
    print("Число должно быть в диапазоне от 3 до 20.")