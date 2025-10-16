import turtle
import pandas


screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

turtle = turtle.Turtle()
turtle.penup()
turtle.hideturtle()

states_data = pandas.read_csv('50_states.csv')
states = states_data['state']

def draw_state(answer_state, state_x_cor, state_y_cor):
    turtle.goto(state_x_cor, state_y_cor)
    turtle.write(answer_state, align='center', font=('Courier', 8 , 'normal'))

game_is_on = True
score = 0
correct_guesses = []
while game_is_on:
    answer_state = screen.textinput(title=f'{score}/50 States Correct', prompt="What's another state's name")
    if answer_state.lower() in (s.lower() for s in states) and answer_state.lower() not in correct_guesses:
        score += 1
        correct_guesses.append(answer_state.lower())
        reformat_answer_state = answer_state.title()
        answer_state_data = states_data[states_data['state'] == reformat_answer_state]

        answer_state_x_cor = answer_state_data.x.iat[0]
        answer_state_y_cor = answer_state_data.y.iat[0]
        draw_state(reformat_answer_state, answer_state_x_cor, answer_state_y_cor)

    if answer_state.title() == 'Exit':
        break

states_to_learn = []
for state in states:
    if state not in correct_guesses:
        states_to_learn.append(state)

df = pandas.DataFrame(states_to_learn)
df.to_csv('states_to_learn.csv')