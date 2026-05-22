import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from services.calorie_service import CalorieCalculator
from services.meal_logger import MealLogger


class FoodCalorieTracker:

    def __init__(self, root):

        self.root = root

        self.root.title("Food Calorie Tracker")
        self.root.geometry("700x500")
        self.root.config(bg="#7B2CBF")

        self.logger = MealLogger()

        # TITLE
        title = tk.Label(
            root,
            text="Food Calorie Tracker",
            font=("Arial", 18, "bold"),
            bg="#7B2CBF",
            fg="white"
        )

        title.pack(pady=10)

        # INPUT FRAME
        frame = tk.Frame(root, bg="#9D4EDD")
        frame.pack(pady=10)

        tk.Label(
            frame,
            text="Meal Type:",
            bg="#9D4EDD",
            fg="white"
        ).grid(row=0, column=0, padx=5, pady=5)

        self.meal_type = ttk.Combobox(
            frame,
            values=[
                "Breakfast",
                "Lunch",
                "Dinner",
                "Snack"
            ],
            width=20
        )

        self.meal_type.grid(row=0, column=1)
        self.meal_type.current(0)

        tk.Label(
            frame,
            text="Food Name:",
            bg="#9D4EDD",
            fg="white"
        ).grid(row=1, column=0, padx=5, pady=5)

        self.food_entry = tk.Entry(
            frame,
            width=25
        )

        self.food_entry.grid(row=1, column=1)

        # BUTTON FRAME
        btn_frame = tk.Frame(root, bg="#7B2CBF")
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame,
            text="ENTER",
            width=10,
            bg="#FFAFCC",
            command=self.add_meal
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            btn_frame,
            text="CLEAR",
            width=10,
            bg="#FFAFCC",
            command=self.clear_all
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            btn_frame,
            text="EXIT",
            width=10,
            bg="#FFAFCC",
            command=root.destroy
        ).grid(row=0, column=2, padx=5)

        # DAILY MEAL DISPLAY
        self.listbox = tk.Listbox(
            root,
            width=80,
            height=15
        )

        self.listbox.pack(pady=10)

        # TOTAL CALORIES
        self.total_label = tk.Label(
            root,
            text="Total Calories: 0",
            bg="#7B2CBF",
            fg="yellow",
            font=("Arial", 12, "bold")
        )

        self.total_label.pack()

        self.update_display()

    # FEATURE 1 + 2
    def add_meal(self):

        food = self.food_entry.get().strip()

        if not food:

            messagebox.showerror(
                "Error",
                "Please enter food name"
            )

            return

        calories = CalorieCalculator.calculate(food)

        self.logger.add_meal(
            self.meal_type.get(),
            food,
            calories
        )

        messagebox.showinfo(
            "Success",
            f"{food} added with {calories} calories."
        )

        self.food_entry.delete(0, tk.END)

        self.update_display()

    # FEATURE 3 + 4 + 5
    def update_display(self):

        self.listbox.delete(0, tk.END)

        total = 0

        for meal in self.logger.get_meals():

            self.listbox.insert(
                tk.END,
                f"{meal['date']} | "
                f"{meal['meal_type']} | "
                f"{meal['food']} | "
                f"{meal['calories']} Calories"
            )

            total += meal["calories"]

        self.total_label.config(
            text=f"Total Calories: {total}"
        )

    def clear_all(self):

        confirm = messagebox.askyesno(
            "Confirm",
            "Delete all meals?"
        )

        if confirm:

            self.logger.clear_all()

            self.update_display()