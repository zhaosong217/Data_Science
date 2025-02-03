# Python数据可视化库对比：Matplotlib vs Seaborn vs Plotly

## 目录
1. [Matplotlib](#1-matplotlib)
2. [Seaborn](#2-seaborn)
3. [Plotly](#3-plotly)
4. [对比总结](#对比总结)
5. [协作关系](#协作关系)
---

## 1. Matplotlib
### 核心特点
- **底层控制**：像素级精细调整能力
- **静态输出**：支持PDF/SVG/PNG等出版级格式
- **面向对象API**：通过`Figure`和`Axes`对象管理复杂布局
- **灵活但繁琐**：需手动设置坐标轴/图例等细节

### 典型代码示例
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, linestyle='--', color='#1f77b4', label='Trend')
ax.set_title("Publication-ready Figure", fontsize=14)
ax.legend()
ax.grid(True, linestyle=':')
plt.savefig("paper_figure.png", dpi=300)
```

### 适用场景
科研论文/技术报告中的高质量图表
需要精确控制每个元素的定制化需求
生成印刷级矢量图形（如PDF/SVG）

## 2. Seaborn
### 核心特点
统计可视化：内置回归分析/分布对比等统计图表
高级封装：pairplot/heatmap等一键生成复杂图形
美学优化：专业配色方案（如husl/Set2调色板）
数据整合：直接支持Pandas DataFrame输入
### 典型代码示例
```PYTHON
import seaborn as sns

sns.set_theme(context="notebook", style="darkgrid")
g = sns.relplot(
    data=df, x="total_bill", y="tip",
    hue="size", size="size", 
    palette="viridis", sizes=(40, 400)
)
g.fig.suptitle("Multivariate Analysis", y=1.02)
```
### 适用场景
数据探索阶段的快速可视化
多维数据关系分析
统计特性可视化（如分布/相关性）

## 3. Plotly
### 核心特点
交互操作：支持缩放/平移/数据点悬停查看
动态输出：生成可嵌入网页的HTML文件
三维支持：原生3D曲面/散点图绘制能力
Dash集成：配合Dash框架构建交互式仪表盘
### 典型代码示例
```PYTHON
import plotly.express as px

fig = px.scatter_3d(
    df, x='sepal_length', y='sepal_width', z='petal_length',
    color='species', size='petal_width', 
    title="Interactive 3D Visualization"
)
fig.update_layout(scene=dict(camera_eye=dict(x=1.5, y=1.5, z=0.8)))
fig.show()
```
### 适用场景
网页端交互式数据展示
地理信息/三维数据可视化
实时数据监控仪表盘
___
## 对比总结
|特性|Matplotlib|Seaborn|Plotly|
|---|---|---|---|
学习曲线|陡峭|中等|中等（需学HTML交互）
渲染速度|快（静态）	|快	|较慢（动态渲染）
交互性|无（需额外工具）	|无|	原生支持
输出格式|	PNG/PDF/SVG|	PNG/PDF|	HTML/WebGL
最佳场景|	出版级图表|	统计探索|	Web交互可视化

## 协作关系
混合使用示例
```PYTHON
import matplotlib.pyplot as plt
import seaborn as sns

# 使用Seaborn主题风格
sns.set_theme(font_scale=1.2, rc={"axes.facecolor": "#f0f0f0"})

# 使用Matplotlib底层API绘制
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].hist(df['value'], bins=30, edgecolor='black')
sns.kdeplot(df['value'], ax=axs[1], fill=True)

plt.tight_layout()
plt.savefig("hybrid_plot.pdf")
```
## 选择策略
📊 快速原型 → Seaborn
✏️ 精细调整 → Matplotlib
🖱️ 交互需求 → Plotly
🌐 网页部署 → Plotly + Dash