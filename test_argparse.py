import argparse

# 实例化
parse = argparse.ArgumentParser()

# 添加参数
parse.add_argument('--a', type=int, default=1, help='a_help')
parse.add_argument('--b', type=float, default=2.0, help='b_help')
parse.add_argument('--c', type=bool, default=False, help='c_help')

a = parse.parse_args()

b = parse.parse_known_args()

print(a)
print(b)