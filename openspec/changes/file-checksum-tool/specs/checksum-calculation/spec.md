## ADDED Requirements

### Requirement: Algorithm Selection
系统必须支持 MD5, SHA-1, SHA-256 三种哈希算法。

#### Scenario: Select Algorithm
- **WHEN** 用户在下拉框中选择“MD5”
- **THEN** 系统将当前计算模式设置为 MD5。

### Requirement: Hash Calculation
系统必须能够计算所选文件的哈希值，并在计算过程中保持界面不卡顿。

#### Scenario: Calculate MD5 for File
- **WHEN** 用户选择了一个文件并点击“计算”
- **THEN** 系统在后台线程计算 MD5，计算完成后在界面上显示 32 位十六进制字符串。
