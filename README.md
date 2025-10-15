# 学生成绩管理系统 (Student Grade Management System)

## 📖 项目简介

一个基于 Python tkinter 开发的图形化学生成绩管理系统，提供完整的学生信息管理、成绩统计分析及数据可视化功能。该系统专为教育工作者设计，简化成绩管理流程，提高工作效率。

**🚀 开箱即用**：项目已使用 PyInstaller 打包为可执行文件，无需安装 Python 环境即可直接运行！

## ✨ 核心功能

### 📊 基础管理
- **学生信息管理** - 完整的增删改查(CRUD)操作
- **成绩录入** - 支持语文、数学、英语三科成绩录入
- **数据验证** - 学号唯一性检测和成绩格式验证
- **批量操作** - 支持数据导入导出功能

### 📈 智能分析
- **成绩统计** - 自动计算各科平均分、最高分、最低分
- **数据可视化** - 使用 matplotlib 生成成绩统计柱状图
- **总分计算** - 自动计算学生总分和平均分

### 💾 数据安全
- **持久化存储** - 自动保存数据到本地文件
- **数据备份** - 支持导入导出，防止数据丢失
- **编码安全** - 完整的 UTF-8 中文支持

## 🎯 快速开始

### 方式一：直接运行可执行文件（推荐）
1. 前往 [Releases](https://github.com/wenfeichen068/scoreManageGUI.git) 页面
2. 下载最新版本的 `scoreManageGUI.exe`
3. 双击即可运行，无需安装任何依赖

### 方式二：从源码运行
#### 环境要求
```bash
Python 3.6+
matplotlib
numpy
```

#### 安装运行
```bash
# 克隆项目
git clone https://github.com/wenfeichen068/scoreManageGUI.git

# 进入目录
cd student-grade-management

# 安装依赖
pip install -r requirements.txt

# 运行系统
python scoreManageGUI.py
```

## 📁 项目结构

```
student-grade-management/
├── dist/
│   └── scoreManageGUI.exe    # 🎯 主程序可执行文件
├── build/                    # 🔧 临时构建文件（可忽略）
├── scoreManageGUI.spec       # ⚙️ PyInstaller配置文件（可忽略）
├── scoreManageGUI.py         # 📝 源代码文件
├── grades.txt               # 💾 示例数据文件
├── requirements.txt         # 📦 依赖包列表
└── README.md               # 📖 项目说明
```

## 🛠 构建说明

### 使用 PyInstaller 打包

如果你想从源码构建可执行文件：

```bash
# 安装 PyInstaller
pip install pyinstaller

# 打包程序（单文件模式）
pyinstaller --onefile --windowed scoreManageGUI.py

# 或者使用提供的spec文件
pyinstaller scoreManageGUI.spec
```

### 构建选项说明
- `--onefile`: 打包为单个可执行文件
- `--windowed`: 不显示命令行窗口（纯GUI程序）
- `--icon=icon.ico`: 可添加自定义图标

## 🎯 使用指南

### 首次使用
1. 下载并运行 `dist/scoreManageGUI.exe`
2. 系统会自动创建 `grades.txt` 数据文件
3. 开始添加学生信息或导入现有数据

### 数据导入
- 支持从标准格式的文本文件导入
- 格式：`学号,姓名,语文成绩,数学成绩,英语成绩`
- 导入时自动去重和排序

### 数据备份
- 定期使用"导出数据"功能备份重要数据
- 数据文件为纯文本格式，便于查看和迁移

## 🖥 系统要求

- **操作系统**: Windows 7/8/10/11, macOS, Linux
- **内存**: 至少 512MB RAM
- **存储**: 至少 100MB 可用空间
- **分辨率**: 1024×768 或更高

## 🐛 常见问题

**Q: 运行时提示缺少 DLL 文件？**
A: 请确保下载完整的发布包，或从 Releases 页面重新下载。

**Q: 程序无法启动？**
A: 尝试以管理员权限运行，或检查杀毒软件是否误报。

**Q: 如何重置数据？**
A: 删除同级目录下的 `grades.txt` 文件即可。

**Q: 支持多少学生记录？**
A: 理论上无限制，实际受计算机内存限制。

## 🔄 更新日志

### v1.0.0
- ✅ 基础成绩管理功能
- ✅ 数据导入导出
- ✅ 成绩统计分析
- ✅ 数据可视化图表
- ✅ 可执行文件打包

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来改进这个项目！

1. Fork 本仓库
2. 创建特性分支：`git checkout -b feature/AmazingFeature`
3. 提交更改：`git commit -m 'Add some AmazingFeature'`
4. 推送到分支：`git push origin feature/AmazingFeature`
5. 提交 Pull Request

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🆘 技术支持

如果遇到问题，请：
1. 查看本 README 的常见问题部分
2. 在 [Issues](https://github.com/your-username/student-grade-management/issues) 页面搜索相关问题
3. 提交新的 Issue 并详细描述问题

---

**🎉 立即下载体验，让成绩管理变得更简单、更智能！**

---
*如果这个项目对您有帮助，请给个 ⭐ Star 支持一下！*

