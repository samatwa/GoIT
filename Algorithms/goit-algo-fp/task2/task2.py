import turtle
import math

# Функція для малювання дерева Піфагора


def draw_pythagoras_tree(t, branch_length, level):
    """Аргументи: t - об'єкт черепашки, branch_length - довжина гілки, level - поточний рівень рекурсії"""
    if level == 0:
        return

    # Малюємо основну гілку
    t.forward(branch_length)

    # Малюємо праву піддереву
    t.left(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2)/2, level - 1)
    t.right(45)

    # Малюємо ліву піддереву
    t.right(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2)/2, level - 1)
    t.left(45)

    # Повертаємося до початкової позиції
    t.backward(branch_length)


def main():
    # Запитуємо рівень рекурсії у користувача
    level = int(input("Enter the level of recursion: "))

    # Налаштовуємо екран
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Налаштовуємо черепашку
    t = turtle.Turtle()
    t.color("green")
    t.speed(0)
    t.left(90)  # Повертаємо черепашку вгору

    # Переміщуємо черепашку до кращої стартової позиції
    t.penup()
    t.goto(0, -100)
    t.pendown()

    # Малюємо дерево
    draw_pythagoras_tree(t, 100, level)

    # Завершення
    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()
