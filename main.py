import turtle
import pandas

screen = turtle.Screen()

screen.title("Waifu Game")
image = "anime.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("waifu_name.csv")
all_name = data.waifu.to_list()
guessed_names = []

while len(guessed_names) < 12:
    answer_name = screen.textinput(title=f"{len(guessed_names)}/12 Waifus Done",
                                       prompt="Enter Waifu name?").title()
    print(answer_name)

    if answer_name in all_name:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        waifu_data = data[data.waifu == answer_name]
        t.goto(int(waifu_data.x), int(waifu_data.y))
        t.write(answer_name, font = ("Arial", 12, "bold"))
        guessed_names.append(answer_name)






