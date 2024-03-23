import tkinter as tk
from tkinter import messagebox

class BMI_Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")

        self.label_weight = tk.Label(self.root, text="Enter Weight (kg):")
        self.label_weight.grid(row=0, column=0, padx=10, pady=10)

        self.entry_weight = tk.Entry(self.root)
        self.entry_weight.grid(row=0, column=1, padx=10, pady=10)

        self.label_height = tk.Label(self.root, text="Enter Height (m):")
        self.label_height.grid(row=1, column=0, padx=10, pady=10)

        self.entry_height = tk.Entry(self.root)
        self.entry_height.grid(row=1, column=1, padx=10, pady=10)

        self.calculate_button = tk.Button(self.root, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, columnspan=2, padx=10, pady=10)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=3, columnspan=2, padx=10, pady=10)

    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())
            bmi = weight / (height ** 2)

            category = ""
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 25:
                category = "Normal"
            elif 25 <= bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"

            result = f"BMI: {bmi:.2f}\nCategory: {category}"
            self.result_label.config(text=result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid weight and height.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMI_Calculator(root)
    root.mainloop()
