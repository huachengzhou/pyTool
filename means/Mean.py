# 导入枚举类
from enum import Enum


# 继承枚举类
class Mean(Enum):
    FILE = 1
    OFFICE = 2
    FORMAT = 3



if __name__ == '__main__':

    print(Mean.FILE)  # Mean.FILE
    print(Mean.FILE.value)  # 1
    print(Mean.FILE.name)  # FILE