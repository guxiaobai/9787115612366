# 第 1 章 Python数据模型

> 为什么获取容器大小不使用 collection.len()，而是 使用 len(collection)？



## Python 数据模型



* 双下划线方法





## 1.2 

```python
# len()
def __len__:
  
# []  
def __getitem__
```







## 1.3 特殊方法如何使用的

* 特殊方法供 Python 解释器调用

```python

for i in x:
  
iter(x)

x.__iter__
x.__getitem__
```


## 1.3.2 字符串表示形式

```python
# 控制台： repr
__repr__


# str()， print调用
__str__

```
* 如果必须二选一的话，请选择 __repr__ 方法



## 1.3.3

```python
bool(x)
x.__bool__()
```


## 1.3.4 容器API

