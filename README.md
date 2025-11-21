# safeinterp

**Safe, Intelligent, and Adaptive 1D Interpolation Engine for Python**

> *Robust curve fitting, multi-segment evolution, and safe extrapolation — designed for numerical modeling, energy planning, and economic scenarios.*

<p align="center">
  <a href="https://github.com/mrbinxu2025-dotcom/safeinterp/stargazers">
    <img src="https://img.shields.io/github/stars/mrbinxu2025-dotcom/safeinterp?style=flat-square&logo=github&label=Stars" alt="GitHub Stars" />
  </a>
  <a href="https://github.com/mrbinxu2025-dotcom/safeinterp/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/mrbinxu2025-dotcom/safeinterp?style=flat-square&color=blue" alt="License" />
  </a>
  <a href="https://pypi.org/project/safeinterp/">
    <img src="https://img.shields.io/pypi/v/safeinterp?style=flat-square&color=orange" alt="PyPI Version" />
  </a>
  <a href="https://github.com/mrbinxu2025-dotcom/safeinterp/issues">
    <img src="https://img.shields.io/github/issues/mrbinxu2025-dotcom/safeinterp?style=flat-square" alt="Issues" />
  </a>
</p>

---

## 📖 Introduction / 简介

**safeinterp** 是一个专为数值稳定性设计的 Python 插值库。它不仅提供常规的插值功能，更专注于解决实际工程中常见的“脏数据”和“边界爆炸”问题。

大多数插值库在面对乱序数据、重复点或极短区间时容易报错或产生奇异值；而 safeinterp 的目标是：
> **In any scenario, provide a curve that is safe, smooth, and physically plausible.**
> (在任何场景下，都提供一条安全、平滑且符合物理直觉的曲线。)

---

## ✨ Key Features / 核心特性

### 🛡️ **Robust & Safe (稳健安全)**
- **自动清洗**：自动处理 `x` 乱序、重复点、`NaN/Inf` 以及两点过近导致的数值奇异。
- **安全外推**：`extrapolate="auto"` 模式自动评估趋势，优先选择稳健的边界行为，防止指数爆炸。

### 🧠 **Intelligent "Auto" Mode (智能模式)**
- **自适应选择**：对每一小段区间，自动从 `linear`, `power`, `exp`, `logistic` 等 8 种模式中择优。
- **趋势约束**：内置代价函数考虑了整体趋势和单调性，极大减少了传统插值的“反冲”和“振铃”现象。

### 📈 **Rich Curve Families (丰富的曲线族)**
支持手动指定多种物理/数学含义明确的曲线形状：
- **Growth**: `linear` (线性), `power` (幂律), `exp` (指数), `logistic` (S形增长)
- **Transition**: `sin` / `cos` (三角缓动), `poly2` / `poly3` (平滑多项式/Smoothstep)

### 📦 **Batch Processing (批量插值)**
- 专为多情景模拟设计：`batch_interp_curve` 可一次性处理成百上千条曲线。
- **灵活配置**：支持不同序列继承公共坐标轴，或独立指定参数。

### ⚡ **Lightweight (轻量级)**
- **Pure NumPy**：仅依赖 `numpy`，无其他重型依赖，易于集成到任何环境中。

---

## 🆚 Why safeinterp? / 对比

| 常见痛点 (Pain Points) | ❌ 普通插值库 (scipy/numpy) | ✅ safeinterp |
| :--- | :--- | :--- |
| **数据质量差** (乱序/重复/NaN) | 报错 / 产生 NaN / 结果震荡 | **自动排序、去重、清洗** |
| **区间极短** (数值不稳定) | 斜率爆炸 / 浮点溢出 | **自动修正，保证数值稳定** |
| **外推风险** (Extrapolation) | 简单的线性延伸或无外推 | **多策略智能外推 + 自动回退** |
| **复杂形态** (Multi-segment) | 只能全局统一模式 | **支持分段指定不同形状 (Mode/K)** |
| **非单调趋势** | 容易产生非物理的反转 | **内置趋势检测与约束** |

---

## 💻 Installation / 安装

### Option 1: Install from PyPI (Recommended after release)
```bash
pip install safeinterp
````

### Option 2: Install from Source (For latest updates)

```bash
git clone [https://github.com/mrbinxu2025-dotcom/safeinterp.git](https://github.com/mrbinxu2025-dotcom/safeinterp.git)
cd safeinterp
pip install .
```

-----

## 🚀 Quick Start / 快速上手

### 1\. Basic Usage (基础插值)

```python
import numpy as np
from safeinterp import interp_curve

# 原始数据
x = [2020, 2030, 2040, 2050]
y = [100,  150,  280,  300]

# 目标点（包含外推区域）
new_x = np.arange(2020, 2061, 1)

# 一行代码完成插值 + 外推
values = interp_curve(x, y, new_x)
```

### 2\. Auto Mode (智能模式)

让算法自动寻找最符合数据趋势的平滑曲线：

```python
# mode="auto" 会自动平衡平滑度和趋势贴合度
values = interp_curve(x, y, new_x, mode="auto", extrapolate="auto")
```

### 3\. Manual Segments (手动分段控制)

精细控制每一段的演化逻辑（例如：先指数增长，后线性趋稳）：

```python
segments = [
    {"mode": "exp", "k": 1.5},    # 2020-2030: 快速指数增长
    {"mode": "linear"},           # 2030-2040: 线性过渡
    {"mode": "logistic", "k": 4}  # 2040-2050: S形饱和
]

values = interp_curve(x, y, new_x, segments=segments)
```

### 4\. Batch Interpolation (批量处理)

适用于能源/经济模型中的多区域、多变量处理：

```python
from safeinterp import batch_interp_curve

data_config = {
    "solar_capacity": {
        "y": [0, 50, 200], 
        "mode": "exp"       # 太阳能按指数增长
    },
    "coal_capacity": {
        "y": [500, 480, 200], 
        "mode": "logistic", # 煤电按 S 形退出
        "extrapolate": "edge"
    }
}

# 共享时间轴
results = batch_interp_curve(
    data_config,
    common_x=[2020, 2030, 2050],
    common_new_x=range(2020, 2061)
)
```

-----

## 📊 Visualization / 效果展示

*(Coming soon: Visual comparison charts)*

> 💡 **Tip**: Check the `examples/` directory for Jupyter Notebooks demonstrating advanced usage.

-----

## 🗺️ Roadmap / 路线图

  - [x] v0.1: 核心插值引擎 (Core Engine) & 批量接口 (Batch API)
  - [ ] v0.2: 增加单调 Hermite 插值模式 (PCHIP 改进版)
  - [ ] v0.3: 2D Surface Interpolation (二元曲面插值)
  - [ ] v0.4: Visualization Helpers (内置简单绘图辅助)
  - [ ] v1.0: 稳定版发布

-----

## 🤝 Contributing / 贡献指南

我们非常欢迎社区贡献！无论是修复 Bug、提交新特性，还是完善文档。

1.  Fork 本仓库
2.  创建特性分支 (`git checkout -b feature/AmazingFeature`)
3.  提交更改 (`git commit -m 'Add some AmazingFeature'`)
4.  推送到分支 (`git push origin feature/AmazingFeature`)
5.  提交 Pull Request

如果你在**能源规划、经济预测、环境模拟**等领域使用了 `safeinterp`，欢迎在 Issue 中告诉我们要优化哪些特定场景！

-----

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

-----
