import tkinter as tk
def click(x):
    entry.insert(tk.END,x)
def clear():
    entry.delete(0,tk.END)
def calc():
    try:
        result=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"error")
    
root=tk.Tk()
root.title("Calculator")
root.configure(bg="gray")
root.resizable(True,True)
entry =tk.Entry(root,
                font=("Segoe UI",20),
                bg="black",fg="white",
                bd=0,justify="right")
entry.grid(row=0,column=0,columnspan=4,padx=12,pady=12,ipady=10)
buttons=["7","8","9","/","4","5","6","*","1","2","3","-","0",".","=","+"]
r=1
c=0
for b in buttons:
    cmd=calc if b=="=" else lambda x=b:click(x)
    tk.Button(root,text=b,command=cmd,font=("Segoe UI",8),padx=2,pady=2,bg="#ff9500" if b in "+-/*=" else "gray",fg="white",bd=0,height=2,width=4).grid(row=r,column=c,ipady=7)
    c=c+1
    if c==4:
        c=0
        r=r+1
tk.Button(root,text="c",font=("Segoe UI",10),command=clear,bg="red",fg="white",bd=2,height=3,width=4).grid(row=r,column=c,columnspan=2)
root.mainloop()
