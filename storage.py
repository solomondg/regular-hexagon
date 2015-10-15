
# # print (test_case.chromosone)
# # print (evaluator(test_case))

# start_time = time.time()
#
# val_list = []
# n = 2 ** 20
# lastnum = 0
# tempdict = {150: "F", 120: "E", 90: "D", 60: "C", 30: "B", 0: "A"}
#
# for x in range(0, n):
#     val_list += fitness_select(tempdict)
#
#     if round((x / float(n)*100)) != lastnum:
#         lastnum = int(round((x / float(n))*100))
#         print(str(lastnum) + "%  done")
#
# a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
# for x in val_list:
#     if x == 'A':
#         a += 1
#     elif x == 'B':
#         b += 1
#     elif x == 'C':
#         c += 1
#     elif x == 'D':
#         d += 1
#     elif x == 'E':
#         e += 1
#     elif x == 'F':
#         f += 1
#
#print("A occured " + str(a) + " times, " +
#      str(int(round(float(a)/(a + b + c + d + e + f)*100))) + "% of all times")
#print("B occured " + str(b) + " times, " +
#      str(int(round(float(b)/(a + b + c + d + e + f)*100))) + "% of all times")
#print("C occured " + str(c) + " times, " +
#      str(int(round(float(c)/(a + b + c + d + e + f)*100))) + "% of all times")
#print("D occured " + str(d) + " times, " +
#      str(int(round(float(d)/(a + b + c + d + e + f)*100))) + "% of all times")
#print("E occured " + str(e) + " times, " +
#      str(int(round(float(e)/(a + b + c + d + e + f)*100))) + "% of all times")
#print("F occured " + str(f) + " times, " +
#       str(int(round(float(f)/(a + b + c + d + e + f)*100))) + "% of all times")
#print(fitness_select({360:"F", 288: "E", 216: "D", 144: "C", 72: "B",
#                      0: "A"}))
#
# print("--- %s ---" % (time.time() - start_time) + " Seconds")
