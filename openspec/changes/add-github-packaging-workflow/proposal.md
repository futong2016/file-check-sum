## Why

当前项目缺乏自动化的分发流程。每次发布新版本时，手动构建 Windows 可执行文件并上传到 GitHub Release 既耗时又容易出错。通过集成 GitHub Actions，我们可以在推送 tag 时自动完成构建和发布过程，确保分发版本的一致性和及时性。

## What Changes

- 在 `.github/workflows/` 目录下添加 `build.yml` 配置文件。
- 配置工作流以在推送以 `v*` 开头的 tag 时触发。
- 使用 PyInstaller 或类似的工具在 Windows 运行器上打包 Python 代码为 `.exe` 文件，文件名应包含版本号（例如 `FileChecksumTool-v1.0.0.exe`）。
- 自动将生成的带版本号的 `.exe` 文件作为资源上传到 GitHub Release。

## Capabilities

### New Capabilities
- `github-release-workflow`: 自动化构建和发布流程，专门针对 Windows 平台的 `.exe` 打包。

### Modified Capabilities
<!-- 无现有需求变更 -->

## Impact

- **项目结构**: 新增 `.github/workflows/` 目录。
- **构建依赖**: 可能需要配置 `pyproject.toml` 或专门的构建脚本以配合 PyInstaller。
- **CI/CD**: 引入 GitHub Actions 作为项目的持续集成/持续部署工具。
