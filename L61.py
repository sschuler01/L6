#the authors' names are: Mac and Serenity

def mood():
    x = input("How is your mood?\n")
    import turtle
    riley = turtle.Turtle()
    riley.width(5)
    riley.speed(0)
    def draw_star(color):
        for side in range(5):
            riley.hideturtle()
            riley.color(color)
            riley.forward(100)
            riley.right(144)
    if x == "happy":
        draw_star("pink")
    elif x == "sad":
        draw_star("blue")
    elif x == "sleepy":
        draw_star("green")
    else:
        draw_star("red")

mood() #testing
