import tkinter
import tkinter.ttk
searched_window=tkinter.Tk()
searched_window.geometry("1000x500")

searched_treeview = tkinter.ttk.Treeview(searched_window, columns=["브랜드","품명","종류","개수","입고가격","소비자가격","위치","품목코드"],displaycolumns=["브랜드","품명","종류","개수","입고가격","소비자가격","위치","품목코드"])
searched_treeview.grid(row=0, column=0)

searched_treeview.column("#0", width=70)
searched_treeview.heading("#0")

searched_treeview.column("브랜드", width=100, anchor="center")
searched_treeview.heading("브랜드", text="브랜드", anchor="center")
searched_treeview.column("품명", width=100, anchor="center")
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
