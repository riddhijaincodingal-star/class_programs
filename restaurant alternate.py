from tkinter import *

def calculate_bill():
    try:
        pizza = int(pizza_entry.get())
        burger = int(burger_entry.get())
        coffee = int(coffee_entry.get())

        total = (pizza * 200) + (burger * 100) + (coffee * 50)

        total_label.config(text="Total Bill: ₹" + str(total))
    except:
        total_label.config(text="Enter valid numbers")

root = Tk()
root.title("Restaurant Bill Generator")
root.geometry("350x300")

Label(root, text="Restaurant Bill Generator", font=("Arial", 16, "bold")).pack(pady=10)

Label(root, text="Pizza (₹200):").pack()
pizza_entry = Entry(root)
pizza_entry.pack()

Label(root, text="Burger (₹100):").pack()
burger_entry = Entry(root)
burger_entry.pack()

Label(root, text="Coffee (₹50):").pack()
coffee_entry = Entry(root)
coffee_entry.pack()

Button(root, text="Calculate Bill", command=calculate_bill).pack(pady=10)

total_label = Label(root, text="Total Bill: ₹0", font=("Arial", 12, "bold"))
total_label.pack()

root.mainloop()
