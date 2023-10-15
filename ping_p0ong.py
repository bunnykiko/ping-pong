import tkinter as tk
from two import PingPong  # Импорт класса PingPong из модуля 'two'
from solo import PingPongSolo  # Импорт класса PingPongSolo из модуля 'solo'

class GameMenu:
    def __init__(self, master):
        self.master = master
        master.title("Меню игры")  # Устанавливаем заголовок главного окна "Меню игры"
        master.geometry("1100x658")  # Устанавливаем размеры главного окна 1100x658 пикселей
        master.config(bg="#1a1a1a")  # Устанавливаем фоновый цвет главного окна в темно-серый цвет

        self.menu_visible = True  # Флаг для отслеживания состояния меню
        self.instructions_visible = False  # Флаг для отслеживания состояния инструкций

        self.title_label = tk.Label(master, text="Меню игры", font=("Helvetica", 36), fg="#fff", bg="#1a1a1a")
        self.title_label.pack(pady=50)  # Создаем и размещаем метку с заголовком в главном окне с некоторыми параметрами настройки

        self.start_button = tk.Button(master, text="Начать игру", font=("Helvetica", 24), fg="#1a1a1a", bg="#fff", command=self.show_game_options)
        self.start_button.pack(pady=50)  # Создаем и размещаем кнопку "Начать игру" в главном окне с некоторыми параметрами настройки

        self.instructions_button = tk.Button(master, text="Как играть?", font=("Helvetica", 24), fg="#1a1a1a", bg="#fff", command=self.toggle_instructions)
        self.instructions_button.pack(pady=50)  # Создаем и размещаем кнопку "Как играть?" в главном окне с некоторыми параметрами настройки

        self.quit_button = tk.Button(master, text="Покинуть игру", font=("Helvetica", 24), fg="#1a1a1a", bg="#fff", command=root.destroy)
        self.quit_button.pack(pady=50)  # Создаем и размещаем кнопку "Покинуть игру" в главном окне с некоторыми параметрами настройки

        self.game_window_open = False  # Флаг для отслеживания состояния окна игры

        self.instructions_label = tk.Label(master, text="", font=("Helvetica", 14), fg="#fff", bg="#1a1a1a")
        self.return_button = tk.Button(master, text="Вернуться в главное меню", font=("Helvetica", 14), fg="#1a1a1a", bg="#fff", command=self.return_to_menu)
        self.return_button.pack_forget()

        self.singleplayer_button = tk.Button(master, text="Игра в одиночку", font=("Helvetica", 24), fg="#1a1a1a", bg="#fff", command=self.start_singleplayer_game)
        self.singleplayer_button.pack_forget()

        self.multiplayer_button = tk.Button(master, text="Игра вдвоем", font=("Helvetica", 24), fg="#1a1a1a", bg="#fff", command=self.start_multiplayer_game)
        self.multiplayer_button.pack_forget()

    def show_game_options(self):
        self.start_button.pack_forget()
        self.instructions_button.pack_forget()
        self.quit_button.pack_forget()

        self.singleplayer_button.pack(pady=10)
        self.multiplayer_button.pack(pady=10)
        self.return_button.pack(pady=150)

    def toggle_instructions(self):
        if self.menu_visible:
            self.menu_visible = False
            self.instructions_visible = True
            self.title_label.pack_forget()
            self.start_button.pack_forget()
            self.instructions_button.pack_forget()
            self.quit_button.pack_forget()
            self.instructions_label.config(text="Одиночная игра:\nW - сместить ракетку вверх\nS - сместить ракетку вниз\n\n"
                                                "Игра вдвоем:\nИгрок первый:\nW - сместить ракетку вверх\nS - сместить ракетку вниз\n\n"
                                                "Игрок второй:\nСтрелка вверх - сместить ракетку вверх\nСтрелка вниз - сместить ракетку вниз\nP - поставить игру на паузу")
            self.instructions_label.pack(pady=20)
            self.return_button.pack(pady=100)
        else:
            self.menu_visible = True
            self.instructions_visible = False
            self.title_label.pack()
            self.start_button.pack()
            self.instructions_button.pack()
            self.quit_button.pack()
            self.instructions_label.pack_forget()
            self.return_button.pack_forget()
            self.return_to_menu()  # Вызываем функцию return_to_menu при скрытии инструкций

    def start_singleplayer_game(self):
        if not self.game_window_open:  # Проверяем, что окно игры не открыто
            self.master.withdraw()  # Скрываем окно меню
            game_window = tk.Toplevel()  # Создаем новое окно для игры в одиночку
            game_window.protocol("WM_DELETE_WINDOW", self.return_to_menu)  # Обрабатываем событие закрытия окна игры
            game = PingPongSolo(game_window)
            game.start()
            self.game_window_open = True  # Устанавливаем флаг, что окно игры открыто
            self.master.deiconify()  # Восстанавливаем окно меню при закрытии окна игры

    def start_multiplayer_game(self):
        if not self.game_window_open:  # Проверяем, что окно игры не открыто
            self.master.withdraw()  # Скрываем окно меню
            game_window = tk.Toplevel()  # Создаем новое окно для многопользовательской игры
            game_window.protocol("WM_DELETE_WINDOW", self.return_to_menu)  # Обрабатываем событие закрытия окна игры
            game = PingPong(game_window)
            game.start()
            self.game_window_open = True  # Устанавливаем флаг, что окно игры открыто
            self.master.deiconify()  # Восстанавливаем окно меню при закрытии окна игры

    def return_to_menu(self):
        self.game_window_open = False  # Сбрасываем флаг окна игры

        # Центрирование элементов интерфейса
        self.title_label.pack(pady=50)
        self.start_button.pack(pady=10)
        self.instructions_button.pack(pady=10)
        self.quit_button.pack(pady=10)
        self.singleplayer_button.pack_forget()
        self.multiplayer_button.pack_forget()
        self.instructions_label.pack_forget()
        self.return_button.pack_forget()

root = tk.Tk()
menu = GameMenu(root)
root.mainloop()
