## ADDED Requirements

### Requirement: Trigger on Tag Push
GitHub Actions 工作流必须在推送以 `v*` 开头的 tag 时自动触发。

#### Scenario: Workflow triggered by version tag
- **WHEN** 用户推送一个名为 `v1.0.0` 的 tag
- **THEN** GitHub Actions 启动 `build.yml` 中定义的工作流

### Requirement: Build Windows Executable
工作流必须在 Windows 环境下运行，并使用 PyInstaller 将 Python 项目打包成单个 `.exe` 文件。

#### Scenario: Successful compilation on Windows
- **WHEN** 工作流在 `windows-latest` 运行器上执行
- **THEN** 构建工件中生成一个可独立运行的 `.exe` 文件

### Requirement: Versioned Executable Filename
生成的 `.exe` 文件名必须包含触发工作流的 tag 版本号（例如 `FileChecksumTool-v1.0.0.exe`）。

#### Scenario: Executable named with version
- **WHEN** 用户推送 tag `v1.2.3` 触发构建
- **THEN** 构建产生的工件命名为 `FileChecksumTool-v1.2.3.exe`

### Requirement: Upload to GitHub Release
工作流必须将生成的 `.exe` 文件自动上传到与触发 tag 对应的 GitHub Release 页面。

#### Scenario: Executable attached to release
- **WHEN** 构建步骤成功完成
- **THEN** 系统创建一个新的 Release（如果尚不存在），并将 `.exe` 文件作为附件上传
