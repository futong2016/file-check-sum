## Context

用户需要一个轻量级、跨平台的工具，通过计算哈希值（MD5, SHA-1, SHA-256）来验证文件完整性。本项目将使用 Python 开发，利用其内置的 `hashlib` 和 `tkinter`。

## Goals / Non-Goals

**Goals:**
- 提供简单易用的 GUI。
- 支持 MD5, SHA-1, SHA-256 计算。
- 支持单个文件和批量文件选择。
- 实现与预期哈希值的自动比对。

**Non-Goals:**
- 不支持文件夹同步。
- 不提供复杂的加密/解密功能。
- 不打算处理超大型文件（例如超过 100GB）的实时分块进度显示。

## Decisions

- **GUI Framework**: 选择 `tkinter`。
  - **理由**: Python 内置，无需额外安装，适合轻量级工具，跨平台支持良好。
- **Package Management**: 使用 `uv`。
  - **理由**: 现代、高性能的 Python 包和项目管理器，提供极快的依赖安装和隔离的虚拟环境。
- **Execution Environment**: 在 `uv` 虚拟环境中运行。
  - **理由**: 确保依赖隔离，通过 `uv run` 可以方便地在一致的环境中启动程序。
- **Hash Computation**: 使用 `hashlib`。
  - **理由**: Python 标准库，安全、稳定且支持多种算法。
- **Concurrency**: 使用 `threading` 处理耗时计算。
  - **理由**: 防止在计算大文件哈希时界面卡死，确保良好的用户体验。

## Risks / Trade-offs

- [界面响应] -> 计算大文件哈希时需异步处理。
- [多算法性能] -> 暂不实现并行计算（即同时算 MD5 和 SHA-256），按需顺序计算以简化设计。
