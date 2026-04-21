## Why

用户需要一个简单、直观的桌面工具来校验文件的完整性，确保下载或传输的文件未被篡改。目前缺乏一个集成的、支持多种常用算法（如 MD5, SHA-1, SHA-256）的轻量级 Python 桌面应用。

## What Changes

- 开发一个基于 Python 的桌面应用程序界面 (GUI)。
- 支持选择单个或多个文件进行校验。
- 提供 MD5、SHA-1、SHA-256 等常用校验算法。
- 显示校验进度和结果。
- 支持将结果与预期值进行比对。

## Capabilities

### New Capabilities
- `file-selection`: 允许用户通过文件浏览器选择要校验的文件。
- `checksum-calculation`: 执行所选算法（MD5, SHA-1, SHA-256 等）的计算。
- `result-comparison`: 提供一个输入框，让用户粘贴预期的校验值并自动进行比对。
- `gui-interface`: 提供图形用户界面，展示操作和结果。

### Modified Capabilities

## Impact

- 新项目，不影响现有代码。
- 依赖：`hashlib` (内置), `tkinter` (GUI 框架)。
