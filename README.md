# 文件内容校验工具 (File Checksum Tool)

这是一个基于 Python 的轻量级桌面工具，用于校验文件的完整性。

## 功能特性

- 支持多种哈希算法：MD5, SHA-1, SHA-256。
- 支持大文件分块读取，防止界面卡死。
- 支持将计算结果与预期哈希值进行实时比对。
- 简洁的图形化操作界面。

## 环境要求

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) (推荐的包管理工具)

## 启动说明

本项目使用 `uv` 进行环境管理。请在项目根目录下运行以下命令启动程序：

```bash
uv run python main.py
```

如果你没有安装 `uv`，也可以直接使用标准的 Python 环境运行（需确保已安装 `tkinter`）：

```bash
python main.py
```

## 测试

运行单元测试：

```bash
python test_hash.py
```
