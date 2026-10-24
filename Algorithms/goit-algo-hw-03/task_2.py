import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def draw_koch_curve(level, size):

    # Налаштування вікна та черепахи
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("The Koch snowflake")

    snowflake = turtle.Turtle()
    snowflake.speed(0)
    snowflake.color("blue")
    snowflake.penup()
    snowflake.goto(-size/2, 150)
    snowflake.pendown()

    # Виклик функції для малювання сніжинки Коха
    for _ in range(3):
        koch_snowflake(snowflake, level, size)
        snowflake.right(120)

    # Закриваємо вікно при кліку
    window.exitonclick()

def main():
    # Введення рівня рекурсії від користувача
    level = int(input("Enter the recursion level for the Koch snowflake fractal: "))
    draw_koch_curve(level, size=300)

if __name__ == "__main__":
    main()
