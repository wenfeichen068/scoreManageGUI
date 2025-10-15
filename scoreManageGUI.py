import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from tkinter import filedialog
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# 设置全局字体与负号支持
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False


# ------------------- 数据操作 -------------------
import os

DATA_FILE = 'grades.txt'


def load_data():
    students = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                data = line.strip().split(',')
                if len(data) == 5:
                    student = {
                        '学号': data[0],
                        '姓名': data[1],
                        '语文': int(data[2]),
                        '数学': int(data[3]),
                        '英语': int(data[4])
                    }
                    students.append(student)
    return students


def save_data(students):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        for student in students:
            line = f"{student['学号']},{student['姓名']},{student['语文']},{student['数学']},{student['英语']}\n"
            f.write(line)


students = load_data()

# ------------------- 主界面 -------------------
root = tk.Tk()
root.title("学生成绩管理系统")

# ------ 表格 ------
columns = ("学号", "姓名", "语文", "数学", "英语", "总分", "平均分")
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=70)
tree.pack(fill=tk.BOTH, expand=True)


def refresh_table():
   # tree.delete(*tree.get_children())

    for item in tree.get_children():
        tree.delete(item)

    for s in students:
        total = s['语文'] + s['数学'] + s['英语']
        avg = total / 3
        tree.insert('', tk.END, values=(
            s['学号'], s['姓名'], s['语文'], s['数学'], s['英语'], total, f"{avg:.1f}"
        ))


# ------ 功能实现 ------
#导入数据函数
def import_data():
    filepath = filedialog.askopenfilename(filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")])
    if not filepath:
        return
    imported = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split(",")
                if len(data) == 5:
                    student = {
                        '学号': data[0],
                        '姓名': data[1],
                        '语文': int(data[2]),
                        '数学': int(data[3]),
                        '英语': int(data[4])
                    }
                    imported.append(student)
        # 合并且跳过学号重复
        existing_ids = set(s['学号'] for s in students)
        added_count = 0
        for s in imported:
            if s['学号'] not in existing_ids:
                students.append(s)
                added_count += 1

        # ======= 加入学号排序 =======
        students.sort(key=lambda x: int(x['学号']))
        # ===========================

        refresh_table()
        messagebox.showinfo("导入结果", f"导入完成，新增 {added_count} 条数据。")
    except Exception as e:
        messagebox.showerror("导入失败", f"发生错误: {e}")




#导出数据函数
def export_data():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("文本文件", "*.txt")])
    if not filepath:
        return
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            for s in students:
                line = f"{s['学号']},{s['姓名']},{s['语文']},{s['数学']},{s['英语']}\n"
                f.write(line)
        messagebox.showinfo("导出结果", "导出成功！")
    except Exception as e:
        messagebox.showerror("导出失败", f"发生错误: {e}")

def add_student():
    add_win = tk.Toplevel(root)
    add_win.title("添加学生成绩")
    add_win.grab_set()

    labels = ["学号", "姓名", "语文", "数学", "英语"]
    entries = []

    for i, label in enumerate(labels):
        tk.Label(add_win, text=label).grid(row=i, column=0, padx=5, pady=5)
        entry = tk.Entry(add_win)
        entry.grid(row=i, column=1, padx=5, pady=5)
        entries.append(entry)

    def do_add():
        info = [e.get().strip() for e in entries]
        if "" in info:
            messagebox.showwarning("输入错误", "请完整填写所有内容！")
            return
        # 学号不能重复
        if any(s['学号'] == info[0] for s in students):
            messagebox.showwarning("输入错误", "学号已存在，请重新输入。")
            return
        try:
            chinese = int(info[2])
            math = int(info[3])
            english = int(info[4])
        except:
            messagebox.showwarning("成绩错误", "成绩需输入整数！")
            return
        students.append({
            "学号": info[0], "姓名": info[1],
            "语文": chinese, "数学": math, "英语": english
        })
        students.sort(key=lambda x: int(x['学号']))
        refresh_table()
        messagebox.showinfo("成功", "学生添加成功")
        add_win.destroy()

    tk.Button(add_win, text="添加", command=do_add).grid(row=5, column=0, columnspan=2, pady=10)



def delete_student():
    sel = tree.selection()
    if not sel:
        messagebox.showinfo("提示", "请先选择要删除的学生。")
        return

    # 只处理一个选择
    s_id = str(tree.item(sel[0])['values'][0]).strip()   # 强制转为字符串并去除空格

    confirm = messagebox.askyesno("确认删除", f"确定要删除学号为 {s_id} 的学生吗？")
    if not confirm:
        return

    # 确保 students 是全局变量
    global students

    # 尝试找到学号完全相等的元素索引
    index = next((i for i, s in enumerate(students) if str(s['学号']).strip() == s_id), None)
    if index is not None:
        del students[index]
        save_data(students)
        refresh_table()
        messagebox.showinfo("成功", "删除成功")
    else:
        messagebox.showinfo("失败", "未找到该学生，删除失败")


def edit_student():
    sel = tree.selection()
    if not sel:
        messagebox.showinfo("提示", "请先选择要修改的学生。")
        return
    s_id = tree.item(sel[0])['values'][0]
    # 用下标定位当前学生
    index = next((i for i, s in enumerate(students) if str(s['学号']) == str(s_id)), None)
    if index is None:
        messagebox.showinfo("错误", "未找到该学生，无法修改。")
        return
    stu = students[index]

    edit_win = tk.Toplevel(root)
    edit_win.title("修改学生成绩")
    edit_win.grab_set()

    labels = ["姓名", "语文", "数学", "英语"]
    values = [stu["姓名"], stu["语文"], stu["数学"], stu["英语"]]
    entries = []
    for j, (label, val) in enumerate(zip(labels, values)):
        tk.Label(edit_win, text=label).grid(row=j, column=0, padx=5, pady=5)
        entry = tk.Entry(edit_win)
        entry.insert(0, str(val))
        entry.grid(row=j, column=1, padx=5, pady=5)
        entries.append(entry)

    def do_edit():
        name, chinese, math, english = [e.get().strip() for e in entries]
        try:
            chinese = int(chinese)
            math = int(math)
            english = int(english)
        except:
            messagebox.showwarning("成绩错误", "成绩需输入整数！")
            return
        # 直接修改students原有元素
        students[index]['姓名'] = name
        students[index]['语文'] = chinese
        students[index]['数学'] = math
        students[index]['英语'] = english
        # 如需重新按学号排序可加：students.sort(key=lambda x: int(x['学号']))
        save_data(students)  # This line is crucial!
        refresh_table()
        messagebox.showinfo("修改成功", "学生信息已更新")
        edit_win.destroy()

    tk.Button(edit_win, text="保存修改", command=do_edit).grid(row=4, column=0, columnspan=2, pady=10)


def search_student():
    def do_search():
        s_id = entry_id.get().strip()
        for s in students:
            if s['学号'] == s_id:
                total = s['语文'] + s['数学'] + s['英语']
                avg = total / 3
                messagebox.showinfo("查找结果",
                                    f"学号：{s['学号']}\n姓名：{s['姓名']}\n语文：{s['语文']}  数学：{s['数学']}  英语：{s['英语']}\n总分：{total}  平均分：{avg:.1f}")
                return
        messagebox.showinfo("查找结果", "未找到该学号的学生。")

    search_win = tk.Toplevel(root)
    search_win.title("查找学生成绩")
    search_win.grab_set()
    tk.Label(search_win, text="请输入学号：").pack(padx=10, pady=5)
    entry_id = tk.Entry(search_win)
    entry_id.pack(padx=10, pady=5)
    tk.Button(search_win, text="查找", command=do_search).pack(pady=8)


def stat_analyse():
    if not students:
        messagebox.showinfo("统计分析", "暂无学生信息。")
        return
    chinese = [s['语文'] for s in students]
    math = [s['数学'] for s in students]
    english = [s['英语'] for s in students]
    c_avg, c_max, c_min = sum(chinese) / len(chinese), max(chinese), min(chinese)
    m_avg, m_max, m_min = sum(math) / len(math), max(math), min(math)
    e_avg, e_max, e_min = sum(english) / len(english), max(english), min(english)
    msg = (f"语文 - 平均分：{c_avg:.1f} 最高分：{c_max} 最低分：{c_min}\n"
           f"数学 - 平均分：{m_avg:.1f} 最高分：{m_max} 最低分：{m_min}\n"
           f"英语 - 平均分：{e_avg:.1f} 最高分：{e_max} 最低分：{e_min}")
    messagebox.showinfo("成绩统计分析", msg)


def show_chart():
    if not students:
        messagebox.showinfo("提示", "暂无学生信息，无法绘制统计图。")
        return

    subjects = ['语文', '数学', '英语']

    # 防止分数字符串化，确保参与计算的数据全为int或float
    def get_scores(subj):
        return [int(s[subj]) for s in students if isinstance(s[subj], (int, float, str)) and str(s[subj]).isdigit()]

    means = []  # 平均分
    maxs = []  # 最高分
    mins = []  # 最低分
    for subj in subjects:
        scores = get_scores(subj)
        if scores:
            means.append(round(sum(scores) / len(scores), 2))
            maxs.append(max(scores))
            mins.append(min(scores))
        else:
            means.append(0)
            maxs.append(0)
            mins.append(0)

    x = np.arange(len(subjects))  # [0,1,2]
    width = 0.25

    plt.figure(figsize=(8, 6))
    bars1 = plt.bar(x - width, mins, width, label='最低分', color='#8dd3c7')
    bars2 = plt.bar(x, means, width, label='平均分', color='#ffffb3')
    bars3 = plt.bar(x + width, maxs, width, label='最高分', color='#bebada')

    plt.xticks(x, subjects, fontsize=12)
    plt.ylabel("分数", fontsize=12)
    plt.title("各科成绩统计", fontsize=14)
    plt.legend()

    # 给每个柱子标注数值
    for bar_group in [bars1, bars2, bars3]:
        for bar in bar_group:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, f'{yval}', ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.show()


def save_and_quit():
    save_data(students)
    root.destroy()


# ------ 按钮栏 ------
frame = tk.Frame(root)
frame.pack(fill=tk.X, pady=5)
btns = [
    ("导入数据", import_data),
    ("导出数据", export_data),
    ("添加学生", add_student),
    ("删除学生", delete_student),
    ("修改学生", edit_student),
    ("查找学生", search_student),
    ("统计分析", stat_analyse),
    ("成绩图表", show_chart),
    ("保存并退出", save_and_quit),
]
for txt, cmd in btns:
    tk.Button(frame, text=txt, command=cmd, width=12).pack(side=tk.LEFT, padx=5)

refresh_table()
root.mainloop()
