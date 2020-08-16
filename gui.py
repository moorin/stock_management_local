import tkinter
import tkinter.ttk

window=tkinter.Tk()
window.geometry("800x600")


# 텍스트들
brand = tkinter.Label(window, text="브랜드").grid(row=0, column=0)
item_name = tkinter.Label(window, text="품명").grid(row=0, column=1)
item_category = tkinter.Label(window, text="종류").grid(row=0, column=2)
item_count = tkinter.Label(window, text="개수").grid(row=0, column=3)
wearing_price = tkinter.Label(window, text="입고가격").grid(row=0, column=4)
retail_price = tkinter.Label(window, text="소비자가격").grid(row=0, column=5)
item_loc = tkinter.Label(window, text="위치").grid(row=0, column=6)
item_code = tkinter.Label(window, text="품목코드").grid(row=0, column=7)

'''
brand.pack()
item_name.pack()
item_category.pack()
item_count.pack()
wearing_price.pack()
retail_price.pack()
item_loc.pack()
item_code.pack()
'''


# 엔트리들
entry_brand = tkinter.Entry(window, width = 10).grid(row=1, column=0)
entry_item_name = tkinter.Entry(window, width = 10).grid(row=1, column=1)
entry_item_category = tkinter.Entry(window, width = 10).grid(row=1, column=2)
entry_item_count = tkinter.Entry(window, width = 10).grid(row=1, column=3)
entry_wearing_price = tkinter.Entry(window, width = 10).grid(row=1, column=4)
entry_retail_price = tkinter.Entry(window, width = 10).grid(row=1, column=5)
entry_item_loc = tkinter.Entry(window, width = 10).grid(row=1, column=6)
entry_item_code = tkinter.Entry(window, width = 10).grid(row=1, column=7)

'''
label=tkinter.Label(window, text="파이썬")
b1=tkinter.Button(window, text="(50, 50)")
b1.place(x=50, y=50)
label.place(x=100, y=100)

entry_brand.pack()
entry_item_name.pack()
entry_item_category.pack()
entry_item_count.pack()
entry_wearing_price.pack()
entry_retail_price.pack()
entry_item_loc.pack()
entry_item_code.pack()
'''

# 버튼들
btn_add = tkinter.Button(window, text="추가").grid(row=2, column=0)
btn_del = tkinter.Button(window, text="삭제").grid(row=2, column=1)
btn_modify = tkinter.Button(window, text="수정").grid(row=2, column=2)
btn_save =tkinter.Button(window, text="저장").grid(row=2, column=3)

# 표
# 데이터 프레임에서 정보 가져오기
treeview = tkinter.ttk.Treeview(window, columns=["브랜드","품명","종류","개수","입고가격","소비자가격","위치","품목코드"],displaycolumns=["브랜드","품명","종류","개수","입고가격","소비자가격","위치","품목코드"]).grid(row=4,columnspan=32)
treeview.column("#0", width=70)

# window.mainloop()
