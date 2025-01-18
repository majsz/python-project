from project import lista
from project import CialoNiebieskie

import customtkinter
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("1000x750")

frame1 = customtkinter.CTkFrame(root, width=450, height=600, corner_radius=10, fg_color="#bd9bad")
frame1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10) 

frame2 = customtkinter.CTkFrame(root, width=450, height=600, corner_radius=10, fg_color="#bd9bad")
frame2.grid(row=0, column=1, sticky="nsew", padx=10, pady=10) 

# Configure grid to ensure frames are the same size
root.grid_columnconfigure(0, weight=1) 
root.grid_columnconfigure(1, weight=1)  
root.grid_rowconfigure(0, weight=1)

label1 = customtkinter.CTkLabel(frame1, text="Lista ciał niebieskich", text_color="#450945", font=("Arial", 20))
label1.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

label2 = customtkinter.CTkLabel(frame2, text="Actions", text_color="#450945", font=("Arial", 20))
label2.grid(row=0, column=0, columnspan=2, pady=10, padx=10)


# input to add
#name
text_label = customtkinter.CTkLabel(frame2, text="Wprowadz dane nowego obiektu:", text_color="#450945", font=("Arial", 16))
text_label.grid(row=1, column=0, columnspan=2, pady=10, padx=10,sticky = "n")

data_entry_name = customtkinter.CTkEntry(
    master=frame2,
    font=("Arial", 14),
    placeholder_text="Wpisz imie by dodac obiekt",
    fg_color="#d9b6c9", 
    text_color="#1f1219",
    width=300,
    height=35,
    corner_radius=20
)
data_entry_name.grid(row=2, column=0, padx=8, pady=8, sticky="w")

#odleglosc
data_entry_distance = customtkinter.CTkEntry(
    master=frame2,
    font=("Arial", 14),
    placeholder_text="Wpisz odleglosc by dodac obiekt",
    fg_color="#d9b6c9", 
    text_color="#1f1219",
    width=300,
    height=35,
    corner_radius=20
)
# in 2 column
data_entry_distance.grid(row=2, column=1, padx=8, pady=8, sticky="w")
#masa
data_entry_masa = customtkinter.CTkEntry(
    master=frame2,
    font=("Arial", 14),
    placeholder_text="Wpisz mase by dodac obiekt",
    fg_color="#d9b6c9", 
    text_color="#1f1219",
    width=300,
    height=35,
    corner_radius=20
)
data_entry_masa.grid(row=3, column=0, padx=8, pady=8, sticky="w")
#okres obiegu
data_entry_okres = customtkinter.CTkEntry(
    master=frame2,
    font=("Arial", 14),
    placeholder_text="Wpisz okres obiegu by dodac obiekt",
    fg_color="#d9b6c9", 
    text_color="#1f1219",
    width=300,
    height=35,
    corner_radius=20
)
data_entry_okres.grid(row=3, column=1, padx=8, pady=8, sticky="w")

def add_object():
    try:
        name = data_entry_name.get().strip()
        distance = float(data_entry_distance.get().strip())
        mass = float(data_entry_masa.get().strip())
        period = int(data_entry_okres.get().strip())
        if name == "" or distance == "" or mass == "" or period == "":
            error_label.configure(text="Wprowadz wszystkie dane")
            return
        if distance <= 0 or mass <= 0 or period < 0:
            error_label.configure(text="Wprowadz dodatnie wartosci")
            return
        lista.add(name, distance, mass, period)
        update_display()
    except ValueError:
        error_label.configure(text="Wprowadz dane w odpowiednim formacie")
    except IndexError:
        error_label.configure(text="Wprowadz dane w odpowiednim formacie")

add_button = customtkinter.CTkButton(
    master=frame2,
    text="Dodaj objekt",     
    font=("Arial", 20),
    command=lambda: [add_object(), update_display()],
    fg_color="#f0c2db", 
    hover_color="#d690b5",
    text_color="#1f1219",
    width=200, 
    height=50,
    corner_radius=20
)
add_button.grid(row=4, column=0, columnspan=2, pady=15, padx=15)

data_entry_to_remove_by_name = customtkinter.CTkEntry(
    master=frame2,
    font=("Arial", 14),
    placeholder_text="Wpisz nazwe do usunięcia",
    fg_color="#d9b6c9", 
    text_color="#1f1219",
    width=300,
    height=35,
    corner_radius=20
)
data_entry_to_remove_by_name.grid(row=5, column=0, columnspan=2, padx=8, pady=8)


delete_button = customtkinter.CTkButton(
    master=frame2,
    text="Usun objekt",
    font=("Arial", 20),
    command=lambda: [
        lista.remove_by_name(data_entry_to_remove_by_name.get().strip()),
        update_display()
    ],
    fg_color="#f0c2db",  
    hover_color="#d690b5",
    text_color="#1f1219",
    width=200, 
    height=50,
    corner_radius=20
)
delete_button.grid(row=6, column=0, columnspan=2, pady=15, padx=15)

# NAME input for edit
data_entry_to_edit_by_name = customtkinter.CTkEntry(
    master=frame2,
    font=("Arial", 14),
    placeholder_text="Wpisz nazwe ob do edytowania",
    fg_color="#d9b6c9", 
    text_color="#1f1219",
    width=300,
    height=35,
    corner_radius=20
)
data_entry_to_edit_by_name.grid(row=8, column=0, columnspan=2, padx=8, pady=8)

edit_button_by_name = customtkinter.CTkButton(
    master=frame2,
    text="Edytuj objekt po nazwie", 
    font=("Arial", 20),
    command=lambda: [
        # edit NIE DZIALA
        lista.edit_by_name(data_entry_to_edit_by_name, data_entry_name,data_entry_masa,data_entry_distance,data_entry_okres),
        update_display()
    ],
    fg_color="#f0c2db",  
    hover_color="#d690b5",
    text_color="#1f1219",
    width=200,  
    height=50,
    corner_radius=20
)
edit_button_by_name.grid(row = 9, column = 0,columnspan = 2,pady=15, padx=15)

#SORT dropdown
def sort_objects(choice):
    if choice == "Odległości od Słońca":
        print("Sort by distance from the sun")
    elif choice == "Okresu obiegu dookoła Słońca (rosnąco)":
        print("Sort by period (ascending)")
    elif choice == "Masy":
        print("Sort by mass")
    elif choice == "Okresu obiegu dookoła Słońca (malejąco)":
        print("Sort by period (descending)")

sort_options = ["Odległości od Słońca", "Masy", "Okresu obiegu dookoła Słońca (rosnąco)", "Okresu obiegu dookoła Słońca (malejąco)"]
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
    width=200,
    height=50,
    corner_radius=20
)
sort_combobox.set("Sortuj według: ")
sort_combobox.grid(row=10, column=0, columnspan=2, pady=15, padx=15)

# displaying objects in frame 1
display_textbox = customtkinter.CTkTextbox(
    frame1,
    width=280,
    height=600,
    fg_color="#f0c2db",
    text_color="#450945",
    font=("Arial", 16),
    corner_radius=20
)
display_textbox.grid(row=1, column=0, columnspan=2, pady=15, padx=15)
error_label = customtkinter.CTkLabel(frame1, text="", text_color="#fc0324", font=("Arial", 12))
error_label.grid(row = 2, column = 0, columnspan = 2,pady=10, padx=10)

def update_display():
    display_textbox.delete("1.0", "end")  # Clear the textbox
    for obj in lista.objects:
        display_textbox.insert("end", f"Nazwa: {obj.nazwa}\n")
        display_textbox.insert("end", f"Odległość: {obj.odleglosc} AU\n")
        display_textbox.insert("end", f"Masa: {obj.masa} x10^24 kg\n")
        display_textbox.insert("end", f"Okres obiegu: {obj.okresObiegu} dni\n")
        display_textbox.insert("end", "-"*30 + "\n")  # Separator

update_display()

# running 
root.mainloop()
