import random


user_input = input("Enter numbers: ")
user_input_array = [float(x) for x in user_input.split()]
weights = [random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)]
train_inputs = [[1, 2, 3],[3, 3, 3],[2, 2, 2],[1, 1, 1],[10, 10, 10]
]
train_targets = [6,9,6,3,30]
learning_lv = 0.0001

def give_output(user_input_array):
    wynik = user_input_array[0] * weights[0] + user_input_array[1] * weights[1] + user_input_array[2] * weights[2]
    return wynik


def train_model():
    measurement_error = 0
    for epoch in range(2000):
        for i in range(len(train_inputs)):
            przewidywanie = (
                    train_inputs[i][0] * weights[0] +
                    train_inputs[i][1] * weights[1] +
                    train_inputs[i][2] * weights[2]
            )
            measurement_error = train_targets[i] - przewidywanie
            for z in range(3):
                weights[z] += measurement_error * train_inputs[i][z] * learning_lv


train_model()
user_result = give_output(user_input_array)
print("wynik to", user_result)

