from project import lista

import customtkinter
customtkinter.set_default_color_theme("dark-blue")
# window
root = customtkinter.CTk()
root.geometry("800x600")
frame1 = customtkinter.CTkFrame(root, width=300, height=450, corner_radius=10, fg_color="#bd9bad")
frame1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10) 

frame2 = customtkinter.CTkFrame(root, width=300, height=450, corner_radius=10, fg_color="#bd9bad")
frame2.grid(row=0, column=1, sticky="nsew", padx=10, pady=10) 

# Configure grid to ensure frames are the same size
root.grid_columnconfigure(0, weight=1) 
root.grid_columnconfigure(1, weight=1)  
root.grid_rowconfigure(0, weight=1)   

label1 = customtkinter.CTkLabel(frame1, text="Lista ciał niebieskich", text_color="#450945",font=("Arial", 20))
label1.pack(pady=10, padx=10)

label2 = customtkinter.CTkLabel(frame2, text="Actions", text_color="#450945",font=("Arial", 20))
label2.pack(pady=10, padx=10)


# buttons
add_button = customtkinter.CTkButton(
    master = frame2,
    text = "Dodaj objekt",     font=("Arial", 20),
    command = lambda: [lista.append("Marssssss ", 1.52, 6.42, 687),update_display()],
    fg_color="#f0c2db", 
    hover_color="#d690b5",
    text_color="#1f1219",
    width=200, 
    height=70,
    corner_radius=20
    )
add_button.pack(pady = 15, padx = 15)

delete_button = customtkinter.CTkButton(
    master = frame2,
    text = "Usun objekt",
    font=("Arial", 20),
    command = lambda: [lista.remove("Mars"),update_display()],
    fg_color="#f0c2db",  
    hover_color="#d690b5",
    text_color="#1f1219",
    width=200, 
    height=70,
    corner_radius=20
    )
delete_button.pack(pady = 15, padx = 15)

edit_button = customtkinter.CTkButton(
    master = frame2,
    text = "Edytuj objekt", 
    font=("Arial", 20),
    command=lambda: [
        lista.editByName("Mars", nazwa=None, odleglosc=None, masa=None, okresObiegu=None),
        update_display()
    ],
    fg_color="#f0c2db",  
    hover_color="#d690b5",
    text_color="#1f1219",
    width=200,  
    height=70,
    corner_radius=20
    )
edit_button.pack(pady = 15, padx = 15)

def sort_objects(choice):
    if choice == "Odleglosc od Slonca":
        print("Sort by distance from the sun")
    elif choice == "Okres obiegu dookoła Słońca rosnąca":
        print("Sort by Okres obiegu dookoła Słońca rosnąca")
    elif choice == "Masa":
        print("Sort by Okres obiegu dookoła Słońca rosnąca")
    elif choice == "Okres obiegu dookoła Słońca malejąca":
        print("Sort by Okres obiegu dookoła Słońca malejąca")


sort_options = ["Odległości od Słońca","Masy", "Okresu obiegu dookoła Słońca (rosnąco)", "Okresu obiegu dookoła Słońca (malejąco)"]
sort_combobox = customtkinter.CTkComboBox(
    master=frame2, 
    font=("Arial", 20),

    values=sort_options, 
    
    command=sort_objects, 
    button_color="#f0c2db",
    text_color="#1f1219",
    border_color="#f0c2db",
    fg_color="#f0c2db",
    state="readonly",
    
    width=200,  # Set the width to 200 pixels
    height=70,
    corner_radius=20
    )
sort_combobox.set("Sortuj według: ")
sort_combobox.pack(pady = 15, padx = 15)


# frame 1
display_textbox = customtkinter.CTkTextbox(
    frame1,
    width=300,
    height=450,
    fg_color="#f0c2db",
    text_color="#450945",
    font=("Arial", 16),
    corner_radius=20
)
display_textbox.pack(pady=15, padx=15)

def update_display():
    if display_textbox.get("1.0", "end").strip():  #if not empty, proceed to delete
        display_textbox.delete("1.0", "end") #clear the textbox
    counter = lista.head
    while counter is not None:
        display_textbox.insert("end", f"Nazwa: {counter.nazwa}\n")
        display_textbox.insert("end", f"Odległość: {counter.odleglosc} AU\n")
        display_textbox.insert("end", f"Masa: {counter.masa} x10^24 kg\n")
        display_textbox.insert("end", f"Okres obiegu: {counter.okresObiegu} dni\n")
        display_textbox.insert("end", "-"*30 + "\n")  # Separator
        counter = counter.next



#displaying objects
counter = lista.head
while counter is not None:
    display_textbox.insert("end", f"Nazwa: {counter.nazwa}\n")
    display_textbox.insert("end", f"Odległość: {counter.odleglosc} AU\n")
    display_textbox.insert("end", f"Masa: {counter.masa} x10^24 kg\n")
    display_textbox.insert("end", f"Okres obiegu: {counter.okresObiegu} dni\n")
    display_textbox.insert("end", "-"*30 + "\n")  # Separator
    counter = counter.next  
root.mainloop()