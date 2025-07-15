import customtkinter as ctk
from tkinter import *
# from tkinter import messagebox
# import openpyxl
# import xlrd
# from pathlib import Path
# from openpyxl import workbook

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

    def appearence(self):
        self.appearence_mode_label = ctk.CTkLabel(
            self, text='tema', bg_color='transparent', text_color=['#000', '#fff']).place(x=50, y=430)
        self.appearence_mode_opitions = ctk.CTkOptionMenu(
            self, values=['Light', 'Dark', 'System'], command=self.change_appearence).place(x=50, y=460)

    def change_appearence(self, new_appearence_mode):
        ctk.set_appearance_mode(new_appearence_mode)

    def all_system(self):
        frame = ctk.CTkFrame(self, width=800, height=50,
                             corner_radius=0, bg_color="green", fg_color="green").place(x=0, y=10)
        title = ctk.CTkLabel(frame, text='Sistema Cadastro de Clientes', font=(
            "Ebrima Bold", 25), text_color="#fff")
        smal_box = ctk.CTkLabel(self, text='Por favor, preencha todos os dados do formulário!', font=(
            "Ebrima Bold", 16), text_color=["#000", "#fff"]).place(x=50, y=70)

        name_entry = ctk.CTkEntry(self, width=400, font=(
            "Ebrima Bold", 16), fg_color='transparent')
        contact_entry = ctk.CTkEntry(self, width=200, font=(
            "Ebrima Bold", 16), fg_color='transparent')
        age_entry = ctk.CTkEntry(self, width=200, font=(
            "Ebrima Bold", 16), fg_color='transparent')
        address_entry = ctk.CTkEntry(self, width=200, font=(
            "Ebrima Bold", 16), fg_color='transparent')

        gender_combobox = ctk.CTkComboBox(
            self, values=['Masculino', 'Feminino'], font=('Ebrima Bold', 15))
        gender_combobox.set('Masculino')

        obs_input = ctk.CTkTextbox(self, width=500, height=150, font=(
            'Arial', 18), bg_color='#aaa', border_width=2, fg_color='transparent')

        input_name = ctk.CTkLabel(self, text='Nome Completo:', font=(
            "Ebrima Bold", 16), text_color=["#000", "#fff"])
        input_contact = ctk.CTkLabel(self, text='Número de contato', font=(
            "Ebrima Bold", 16), text_color=["#000", "#fff"])
        input_age = ctk.CTkLabel(self, text='Idade:', font=(
            "Ebrima Bold", 16), text_color=["#000", "#fff"])
        input_gender = ctk.CTkLabel(self, text='Nascimento:', font=(
            "Ebrima Bold", 16), text_color=["#000", "#fff"])
        input_address = ctk.CTkLabel(self, text='Endereço:', font=(
            "Ebrima Bold", 16), text_color=["#000", "#fff"])
        input_options = ctk.CTkLabel(self, text='Observaçoes:', font=(
            "Ebrima Bold", 16), text_color=["#000", "#fff"])

        input_name.place(x=50, y=120)
        name_entry.place(x=50, y=150)


if __name__ == '__main__':
    app = App()
    app.mainloop()
