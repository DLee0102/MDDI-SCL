# 每个0.5秒打印一个数字
import time
import sys
for i in range(10):
    print(i)
    sys.stdout.flush()
    time.sleep(1)

