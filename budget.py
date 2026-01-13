import json
import os
from datetime import datetime

DATA_FILE = "data.json"

# 初始化数据文件
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

# 读取数据
def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# 保存数据
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# 添加账目
def add_record():
    date_str = input("请输入日期 (YYYY-MM-DD) [默认今天]: ")
    if not date_str:
        date_str = datetime.today().strftime("%Y-%m-%d")
    category = input("请输入类别 (如: food, salary): ")
    record_type = input("类型 (income/expense): ").lower()
    if record_type not in ["income", "expense"]:
        print("类型错误，请输入 income 或 expense")
        return
    try:
        amount = float(input("请输入金额: "))
    except ValueError:
        print("金额必须是数字")
        return
    note = input("备注 (可选): ")

    data = load_data()
    data.append({
        "date": date_str,
        "category": category,
        "type": record_type,
        "amount": amount,
        "note": note
    })
    save_data(data)
    print("账目添加成功！\n")

# 查看账目
def view_records():
    data = load_data()
    if not data:
        print("暂无账目记录。\n")
        return
    print("序号 | 日期 | 类别 | 类型 | 金额 | 备注")
    print("-"*50)
    for i, rec in enumerate(data, 1):
        print(f"{i} | {rec['date']} | {rec['category']} | {rec['type']} | {rec['amount']} | {rec['note']}")
    print()

# 统计
def stats():
    data = load_data()
    if not data:
        print("暂无账目记录。\n")
        return
    income = sum(rec["amount"] for rec in data if rec["type"] == "income")
    expense = sum(rec["amount"] for rec in data if rec["type"] == "expense")
    balance = income - expense
    print(f"总收入: {income}")
    print(f"总支出: {expense}")
    print(f"余额: {balance}\n")

# 主菜单
def main():
    while True:
        print("=== 命令行记账工具 ===")
        print("1. 添加账目")
        print("2. 查看账目")
        print("3. 统计")
        print("4. 退出")
        choice = input("请选择操作 (1-4): ")
        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            stats()
        elif choice == "4":
            print("退出程序")
            break
        else:
            print("无效选择，请重新输入\n")

if __name__ == "__main__":
    main()

