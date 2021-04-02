# python中一切皆对象，每个对象由于 标识id 类型type 值print 组成
# 对象本质是一个内存块 拥有特定的值
# 变量是对象的引用 存储对象的地址 变量通过地址引用对象
# 变量位于栈内存 对象位于堆内存
# python是动态类型语言 变量不需要显式定义 强类型+每个对象都有数据类型

## python驻留机制
## 对于合规的字符串（下划线 数字 字母）使用同一对象
## a="a_f" b="a_f"  a is b True

# 类
## __new__用于创建对象，
## __init__初始化对象，给实体赋值

# 模块的发布
# from distutils.core import setup
# setup(name = "", version="",description="",author="",py_modules=[])