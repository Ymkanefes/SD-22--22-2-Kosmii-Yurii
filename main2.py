def show_console(func):
    def wrapper(width, height):
        result = func(width, height)
        print(f"Площа прямокутника: {result}")
        return result
    return wrapper

@show_console
def get_rectangle_area(width, height):
    return width * height

get_rectangle_area(50, 100)