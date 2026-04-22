## Context

项目目前是一个单文件的 Python Tkinter 应用程序。为了方便非技术用户使用，需要将其打包为 Windows 平台的 `.exe` 可执行文件。手动打包过程繁琐且难以保证环境一致性，因此决定引入 GitHub Actions 进行自动化构建。

## Goals / Non-Goals

**Goals:**
- 自动化 Windows 平台构建。
- 在推送 tag 时自动创建 GitHub Release。
- 生成的 `.exe` 文件应该是单文件形式且包含 GUI 支持。

**Non-Goals:**
- 目前不考虑 macOS 或 Linux 平台的打包。
- 不包括代码签名（Code Signing），因为这需要付费证书。

## Decisions

- **构建工具: PyInstaller**: PyInstaller 是 Python 社区最成熟的打包工具，支持将脚本及其依赖打包成单个可执行文件。
- **打包模式: --onefile --noconsole --name**: 由于是 GUI 应用程序，我们需要使用 `--noconsole` 隐藏终端窗口，并使用 `--onefile` 简化分发。通过 `--name` 参数动态指定包含版本号的文件名。
- **版本号获取**: 使用 GitHub Actions 的环境变量 `${{ github.ref_name }}` 来获取触发构建的 tag 名称。
- **CI 环境: windows-latest**: 既然目标是生成 Windows `.exe`，直接在 GitHub 提供的 Windows 虚拟机上构建是最简单可靠的，避免了复杂的交叉编译。
- **Release 工具: softprops/action-gh-release**: 这是一个功能丰富且广泛使用的 GitHub Action，能够处理 Release 的创建和资产上传。

## Risks / Trade-offs

- **[Risk] 杀毒软件误报** ➔ PyInstaller 生成的未签名 `.exe` 经常被 Windows Defender 误报为病毒。
  - **Mitigation**: 在项目 README 中添加说明，建议用户在使用时注意，或者未来考虑代码签名。
- **[Risk] 构建环境差异** ➔ 不同的 Python 版本或库版本可能导致构建出的 `.exe` 行为不一致。
  - **Mitigation**: 在 GitHub Actions 中明确指定 Python 版本（与 `pyproject.toml` 一致，即 3.11+）。
