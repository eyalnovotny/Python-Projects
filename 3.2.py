alpha = ["a", "b", "c", "d"]
alpha.append("e")
alpha = alpha + ["f", "g"]
print(alpha)

d_index=alpha.index("d")
print("d_index: " + str(d_index))
del alpha[d_index]
print(alpha)
