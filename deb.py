def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 1:
            divisors.append(i)
    return divisors


def run():
    num = int(input('Ingresa un número: '))
    
    print(divisors(num))
    print("Terminó mi programa vuelve a reiniciarlo, por favor, vamos tu puedes")


if __name__ == '__main__':
    run()
