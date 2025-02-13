## 什么是LaTeX?
LaTeX 使用纯文本文件作为输入，并通过预定义的命令和语法描述文档结构和格式。LaTeX 可以处理复杂的数学公式、表格、图表和引用，并提供高级功能如自动编号和交叉引用。

## 如何使用LaTeX?
1. 需要使用一对$符号，在公式的首尾。如果首尾使用两个$$，则表示要把公式居中。
2. 使用\begin{equation}和\end{equation}来表示一个公式环境，这样公式会自动编号。
    例如：\begin{bmatrix}和\end{bmatrix}表示矩阵环境。
3. \cdots表示水平省略号，\vdots表示垂直省略号，\ddots表示对角线省略号。
    例如：一个上三角形矩阵
    $$A_{delta} = 
    \begin{bmatrix}
    1 & 1 & 1 & \cdots & 1 \\
    0 & 1 & 1 & \cdots  & 1 \\
    0 & 0 & 1 & \cdots  & 1 \\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & 0 & \cdots  & 1
    \end{bmatrix}$$
4. -{\frac {1}{2}}表示分数，\sqrt{}表示根号，\left(和\right)表示括号，\left[和\right]表示方括号，\left\{和\right\}表示花括号。
    例如：一元高斯概率密度函数
    $$f_X(x)={\frac {1}{\sigma {\sqrt {2\pi }}}}\exp \left({-{\frac {1}{2}}\left({\frac {x-\mu }{\sigma }}\right)^{2}}\right)$$
5. 字体样式
    - \textbf{}表示加粗
    - \textit{}表示斜体
    - \underline{}表示下划线
    - \textsc{}表示小写字母转大写
    - \textsf{}表示无衬线字体
    - \texttt{}表示打字机字体
    - \textsl{}表示倾斜字体
    ![alt text](<CleanShot Preview-2025.02.11.png>)
6. $$x^2 - y^2 = \left(x+y\right)\left(x-y\right)$$
$$a_{n}x^{n} + a_{n-1}x^{n-1} + \cdots + a_{1}x + a_{0}$$
$$\sum_{k=0}^{n}a_{k}x^{k}$$
$$\int_{a}^{b}f(x) \mathrm {d}x$$
$$\int_{-\infty}^{\infty}\exp(-x^{2})\mathrm{d}x={\sqrt{\mathrm{\pi}}}$$
$$x_{1,2} = \frac {-b\pm\sqrt {b^2-4ac}}{2a}$$
$$\frac {1}{x+1} + \frac {1}{x-1} = \frac {2x}{x^2-1}$$ 
$$x^{\prime \prime}$$
$$ \pm2 $$
$$ \int_0^2x^2 \mathrm{d}x $$ 
$$ \sum_{k=0}^{\infty}k $$ 
$$ \bar{x} $$
$$ \hat{x} $$
$$ \overrightarrow{x} $$
$$ \alpha \beta \gamma \delta \epsilon \theta\\
\zeta \eta \lambda \mu \pi \\
\rho \sigma \tau \phi \psi \omega$$当需要对应大写希腊文时，用大写字母开头即可，例如$\Gamma$
$$ 3 \times 7 = 21 \\
81 \div 9 = 9 \\
向量乘\otimes \\
小于等于\leq \\
远小于\ll \\
大于等于\geq \\
远大于\gg \\
不等于\neq \\
梯度算子\nabla \\
角度\angle \\
相似\sim \\
存在\exists \\
任意\forall \\
真子集\subset \\
真超集\supset \\
子集\subseteq \\
空集\varnothing \\
交集\cap \\
并集\cup \\
属于\in \\
不属于\notin \\
因为\because \\
所以\therefore \\
绝对值|x| \\
恒等于\equiv \\
约等于\approx \\
偏导\partial \\
$$
#### **例子**
$$ ax^2 + bx + c = 0 \ (a \neq 0) \\
sin^2\theta +cos^2\theta = 1 \\
sin(\alpha \pm \beta)=sin\alpha cos\beta \pm cos\alpha sin\beta \\
tan(\alpha \pm \beta) = \frac {tan\alpha \pm tan\beta}{1 \mp tan\alpha tan\beta} \\
\left( \sum_{i=0}^{n}a_i\right) \left(\sum_{j=0}^{n}b_j\right)=\sum_{i=0}^{n}\sum_{j=0}^{n}a_ib_j \\
exp(x)=\lim_{n\to \infty}\left(1+\frac{x}{n}\right)^n \\
\int_{-\infty}^{\infty}exp(-x^2)\mathrm{d}x=\sqrt{\pi} \\
\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}exp(-(x^2+y^2))\mathrm{d}x\mathrm{d}y=\pi \\
\frac{\partial^2f}{\partial y \partial x} = \frac {\partial }{\partial y}\left(\frac {\partial f}{\partial x}\right) = f_{xy}^{\prime \prime}$$
#### 矩阵的表达
$$ \mathbf a = {\begin{bmatrix} a_1 \\
a_2 \\ a_3 \end{bmatrix}} = [a_1\ a_2\ a_3]^T \\
\boldsymbol A={\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}} \\
(\boldsymbol {A+B})^T = \boldsymbol A^T + \boldsymbol B^T \\
(\boldsymbol A^T)^{-1} = (\boldsymbol A^{-1})^T$$


