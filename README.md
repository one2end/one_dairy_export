# one_dairy_export

一本日记导出工具
菜鸡试手作品，计划功能只有两个。

* 将一本日记json文件拆分为按日期的txt文本。
* 将日记导入印象笔记并且调整其中的标题日期。

## 直接运行

* 将dairy.json 、enex 和dairy.py 放在同一文件夹下。
* shift右键，运行powershell或者cmd。
* 输入`python dairy.py`回车。
* 输入文件序列，数字。对于是否需要文件夹分类输入True和False
* 运行原理往下看

## 日记拆分

从一本日记从坚果云直接下载json文件。

代码示例：

```python
import dairy

addr = 'json、txt文件绝对地址'
dairy.split_json(addr,dir=True)

# 将该文件进行拆分，dir是带有按照年月的文件夹参数，如果是False，则所有日记输出在一个文件夹内。
```

## 导入印象笔记

印象笔记的接口没时间调，采用比较傻但是能用的办法。

1. 新建笔记本，将txt日记导入印象笔记。
2. 然后导出enex格式文件，删除导入的文件
3. 针对enex文件修改标题，去除后缀.txt，修改创建时间为日记时间
4. 重新导入修改过后的enex

代码示例：

```python
import dairy
addr = 'enex文件绝对地址'
dairy.change_enex(addr)

```


## 有图片的日记

建议直接官方导出为PDF比较好保存。如果需求大也可以后续增加将备份的图片标题改为日记日期的功能。
