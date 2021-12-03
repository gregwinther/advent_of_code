import numpy as np 

data = np.loadtxt("./input_03.txt", dtype=str)
data = np.array(list(map(list, data)), dtype=int)

gamma_rate = np.round(data.sum(axis=0) / data.shape[0]).astype(int)
epsilon_rate = np.logical_not(gamma_rate).astype(int)

gamma_rate = int("".join(list(gamma_rate.astype(str))), 2)
epsilon_rate = int("".join(list(epsilon_rate.astype(str))), 2)

print(f"Answer, part I: {gamma_rate * epsilon_rate}")

# Part II
_, n = data.shape

## Oxy gen
oxy_gen = data.copy()
for i in range(n):
    bits_in_place_i = oxy_gen[:, i]
    m = len(bits_in_place_i)
    n_ones = np.sum(bits_in_place_i)
    if m <= 1:
        break
    n_zeros = m - n_ones
    if n_ones >= n_zeros:
        oxy_gen = oxy_gen[oxy_gen[:, i] == 1, :]
    else:
        oxy_gen = oxy_gen[oxy_gen[:, i] == 0, :]

oxy_gen = int("".join(list(oxy_gen.flatten().astype(str))), 2)

## CO2 Scrubber
co2 = data.copy()
for i in range(n):
    bits_in_place_i = co2[:, i]
    m = len(bits_in_place_i)
    n_ones = np.sum(bits_in_place_i)
    if m <= 1:
        break
    n_zeros = m - n_ones
    if n_ones >= n_zeros:
        co2 = co2[co2[:, i] == 0, :]
    else:
        co2 = co2[co2[:, i] == 1, :]

co2 = int("".join(list(co2.flatten().astype(str))), 2)

print(f"Ansver, part II: {oxy_gen * co2}")