# Machine Learning with Python
## Objectives:
- [ ] Describe how machine learning plays a pivotal role in various career paths
- [ ] Articulate the various stages involved in the machine learning lifecycle
- [ ] Discuss how various machine learning models work
- [ ] Implement machine learning models using Python and scikit-learn
- [ ] Solve data-related problems using machine-learning methods
___
## Module 1 - Linear and Logistic Regression
### 快速探索数据内容
`df.sample(5)`可以用来随机抽样5组数据，查看数据内容
`df.describe`可以用来查看数据内容中数据的统计特性
`df.corr()`可以用来快速查看数据间的相关性，一般相关性>0.85就是强相关
还可以用plot绘图的方式快速查看数据相关性：
```python
axes = pd.plotting.scatter_matrix(df, alpha=0.2, figsize=(10,10))
# need to rotate axis labels so we can read them
for ax in axes.flatten():
    ax.xaxis.label.set_rotation(90)
    ax.yaxis.label.set_rotation(0)
    ax.yaxis.label.set_ha('right')

plt.tight_layout()
plt.gcf().subplots_adjust(wspace=0, hspace=0)
plt.show()
```
### Preprocess selected features
对输入的特征需要进行标准化，避免模型因为某个特征的量级而无意中偏向它。一般的处理方法是减去均值，然后除以标准差，可以使用scikit-learn库来完成。（注意：这种方法在实际使用中用来评估模型时，一般会对测试集和训练集分别处理，不能对整个数据集处理）
```python
from sklearn import preprocessing

std_scaler = preprocessing.StandardScaler()
X_std = std_scaler.fit_transform(X)
```
### Create train and test datasets
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_std,y,test_size=0.2,random_state=42)
```

## Module 2 - Building Supervised Learning Models

## Module 3 - Building Unsupervised Learning Models

## Module 4 - Evaluating and Validating Machine Learning Models
