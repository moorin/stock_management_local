import tkinter
import tkinter.ttk

def modify_item(a):
    brand = entry_brand.get()
    item_name = entry_item_name.get()
    modify_index = int(entry_modify_index.get())
    
    child_id = treeview.get_children()[modify_index] # 핵심
    treeview.item(child_id,values=(brand,item_name)) # 핵심

# 창
window=tkinter.Tk()
window.geometry("1000x300")

# 트리뷰

treeview = tkinter.ttk.Treeview(window, columns=("브랜드","품명"), displaycolumns=("브랜드","품명"))

treeview.column("브랜드", width=100, anchor="center")
treeview.heading("브랜드", text="브랜드", anchor="center")
treeview.column("품명", width=100, anchor="center")
treeview.heading("품명", text="품명", anchor="center")

treeview.insert('', 'end', text="내 노트북 1", values=("Lenovo","Y520"))
treeview.insert('','end',text="내 노트북 2",values=("Apple","Mac Book Air"))


treeview.grid(row=3, columnspan=16)
#treeview.pack()



# 버튼
btn_modify = tkinter.Button(window, text="수정")
btn_modify.grid(row=2,column=0)
btn_modify.bind('<Button-1>', modify_item)
#btn_modify.pack()

# 텍스트들
brand = tkinter.Label(window, text="브랜드").grid(row=0, column=0)
item_name = tkinter.Label(window, text="품명").grid(row=0, column=1)
item_category = tkinter.Label(window, text="종류").grid(row=0, column=2)
item_count = tkinter.Label(window, text="개수").grid(row=0, column=3)
wearing_price = tkinter.Label(window, text="입고가격").grid(row=0, column=4)
retail_price = tkinter.Label(window, text="소비자가격").grid(row=0, column=5)
item_loc = tkinter.Label(window, text="위치").grid(row=0, column=6)
item_code = tkinter.Label(window, text="품목코드").grid(row=0, column=7)
modify_index = tkinter.Label(window, text="수정할 품목 번호").grid(row=0, column=8)
del_index = tkinter.Label(window, text="삭제할 품목 번호").grid(row=0, column=9)


# 엔트리들
entry_brand = tkinter.Entry(window, width = 10)
entry_brand.grid(row=1, column=0)
entry_item_name = tkinter.Entry(window, width = 10)
entry_item_name.grid(row=1, column=1)
entry_item_category = tkinter.Entry(window, width = 10)
entry_item_category.grid(row=1, column=2)
entry_item_count = tkinter.Entry(window, width = 10)
entry_item_count.grid(row=1, column=3)
entry_wearing_price = tkinter.Entry(window, width = 10)
entry_wearing_price.grid(row=1, column=4)
entry_retail_price = tkinter.Entry(window, width = 10)
entry_retail_price.grid(row=1, column=5)
entry_item_loc = tkinter.Entry(window, width = 10)
entry_item_loc.grid(row=1, column=6)
entry_item_code = tkinter.Entry(window, width = 10)
entry_item_code.grid(row=1, column=7)
entry_modify_index = tkinter.Entry(window, width = 10)
entry_modify_index.grid(row=1, column=8)
entry_del_index = tkinter.Entry(window, width = 10)
entry_del_index.grid(row=1, column=9)


print()

















'''
# 참고 : http://tkinter-manual.blogspot.com/p/synopsis-instance-ttk.html
# https://stackoverflow.com/questions/30614279/python-tkinter-tree-get-selected-item-values/30615520
from tkinter import *
from tkinter import ttk

def selectItem(a):
    curItem = tree.focus()
    print(tree.item(curItem))

root = Tk()
tree = ttk.Treeview(root, columns=("size", "modified"))
tree["columns"] = ("date", "time", "loc")

tree.column("date", width=65)
tree.column("time", width=40)
tree.column("loc", width=100)

tree.heading("date", text="Date")
tree.heading("time", text="Time")
tree.heading("loc", text="Loc")
tree.bind('<Button-1>', selectItem)

tree.insert("","end",text = "Name",values = ("Date","Time","Loc"))

tree.grid()
root.mainloop()
'''
