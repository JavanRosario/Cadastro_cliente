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

    def layout_config(self):
        self.title("Sistema de Cadastro de Clientes")
        self.geometry("800x500")


if __name__ == '__main__':
    app = App()
    app.mainloop()
