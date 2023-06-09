import turtle
import pandas


def main():
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()
    guessed_states = []

    while len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                        prompt="What's another state's name?").title()
        if answer_state == "Exit":
            missing_states = [state for state in all_states if state not in guessed_states]
            save_missing_states(missing_states)
            break
        if answer_state in all_states:
            guessed_states.append(answer_state)
            write_state_name(answer_state, data)


def write_state_name(state_name, data):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == state_name]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(state_name)


def save_missing_states(missing_states):
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")


main()
