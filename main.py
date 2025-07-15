import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import openpyxl
import xlrd
from pathlib import Path
from openpyxl import workbook

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.layout_config()
        self.appearence()
        self.all_system()

    def layout_config(self):
        self.title("Sistema de Cadastro de Clientes")
        self.geometry("800x500")
        self.resizable(False, False)  # disable resizing
        self.maxsize(800, 500)
        self.minsize(800, 500)

    def appearence(self):
        # Appearence mode ui
        self.appearence_mode_label = ctk.CTkLabel(
            self, text='tema', bg_color='transparent', text_color=['#000', '#fff']).place(x=50, y=430)
        self.appearence_mode_opitions = ctk.CTkOptionMenu(
            self, values=['Light', 'Dark', 'System'], command=self.change_appearence).place(x=50, y=460)

    def change_appearence(self, new_appearence_mode):
        ctk.set_appearance_mode(new_appearence_mode)

    def all_system(self):
        # header frame title
        frame = ctk.CTkFrame(self, width=800, height=50,
                             corner_radius=0, bg_color="green", fg_color="green")
        frame.place(x=0, y=10)
        title = ctk.CTkLabel(frame, text='Sistema Cadastro de Clientes', font=(
            "Segoe UI", 25), text_color="#fff")
        title.place(relx=0.5, rely=0.5, anchor='center')

        smal_box = ctk.CTkLabel(self, text='Prencha todos os campos:', font=(
            "Segoe UI", 16), text_color=["#000", "#fff"]).place(x=50, y=70)

        # x,y patterns
        x_label = 50
        x_entry = 220
        y_start = 120
        y_step = 50
        # name
        input_name = ctk.CTkLabel(self, text='Nome Completo:', font=(
            "Segoe UI", 16), text_color=["#000", "#fff"])
        input_name.place(x=x_label, y=y_start)
        name_entry = ctk.CTkEntry(self, width=500, font=(
            "Segoe UI", 16), fg_color='transparent')
        name_entry.place(x=x_entry, y=y_start-5)
        # contact
        input_contact = ctk.CTkLabel(self, text='Número de contato:', font=(
            "Segoe UI", 16), text_color=["#000", "#fff"])
        input_contact.place(x=x_label, y=y_start + y_step)
        contact_entry = ctk.CTkEntry(self, width=200, font=(
            "Segoe UI", 16), fg_color='transparent')
        contact_entry.place(x=x_entry, y=y_start + y_step - 5)
        # age
        input_age = ctk.CTkLabel(self, text='Idade:', font=(
            "Segoe UI", 16), text_color=["#000", "#fff"])
        input_age.place(x=440, y=y_start + y_step)
        age_entry = ctk.CTkEntry(self, width=80, font=(
            "Segoe UI", 16), fg_color='transparent')
        age_entry.place(x=500, y=y_start + y_step - 5)
        # gender
        input_gender = ctk.CTkLabel(self, text='Gênero:', font=(
            "Segoe UI", 16), text_color=["#000", "#fff"])
        input_gender.place(x=600, y=y_start + y_step)
        gender_combobox = ctk.CTkComboBox(
            self, values=['Masculino', 'Feminino'], font=('Segoe UI', 15), width=120)
        gender_combobox.set('Masculino')
        gender_combobox.place(x=670, y=y_start + y_step - 5)
        # addres
        input_address = ctk.CTkLabel(self, text='Endereço:', font=(
            "Segoe UI", 16), text_color=["#000", "#fff"])
        input_address.place(x=x_label, y=y_start + 2 * y_step)
        address_entry = ctk.CTkEntry(self, width=500, font=(
            "Segoe UI", 16), fg_color='transparent')
        address_entry.place(x=x_entry, y=y_start + 2 * y_step - 5)
        # OBS
        input_obs = ctk.CTkLabel(self, text='Observaçoes:', font=(
            "Segoe UI", 16), text_color=["#000", "#fff"])
        input_obs.place(x=x_label, y=y_start + 3 * y_step + 4)
        obs_entry = ctk.CTkTextbox(self, width=670, height=150, font=(
            'Arial', 18), bg_color='#aaa', border_width=2, fg_color='transparent')
        obs_entry.place(x=x_label, y=y_start + 3 * y_step + 30)


if __name__ == '__main__':
    app = App()
    app.mainloop()
