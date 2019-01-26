import tkinter as tk
from simple_mail import send_mail

root = tk.Tk()

root.title('rMail')
root.geometry("400x500")

w_label = tk.Label(root, text="Welcome to talkMail...!", padx = 10)

fm_label = tk.Label(root, text="Your email :",  padx = 10)
fm_entry = Text(root, height=20, width=40)

tm_label = tk.Label(root, text="Recipient's email :",  padx = 10)
tm_entry = tk.Entry(root)

s_label = tk.Label(root, text="Subject :",  padx = 10)
s_entry = tk.Entry(root)

c_label = tk.Label(root, text="Message body :",  padx = 10)
c_entry = tk.Entry(root)

p_label = tk.Label(root, text="Password :",  padx = 10)
p_entry = tk.Entry(root)

w_label.grid(row=0, column=0)


fm_label.grid(row=1, column=0)
fm_entry.grid(row=1, column=1)

tm_label.grid(row=2, column=0)
tm_entry.grid(row=2, column=1)

s_label.grid(row=3, column=0)
s_entry.grid(row=3, column=1)

c_label.grid(row=4, column=0)
c_entry.grid(row=4, column=1)

p_label.grid(row=5, column=0)
p_entry.grid(row=5, column=1)


button = tk.Button(root, text="Send", command= lambda : send_mail(fm_entry.get(),tm_entry.get(),s_entry.get(),c_entry.get(),p_entry.get()))
button.grid(row=6, column=1)

root.mainloop()