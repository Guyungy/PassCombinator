def main():
    """
    主函数
    """
    print("密码组合生成工具")
    # 初始化阶段
    part_count = init_phase()

    # 密码部分输入
    password_parts = password_input(part_count)

    # 密码生成
    generate_passwords(password_parts)


def init_phase():
    """
    初始化阶段，询问密码由几个部分组成
    """
    while True:
        try:
            parts = int(input("请输入密码由几个部分组成："))
            if parts > 0:
                return parts
            else:
                print("请输入一个正整数！")
        except ValueError:
            print("输入无效，请输入一个整数！")


def password_input(part_count):
    """
    根据用户输入的部分数，循环询问每部分的可能密码
    """
    password_parts = []
    for i in range(part_count):
        options = []
        while True:
            print(f"\n输入密码部分 {i + 1} 的可能密码：")
            print("A. 继续为当前部分输入其他可能的密码")
            print("B. 为当前部分增加一个空的选项")
            print("C. 移动到下一个密码部分或，如果所有部分都已输入，开始生成密码。")
            choice = input("请选择(A/B/C): ").strip().upper()
            if choice == 'A':
                option = input("请输入当前部分的可能密码：").strip()
                options.append(option)
            elif choice == 'B':
                options.append('')
            elif choice == 'C':
                if not options:
                    print("至少需要一个可能的密码!")
                    continue
                password_parts.append(options)
                break
            else:
                print("无效的选择，请重新选择!")
    return password_parts


def generate_passwords(password_parts):
    """
    使用每部分的所有可能的组合来生成密码列表，并输出到文件中
    """
    from itertools import product
    with open("password.txt", "w") as f:
        for password_combo in product(*password_parts):
            f.write(''.join(password_combo) + "\n")
    print("所有可能的密码组合已输出到 password.txt 文件中。")


if __name__ == '__main__':
    main()
