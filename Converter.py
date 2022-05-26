


from tkinter import *
from tkinter import ttk

root=Tk()

root.title("Converter")
root.geometry("400x200+500+400")

currency=StringVar()



rbEur=Radiobutton(root,text="Euro", value="EUR", variable=currency) # you need to link it
rbEur.grid(row=1, column=0)

rbLek=Radiobutton(root,text="Leke", value="LEKE", variable=currency)
rbLek.grid(row=2, column=0)

amount=Label(root, text="Insert the amount of money in $: ")
amount.grid(row=0, column=0)
insert_money=Entry(root)
insert_money.grid(row=0, column=1)

label_output=Label(root, text="The amount is: ")
label_output.grid(row=2, column=1)

# creating a label that outputs the result
value=StringVar()
final=Label(root, textvariable=value)
final.grid(row=2, column=2)

def convert():
    val1=float(insert_money.get())
    if currency.get()==rbEur:
        result1=round(float(val1*0.87))
        value.set(f"{result1:,}")
    else:
        result2=round(float(val1*105.20))
        value.set(f"{result2:,}")
        
        
    
convert_button=Button(root, text="Convert", command=convert)
convert_button.grid(row=4, columnspan=2)



root.mainloop()

