## 1. 基础设施准备

- [x] 1.1 创建 `.github/workflows` 目录
- [x] 1.2 在本地环境中验证 `pyinstaller` 的打包基本指令

## 2. GitHub Actions 配置

- [x] 2.1 创建 `.github/workflows/build.yml` 文件
- [x] 2.2 配置工作流触发器（仅在推送 `v*` 形式的 tag 时触发）
- [x] 2.3 编写构建 Job，包括安装 Python 环境和安装依赖（如 `pyinstaller`）
- [x] 2.4 编写打包步骤，使用 `pyinstaller --onefile --noconsole main.py`
- [x] 2.5 编写发布步骤，使用 `softprops/action-gh-release` 上传生成的 `.exe`

## 3. 验证与文档

- [x] 3.1 验证 `.github/workflows/build.yml` 的 YAML 语法正确性
- [x] 3.2 在 README.md 中添加关于如何触发自动发布和下载安装包的说明
