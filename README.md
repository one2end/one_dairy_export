# one_dairy_export

一本日记导出工具
菜鸡试手作品，计划功能只有两个。

* 将一本日记txt文本，json文件拆分为按日期的txt文本。
* 将日记导入印象笔记并且调整其中的标题日期。

## 日记拆分

从一本日记手机端，设置，导出txt或者备份数据。或者从坚果云直接下载json文件。

代码示例：

```python
import one_dairy_export as ode

addr = 'json、txt文件绝对地址'
ode.split(addr,dir=True)
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
import one_dairy_export as ode
addr = 'enex文件绝对地址'
ode.enex(addr)

```

## 有图片的日记

建议直接官方导出为PDF比较好保存。如果需求大也可以后续增加将备份的图片标题改为日记日期的功能。
