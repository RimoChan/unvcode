# 【幼女Code】反和谐超级武器！

你还在因为在群名里加入色图而被QQ改成一个「*」而苦恼吗？你还在因为在红包祝福里写「年轻人好好自慰」而白白花钱吗？

快使用**幼女Code**吧！

**幼女Code**使用Librian幼女娱乐中心最新研发的**unvcode**，可以快速解决你的一切问题！


## 原理

在unicode中<sub>(注意这不是unvcode)</sub>，有很多字，它们看起来长得很像，但是它们的ord不一样。

这样一来，只要把字符串里原本的字……啊，点到为止，再说下去就不好玩了。


## 接口

```python
def unvcode(s: str, skip_ascii=True) -> Tuple[str, Tuple[float, ...]]:
```

输入一个字符串，返回改变后的字符串、每个字符被改变后与原本的像素差异<sub>(没变就是None)</sub>。

如果`skip_ascii`开启则会跳过ascii字符。

样例: 

```python
import unvcode
s, var = unvcode.unvcode('Librian幼女娱乐中心开业了，注册即送色图！')
print(s) 
print(var) 
```

输出: 
```text
Librian幼⼥娱乐㆗⼼开业了，注册即送⾊图！
(None, None, None, None, None, None, None, None, 0.0, None, None, 0.009146429779930796, 0.0, None, None, 0.0, None, None, None, None, None, 0.0, None, None)
```

注意，这句话看起来的样子取决于你的系统字体，所以我也不知道它会是什么样的……

## 安装

```
pip install unvcode
```

然后在代码里`import unvcode`就行了，就是这么简单！

<sub>(我还没发好包，等等先别装……)</sub>


## 结束

如果你觉得幼女Code对你的工作或学习有所帮助，欢迎给作者送一些幼女过来。


