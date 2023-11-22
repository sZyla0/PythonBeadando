import tkinter
from kiegeszito_modul import login

class szamologep:
    def __init__(self, master):
        self.master = master
        master.title("számológép")

        self.szam1 = tkinter.Entry(master)
        self.szam1.grid(row=0, column=0)

        self.szam2 = tkinter.Entry(master)
        self.szam2.grid(row=0, column=2)

        self.muveleti_jel = tkinter.Entry(master)
        self.muveleti_jel.grid(row=0, column=1)

        self.eredmeny = tkinter.Label(master, text="Eredmény:")
        self.eredmeny.grid(row=1, column=0, columnspan=3)

        self.urites = tkinter.Button(master, text="Törlés", command=self.clear_entries)
        self.urites.grid(row=2, column=0)

        self.megoldas = tkinter.Button(master, text="Számol", command=self.calculate)
        self.megoldas.grid(row=2, column=1)

    def clear_entries(self):
        self.szam1.delete(0, tkinter.END)
        self.szam2.delete(0, tkinter.END)
        self.muveleti_jel.delete(0, tkinter.END)
        self.eredmeny.config(text="Eredmény:")

    def calculate(self):
        try:
            num1 = float(self.szam1.get())
            num2 = float(self.szam2.get())
            operator = self.muveleti_jel.get()
            
            if operator == '+':
                muv_eredmeny = num1 + num2
            elif operator == '-':
                muv_eredmeny = num1 - num2
            elif operator == '*':
                muv_eredmeny = num1 * num2
            elif operator == '/':
                muv_eredmeny = num1 / num2
            else:
                raise ValueError("Nem megfelelő műveleti jel!")

            self.eredmeny.config(text=f"Eredmény: {muv_eredmeny}")
        except Exception as e:
            self.eredmeny.config(text="Hiba: " + str(e))

if __name__ == "__main__":
    root = tkinter.Tk()
    
    # Bejelentkezés ellenőrzése
    if login():
        calculator = szamologep(root)
        print("Sikeres belépés!")
        root.mainloop()
    else:
        print("Sikertelen belépés!")
print("Viszlát!")