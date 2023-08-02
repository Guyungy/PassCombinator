import tkinter as tk
from tkinter import simpledialog, messagebox
import itertools


class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("密码组合生成工具")

        # 初始化界面元素
        self.init_ui()

    def init_ui(self):
        # 提示标签
        tk.Label(self.root, text="请输入密码由几个部分组成:").grid(row=0, column=0, padx=10, pady=5)

        # 密码部分数量输入框
        self.num_parts_entry = tk.Entry(self.root)
        self.num_parts_entry.grid(row=0, column=1, padx=10, pady=5)

        # 确定按钮
        tk.Button(self.root, text="确定", command=self.set_num_parts).grid(row=1, columnspan=2, pady=20)

    def set_num_parts(self):
        try:
            num_parts = int(self.num_parts_entry.get())
            if num_parts <= 0:
                raise ValueError
            self.password_parts_input(num_parts)
        except ValueError:
            messagebox.showerror("错误", "请输入一个有效的正整数。")

    def password_parts_input(self, num_parts):
        self.num_parts = num_parts

        # 清空界面
        for widget in self.root.winfo_children():
            widget.destroy()

        self.entries_matrix = []
        for i in range(num_parts):
            tk.Label(self.root, text=f"密码部分 {i + 1}:").grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(self.root)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries_matrix.append([entry])
            add_btn = tk.Button(self.root, text="增加选项", command=lambda i=i: self.add_option(i))
            add_btn.grid(row=i, column=2, padx=10, pady=5)

        tk.Button(self.root, text="生成密码", command=self.generate_password_combinations).grid(row=num_parts, columnspan=3, pady=20)

    def add_option(self, part_index):
        new_entry = tk.Entry(self.root)
        new_entry.grid(row=part_index, column=3+len(self.entries_matrix[part_index]), padx=10, pady=5)
        self.entries_matrix[part_index].append(new_entry)
        self.root.geometry("")  # 更新窗口大小

    def generate_password_combinations(self):
        password_parts = []
        for entry_list in self.entries_matrix:
            part_options = [entry.get() for entry in entry_list if entry.get()]
            password_parts.append(part_options)

        combinations = list(itertools.product(*password_parts))
        file_name = "password.txt"

        with open(file_name, "w") as f:
            for combo in combinations:
                f.write("".join(combo) + "\n")

        messagebox.showinfo("完成", f"所有可能的密码组合已保存到{file_name}文件中。")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    app.run()
