## ADDED Requirements

### Requirement: Hash Comparison
系统必须允许用户输入预期的哈希值，并与计算结果进行比对。

#### Scenario: Matching Hash
- **WHEN** 用户输入的哈希值与计算结果一致
- **THEN** 系统显示绿色“匹配”标识。

#### Scenario: Mismatching Hash
- **WHEN** 用户输入的哈希值与计算结果不一致
- **THEN** 系统显示红色“不匹配”标识。
