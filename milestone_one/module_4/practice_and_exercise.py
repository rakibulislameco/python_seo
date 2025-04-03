# store = [
#     [101, 'Laptop', 999],
#     [102, 'Smartphone', 599],
#     [103, 'Tablet', 299],
#     [104, 'Keyboard', 49],
#     [105, 'Mouse', 19]
# ]
# smartphone_price = store[2][2]
# store_item_name = store[2][1]
# print(store_item_name, smartphone_price)

student_info = [
    [101, 'Jhon Doe', ['Python Basic', 'Python For SEO']],
    [102, 'Jhon Smith', ['Python Basic']],
    [102, 'Doe Smith', ['Basic HTML','Basic Python']]
]

student_1 = student_info[0][1]
student_2 = student_info[1][1]
student_3 = student_info[2][1]


student_1_course = student_info[0][2][1]
student_2_course = student_info[1][2][0]
student_3_course = student_info[2][2][0]



print("\n",student_1,student_1_course,"\n",student_2, student_2_course,"\n", student_3, student_3_course)