```shell
# 初始化conda
/data/dingli/lib/miniconda3/bin/conda init

# 取消默认启动
conda init --reverse

# 10 5下载进程 进程号
[1] 470221

# 查看显卡信息
nvidia-smi

# 后台运行加重定向输出（在所有命令后加上以下语句即可），其中&符号代表后台运行
 > ./file.log 2>&1 &

# 关闭远程连接后仍然保持运行，但是需要用ps -aux | grep "pip3"命令查找
nohup commands > ./log/train.log 2>&1 &

# 在python刷新输出缓存以得到实时重定向
sys.stdout.flush()

# 终端打印北京时间
(TZ=UTC-8 date +%Y-%m-%d" "%H:%M:%S)

(date; nohup python ./MKG-FENN-task2.py) > ./log/train.log 2>&1 &

# ; 用于分割不同命令
((TZ=UTC-8 date +%Y-%m-%d" "%H:%M:%S); nohup python ./task1_big.py; (TZ=UTC-8 date +%Y-%m-%d" "%H:%M:%S)) > ./log/trainTask1big_10_8.log 2>&1 &

# 查看进程
ps -ef
ps -aux | grep "pip3"  # 查找包含pip3字符串的进程

# 杀死进程
kill -9 processID

# 压缩和解压
zip -r dir.zip test_directory/
unzip dir.zip -d test_directory/

# 查看cpu和内存占用情况
top
```

