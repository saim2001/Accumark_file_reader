try:
    import tkinter
    import requests
    import customtkinter
    from tkinter import messagebox
    from excel_data_extractor_test import main
    customtkinter.set_appearance_mode("light")

    customtkinter.set_default_color_theme('blue')

    def start_reader():
        folder = entry.get()
        # exe = entry_1.get()
        if folder == 'Folder' or folder == '':
            messagebox.showerror('Error','Please select a file to execute')
        else:
            main(r'{}'.format(folder))
        

    def browse_folder(entry):
        folder_path = tkinter.filedialog.askdirectory()
        entry.delete(0, 'end')
        entry.insert(0, folder_path)
        # entry.config(foreground='black') 
    # def browse_file_1(entry_1):
    #     file_path = tkinter.filedialog.askopenfilename()
    #     entry_1.delete(0, 'end')
    #     entry_1.insert(0, file_path)
        # entry.config(foreground='black') 

    root = customtkinter.CTk()
    root.title('Accumark automation')

    label = customtkinter.CTkLabel(master=root,
                                text="Accumark File Reader",
                                font=('Helvetica',20))
    label.place(relx=0.5, rely=0.1, anchor=tkinter.N)

    entry = customtkinter.CTkEntry(master=root,
                                width=300,
                                height=25,
                                placeholder_text="Folder")
    entry.place(relx=0.38, rely=0.2, anchor=tkinter.N)

    # entry_1 = customtkinter.CTkEntry(master=root,
    #                             width=300,
    #                             height=25,
    #                             placeholder_text="Executable file")
    # entry_1.place(relx=0.38, rely=0.25, anchor=tkinter.N)

    # exe = entry_1.get()
    file_folder_path = entry.get()

    browse_button = customtkinter.CTkButton(master=root,
                                    text="Browse",
                                    command= lambda: browse_folder(entry),
                                    width=120,
                                    height=25,
                                    border_width=0,
                                    corner_radius=8)
    browse_button.place(relx=0.82, rely=0.2, anchor=tkinter.N)

    # browse_button = customtkinter.CTkButton(master=root,
    #                                 text="Browse",
    #                                 command= lambda: browse_file_1(entry_1),
    #                                 width=120,
    #                                 height=25,
    #                                 border_width=0,
    #                                 corner_radius=8)
    # browse_button.place(relx=0.82, rely=0.25, anchor=tkinter.N)

    execute_button = customtkinter.CTkButton(master=root,
                                    text="Execute",
                                    command=start_reader,
                                    width=430,
                                    height=25,
                                    border_width=0,
                                    corner_radius=8)
    execute_button.place(relx=0.51, rely=0.33, anchor=tkinter.N)


    root.geometry("500x600")

    try:
        cond_AT = requests.get("https://saim2481.pythonanywhere.com/ATactivation-desktop-response/")
        cond_AT.raise_for_status()
        cond_AT = cond_AT.text
    except requests.exceptions.RequestException as e:
        cond_AT = False
        messagebox.showerror("Connection Error","Please Check your internet Connection")
    except:
        cond_AT = False
        messagebox.showerror("Something Went Wrong","Unexpected Error")
    print(cond_AT)
    print(type(cond_AT))
    print(cond_AT == "true")
    if cond_AT != "true":
        execute_button.configure(state=customtkinter.DISABLED) 


    root.mainloop()
except Exception as e:
    print(e)
    while True:
        pass