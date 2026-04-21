## 1. Project Setup

- [x] 1.1 使用 `uv init` 初始化项目并创建虚拟环境
- [x] 1.2 使用 `uv add` 添加必要的依赖（如有）
- [x] 1.3 初始化主程序脚本 `main.py`
- [x] 1.4 验证通过 `uv run python main.py` 能够启动程序

## 2. Core Logic Implementation

- [x] 2.1 实现哈希计算类，支持 MD5, SHA-1, SHA-256
- [x] 2.2 实现大文件分块读取逻辑，防止内存溢出
- [x] 2.3 封装哈希比对逻辑

## 3. GUI Development

- [x] 3.1 使用 tkinter 设计主窗口布局
- [x] 3.2 添加文件选择按钮和路径显示标签
- [x] 3.3 添加算法选择下拉菜单
- [x] 3.4 添加预期哈希值输入框及比对结果标签
- [x] 3.5 添加“开始计算”按钮

## 4. Integration & Concurrency

- [x] 4.1 将 GUI 与哈希计算逻辑集成
- [x] 4.2 使用 `threading` 实现后台计算，确保 UI 响应
- [x] 4.3 实现计算过程中的状态更新（如“计算中...”）

## 5. Testing & Refinement

- [x] 5.1 进行单元测试验证哈希算法准确性
- [x] 5.2 测试不同大小文件的校验表现
- [x] 5.3 优化界面样式和交互逻辑
- [x] 5.4 创建 README.md 并记录启动命令
