f = open("day2.txt", "r")
data = f.readlines()
f.close()
# scores = 0
# for round in data:
#     score = 0
#     p1, p2 = round.strip().split(" ")
#     if p1 == "A":
#         if p2 == "X":
#             score = 1 + 3
#         elif p2 == "Y":
#             score = 2 + 6
#         else:
#             score = 3
#     elif p1 == "B":
#         if p2 == "X":
#             score = 1
#         elif p2 == "Y":
#             score = 2 + 3
#         else:
#             score = 3 + 6
#     else:
#         if p2 == "X":
#             score = 1 + 6
#         elif p2 == "Y":
#             score = 2
#         else:
#             score = 3 + 3
#     print(round.strip(), score)
#     scores += score
# print(scores)
scores = {"A": 1, "B": 2, "C": 3}
scenario = {"X": {"A": "C", "B": "A", "C": "B"}, 
            "Y": {"A": "A", "B": "B", "C": "C"}, 
            "Z": {"A": "B", "B": "C", "C": "A"}}
scenario_pts = {"X": 0, "Y": 3, "Z": 6}
score = 0
for round in data:
    p1, p2 = round.strip().split(" ")
    score += scenario_pts[p2] + scores[scenario[p2][p1]]
print(score)