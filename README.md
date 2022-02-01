# BaseRedisBlast
基于Redis的Python爆破工具, 可以用于爆破任何想爆破的东西啦.

### 为什么要做这个？
python原本的多线程，如果要传递参数, 需要把参数先全部加载进来，如果数据量过大的话，就会导致内存不足，所以使用redis来存储参数，自己只需要专注于写业务逻辑就可以了。

### 多个参数怎么办？
很简单，如果你需要这个项目那证明你也有编写代码的实力，找个符号作为多个参数的分隔符自己处理就好了。

### 编写工具
来自优秀的Pycharm。