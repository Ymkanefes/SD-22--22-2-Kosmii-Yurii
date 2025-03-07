def function_decorator(fu):
    def wrapper():
        print("До виклику функції")
        a, b, result = fu()
        print("Після виклику функції")
        print(f"Сума {result}")
    return wrapper

@function_decorator
def my_fu():
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    return a, b, a + b

if __name__ == "__main__":
    my_fu()
