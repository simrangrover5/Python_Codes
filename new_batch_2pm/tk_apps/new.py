import tkinter as tk


r = tk.Tk()

f1 = tk.Frame(r)
f2 = tk.Frame(r)

l1 = tk.Label(f1,text="Hi THis is Frame One\nHow Are you frame2")
l2 = tk.Label(f2,text='Hi This is Frame two \n I am good frame1')

l1.pack()
l2.pack()

f1.grid(row=0,column=0,rowspan=5,columnspan=5,padx=50,pady=50,ipadx=50,ipady=50)
f2.grid(row=5,column=5,rowspan=5,columnspan=5,padx=50,pady=50,ipadx=50,ipady=50)

r.mainloop()
