import numpy as np
from hmmlearn import hmm

states = ("cold", "medium", "hot")
observations = ("off", "on")
st_probs = []
trans_probs = [[0.0 for _ in range(3)] for _ in range(3)]
emit_probs = [[0.0 for _ in range(2)] for _ in range(3)]

splitted = input().split(" ")
for i in range(len(splitted)):
    st_probs.append(float(splitted[i]))

for i in range(3):
    splitted = input().split(" ")
    for j in range(len(splitted)):
        trans_probs[i][j] = float(splitted[j])

for i in range(3):
    splitted = input().split(" ")
    for j in range(len(splitted)):
        emit_probs[i][j] = float(splitted[j])

evidence = input().split(" ")
for i in range(len(evidence)):
    evidence[i] = int(evidence[i])

state_probabilities = np.array(st_probs)
transition_probabilities = np.array(trans_probs)
emission_probabilities = np.array(emit_probs)
observations_sequence = np.array(evidence).reshape(-1, 1)

model = hmm.CategoricalHMM(len(states))
model.startprob_ = state_probabilities
model.transmat_ = transition_probabilities
model.emissionprob_ = emission_probabilities
MLS = model.predict(observations_sequence)

final_MLS = []
for i in range(len(MLS)):
    final_MLS.append(states[MLS[i]])

print("Most likely sequence of states:", final_MLS, sep="\n")


def b_prime_cal(trans_probs, current_state, B):
    b_prime = 0.0

    for i in range(3):
        b_prime += trans_probs[i][current_state] * B[i]

    return b_prime


def b_cal(evidence, current_state, trans_probs, emit_probs, B, B_copy):
    b_prime = b_prime_cal(trans_probs, current_state, B)
    b = b_prime * emit_probs[current_state][evidence]
    B_copy[current_state] = b
    return B_copy


B = st_probs.copy()
tmp = B.copy()
for ev in evidence:
    for i in range(len(states)):
        tmp = b_cal(ev, i, trans_probs, emit_probs, B, tmp)
    tot = sum(tmp)
    for i in range(len(tmp)):
        tmp[i] = np.round(tmp[i] / tot, 3)
    B = tmp.copy()

print(B)
