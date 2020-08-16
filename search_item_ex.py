color_list = ["pink","hotpink","green","light green","blue","sky blue","indigo"]
result_list = []

input_value = input("검색할 단어를 입력하세요: ")


for s in color_list:
    if input_value in s:
        result_list.append(s)

print(result_list)
