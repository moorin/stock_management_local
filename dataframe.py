import pandas as pd
import numpy as np
import tkinter
import tkinter.ttk

# index number
number = 0
print(type(number))
# 파일 로드
test_df = pd.read_csv("df_list.csv")
# 인덱스 중복 제거
test_df = test_df.drop(test_df.columns[1], axis=1)

data = {"번호":["0"],"브랜드":["야마하"],"품명":["코리아 뷰 거울"],"종류":["핸들미러"],"개수":[2],"입고가격":["35,676"],"소비자가격":["32,000"],"위치":["창고"],"품목코드":["A100"]}

df_list = pd.DataFrame(data, columns = ["번호","브랜드","품명","종류","개수","입고가격","소비자가격","위치","품목코드"])
df_list.info(memory_usage='deep')
# GUI
window=tkinter.Tk()
window.geometry("1000x600")

# 텍스트들

brand = tkinter.Label(window, text="브랜드").grid(row=0, column=1)
item_name = tkinter.Label(window, text="품명").grid(row=0, column=2)
item_category = tkinter.Label(window, text="종류").grid(row=0, column=3)
item_count = tkinter.Label(window, text="개수").grid(row=0, column=4)
wearing_price = tkinter.Label(window, text="입고가격").grid(row=0, column=5)
retail_price = tkinter.Label(window, text="소비자가격").grid(row=0, column=6)
item_loc = tkinter.Label(window, text="위치").grid(row=0, column=7)
item_code = tkinter.Label(window, text="품목코드").grid(row=0, column=8)
modify_index = tkinter.Label(window, text="수정할 품목 번호").grid(row=0, column=9)
del_index = tkinter.Label(window, text="삭제할 품목 번호").grid(row=0, column=10)
search_item = tkinter.Label(window, text="품목 검색").grid(row=0, column=11)

# 엔트리들

entry_brand = tkinter.Entry(window, width = 10)
entry_brand.grid(row=1, column=1)
entry_item_name = tkinter.Entry(window, width = 10)
entry_item_name.grid(row=1, column=2)
entry_item_category = tkinter.Entry(window, width = 10)
entry_item_category.grid(row=1, column=3)
entry_item_count = tkinter.Entry(window, width = 10)
entry_item_count.grid(row=1, column=4)
entry_wearing_price = tkinter.Entry(window, width = 10)
entry_wearing_price.grid(row=1, column=5)
entry_retail_price = tkinter.Entry(window, width = 10)
entry_retail_price.grid(row=1, column=6)
entry_item_loc = tkinter.Entry(window, width = 10)
entry_item_loc.grid(row=1, column=7)
entry_item_code = tkinter.Entry(window, width = 10)
entry_item_code.grid(row=1, column=8)
entry_modify_index = tkinter.Entry(window, width = 10)
entry_modify_index.grid(row=1, column=9)
entry_del_index = tkinter.Entry(window, width = 10)
entry_del_index.grid(row=1, column=10)
entry_search_item = tkinter.Entry(window, width = 10)
entry_search_item.grid(row=1, column=11)

def data_add(event):
    global number

    try:
        number = int(number)
        number += 1
    except TypeError:
        print("type error")
        number = 1

    brand = entry_brand.get()
    item_name = entry_item_name.get()
    item_category = entry_item_category.get()
    item_count = entry_item_count.get()
    wearing_price = entry_wearing_price.get()
    retail_price = entry_retail_price.get()
    item_loc = entry_item_loc.get()
    item_code = entry_item_code.get()

    input_data = [number,brand,item_name,item_category,item_count,wearing_price,retail_price,item_loc,item_code]
    df_list.loc[len(df_list),:] = input_data
    
    treeview.insert('', 'end', text="", values=[number,brand,item_name,item_category,item_count,wearing_price,retail_price,item_loc,item_code])
    print(df_list)

def data_del(event):

    global number
    
    #df 에서 삭제
    global df_list
    del_index = int(entry_del_index.get())
    df_list=df_list.drop(del_index)

    # df 인덱스 리셋
    df_list = df_list.reset_index()
    del df_list['index']

    for i in range(len(treeview.get_children())):
        df_list['번호'][i] = i

    print("test: ",treeview.item(treeview.selection()))

    # df number 리셋


    #del_index = treeview.get_children()[del_index]

    #treeview 에서 삭제
    number -= 1
    values_list = []

    for i in range(len(treeview.get_children())-del_index):
        if i == 0:
            child_id = treeview.get_children()[del_index]
            treeview.delete(child_id)
        else:
            #print(len(treeview.get_children()), " ~ ", len(treeview.get_children()) - del_index, " / ", del_index + i-1)

            child_id = treeview.get_children()[del_index+i-1]
            values_list.append(treeview.item(child_id)["values"])

            values_list[i-1][0] -= 1
            #print("===> ",values_list[del_index-2+i])
            treeview.item(child_id, values=(values_list[del_index-2+i]))  # 핵심

    # brand,item_name,item_category,item_count,wearing_price,retail_price,item_loc,item_code,modify_index,del_index

    print(df_list)


def data_modify(evnet):

    input_values = []; input_values.append(entry_number.get())
    input_values.append(entry_brand.get());input_values.append(entry_item_name.get())
    input_values.append(entry_item_category.get());input_values.append(entry_item_count.get())
    input_values.append(entry_wearing_price.get());input_values.append(entry_retail_price.get())
    input_values.append(entry_item_loc.get());input_values.append(entry_item_code.get())
    
    # treeview에서 바뀌게 하기
    brand = entry_brand.get()
    item_name = entry_item_name.get()
    modify_index = int(entry_modify_index.get())

    # 구현할것: 원래는 다 입력해야하는데 바뀐것만 입력해도 원래 있는거 유지되게 하기
    child_id = treeview.get_children()[modify_index] # 핵심
    
    tmp_save_data = []
    i = 0
    for value in input_values:
        # 값이 없다면 원래 있던 값 입력
        if value == "":
            tmp_save_data.append(treeview.item(child_id)["values"][i])
        # 값이 있다면 입력한 값 입력
        else:
            tmp_save_data.append(value)
        i += 1
    
    # brand,item_name,item_category,item_count,wearing_price,retail_price,item_loc,item_code,modify_index,del_index
    treeview.item(child_id,values=(tmp_save_data)) # 핵심

    # df_list에서 바뀌게 하기
    for item,input_value,tmp_data in zip(list(df_list),input_values, tmp_save_data):
        # 값이 없다면 원래 있던 값 입력
        if value == "":
            df_list.loc[modify_index,item] = tmp_data
        # 값이 있다면 입력한 값 입력
        else:
            df_list.loc[modify_index,item] = input_value
    print(df_list)

    print()
    
    
def data_save(event):
    df_list.to_csv('df_list.csv',encoding='utf-8-sig')

def data_search(event):
    search_item = entry_search_item.get()
    searched_item = []
    searched_item_code = []
    
    i=0
    
    print(len(df_list))
    while i <= len(df_list)-1:
        if search_item in df_list.loc[i,"품명"]:
            searched_item.append(df_list.loc[i,"품명"])
            searched_item_code.append(df_list.loc[i,"번호"])

        i += 1
        
    print()
    # 품목 검색의 결과들의 브랜드, 품명, 종류, ...을 검색 창을 띄우기

    

    # 새 창 띄우기
    searched_window = tkinter.Toplevel(window)

    searched_treeview = tkinter.ttk.Treeview(searched_window, columns=["번호","브랜드","품명","종류","개수","입고가격","소비자가격","위치","품목코드"],displaycolumns=["번호","브랜드","품명","종류","개수","입고가격","소비자가격","위치","품목코드"])
    searched_treeview.grid(row=0, column=0)

    searched_treeview.column("#0", width=0)
    searched_treeview.heading("#0")

    searched_treeview.column("번호", width=70, anchor="center")
    searched_treeview.heading("번호", text="번호", anchor="center")
    searched_treeview.column("브랜드", width=100, anchor="center")
    searched_treeview.heading("브랜드", text="브랜드", anchor="center")
    searched_treeview.column("품명", width=130, anchor="center")
    searched_treeview.heading("품명", text="품명", anchor="center")
    searched_treeview.column("종류", width=100, anchor="center")
    searched_treeview.heading("종류", text="종류", anchor="center")
    searched_treeview.column("개수", width=100, anchor="center")
    searched_treeview.heading("개수", text="개수", anchor="center")
    searched_treeview.column("입고가격", width=100, anchor="center")
    searched_treeview.heading("입고가격", text="입고가격", anchor="center")
    searched_treeview.column("소비자가격", width=100, anchor="center")
    searched_treeview.heading("소비자가격", text="소비자가격", anchor="center")
    searched_treeview.column("위치", width=100, anchor="center")
    searched_treeview.heading("위치", text="위치", anchor="center")
    searched_treeview.column("품목코드", width=100, anchor="center")
    searched_treeview.heading("품목코드", text="품목코드", anchor="center")

 
    df_list_searched = pd.DataFrame()

    for i in range(len(searched_item_code)):
        df_list[df_list['번호'] == searched_item_code[i]]
        df_list_searched = pd.concat([df_list_searched,df_list[df_list['번호'] == searched_item_code[i]]])
        
    searched_list = df_list_searched.values.tolist()
    
    i = 0
    for i in range(len(searched_list)):
        searched_treeview.insert('', 'end', text=i, values=searched_list[i], iid=str(i)+"번:")
        i+=1
  
# 버튼들
btn_add = tkinter.Button(window, text="추가")
btn_add.grid(row=2, column=1)
btn_add.bind('<Button-1>',data_add)

btn_del = tkinter.Button(window, text="삭제")
btn_del.grid(row=2, column=10)
btn_del.bind('<Button-1>',data_del)

btn_modify = tkinter.Button(window, text="수정")
btn_modify.grid(row=2, column=9)
btn_modify.bind('<Button-1>',data_modify)

btn_save = tkinter.Button(window, text="저장")
btn_save.grid(row=2, column=3)
btn_save.bind('<Button-1>',data_save)

btn_search_item = tkinter.Button(window, text="검색")
btn_search_item.grid(row=2, column=11)
btn_search_item.bind('<Button-1>',data_search)

# 데이터 추가
'''
input_brand = input("input brand")
input_category = input("input category")
input_inprice = input("input inprice")
'''
#print(len(df_list))
#df_list.loc[len(df_list),:] = ["야마하","순정 부품 오일 필터","엔진부품","4","10,448","9,000","A 2번째 서랍","B100"]

# 데이터 수정, index만 잘 써주면 됨
#df_list.loc[1,:] = ["d","E","T"]

print(df_list)


# 표
# 데이터 프레임에서 정보 가져오기
treeview = tkinter.ttk.Treeview(window, columns=["번호","브랜드","품명","종류","개수","입고가격","소비자가격","위치","품목코드"],displaycolumns=["번호","브랜드","품명","종류","개수","입고가격","소비자가격","위치","품목코드"])
treeview.grid(row=4, columnspan=36)

treeview.column("#0", width=0)
treeview.heading("#0")

treeview.column("번호", width=70, anchor="center")
treeview.heading("번호", text="번호", anchor="center")
treeview.column("브랜드", width=100, anchor="center")
treeview.heading("브랜드", text="브랜드", anchor="center")
treeview.column("품명", width=130, anchor="center")
treeview.heading("품명", text="품명", anchor="center")
treeview.column("종류", width=100, anchor="center")
treeview.heading("종류", text="종류", anchor="center")
treeview.column("개수", width=100, anchor="center")
treeview.heading("개수", text="개수", anchor="center")
treeview.column("입고가격", width=100, anchor="center")
treeview.heading("입고가격", text="입고가격", anchor="center")
treeview.column("소비자가격", width=100, anchor="center")
treeview.heading("소비자가격", text="소비자가격", anchor="center")
treeview.column("위치", width=100, anchor="center")
treeview.heading("위치", text="위치", anchor="center")
treeview.column("품목코드", width=100, anchor="center")
treeview.heading("품목코드", text="품목코드", anchor="center")
print("=============")

data_list = df_list.values.tolist()

for i in range(len(data_list)):
    treeview.insert('', 'end', text=str(i), values=data_list[i], iid=str(i)+"번:")
    # [야마하, 핸드미러, ...]
print(treeview['columns'])
window.mainloop()