# petrarch2-zh

> source:
>
> petrarch2: https://github.com/openeventdata/petrarch2
>
> stanford-corenlp: https://github.com/Lynten/stanford-corenlp



## 1.配置

#### 下载StanfordCoreNLP及中文model

[链接🔗https://stanfordnlp.github.io/CoreNLP/download.html](https://stanfordnlp.github.io/CoreNLP/download.html)

需要下载两个文件，`CoreNLP 3.9.2`和`Chinese MODEL JAR 3.9.2`

- 完成下载后，将`stanford-chinese-corenlp-2018-10-05-models.jar`放到`stanford-corenlp-full-2018-10-05`文件夹的根目录下
- 如果corenlp不在别的项目中使用，可以直接将`stanford-corenlp-full-2018-10-05`放到`petrarch2-zh`文件夹根目录下

#### 安装python库

```
pip install stanfordcorenlp
```



## 2.使用

根据需要更改`main.py`中的变量

`input_path`  - 输入文件路径

`output_path` - 输出文件路径

`corenlp_path` - `stanford-corenlp-full-2018-10-05`文件夹路径

运行脚本(petrarch2不支持python3)

```
python2 main.py
```

(为了方便在IDE中调试，暂时在脚本中直接写"命令行参数")



## 3.可能的问题

#### Access Denied

> File "/usr/local/lib/python3.7/site-packages/stanfordcorenlp/corenlp.py", line 79, in \_\_init\__
>  if port\_candidate not in [conn.laddr[1] for conn in psutil.net_connections()]:
> File "/usr/local/lib/python3.7/site-packages/psutil/\_\_init\_\_.py", line 2248, in net_connections
>  return \_psplatform.net_connections(kind)
> File "/usr/local/lib/python3.7/site-packages/psutil/\_psosx.py", line 252, in net_connections
>  cons = Process(pid).connections(kind)
> File "/usr/local/lib/python3.7/site-packages/psutil/\_psosx.py", line 344, in wrapper
>  raise AccessDenied(self.pid, self._name)

是调用了`_psosx.py`中的某个方法导致的

```python
# _psosx.py

def net_connections(kind='inet'):
    """System-wide network connections."""
    # Note: on macOS this will fail with AccessDenied unless
    # the process is owned by root.
    ret = []
    for pid in pids():
        try:
            cons = Process(pid).connections(kind)
        except NoSuchProcess:
            continue
        else:
            if cons:
                for c in cons:
                    c = list(c) + [pid]
                    ret.append(_common.sconn(*c))
    return ret
```

需要以root权限执行：

```
sudo python main.py
```

或者还有一个解决方法：修改 corenlp.py 文件
把这段代码注释掉

```python
            # Check if the port is in use
            if self.port in [conn.laddr[1] for conn in psutil.net_connections()]:
                raise IOError('Port ' + str(self.port) + ' is already in use.')
```

变成

```python
            # Check if the port is in use
            # if self.port in [conn.laddr[1] for conn in psutil.net_connections()]:
            #    raise IOError('Port ' + str(self.port) + ' is already in use.')
```

**注意：修改后，启动 `StanfordCoreNLP Server` 一定要指定端口**