import matplotlib.pyplot as plt
import numpy as np

# 假设的内存带宽（单位：B/s）
memory_bandwidth = 1  # 假设为 1GB/s

# 定义一个函数来计算 Roofline 模型的 FLOPS
def roofline_model(arithmetic_intensity, max_flops):
    """
    计算在给定运算强度下的最大 FLOPS。
    运算强度定义为浮点运算次数 FLOP / 所需传输量 B。
    """
    # 根据运算强度计算 FLOPS
    potential_flops = memory_bandwidth * arithmetic_intensity
    flops = np.minimum(potential_flops, max_flops)  # 使用 np.minimum 来处理数组
    return flops

# 假设的最大 FLOPS，这里我们使用一个示例值
max_flops = 10  # 假设为 10**11 FLOPS = 10GFLOPS

# 创建一个数组来表示不同的运算强度
arithmetic_intensity = np.asarray([0, max_flops / memory_bandwidth, 5e1])

# 计算对应的 FLOPS
flops = roofline_model(arithmetic_intensity, max_flops)

# 绘制 Roofline 图
plt.figure(figsize=(6, 4))
plt.plot(arithmetic_intensity, flops, label='Roofline Model')
plt.xlabel('Arithmetic Intensity (FLOP per byte)')
plt.ylabel('FLOPS')
# plt.title('Roofline Model')
# plt.legend()
# plt.grid(True)
# plt.xscale('log')  # 使用对数刻度以便更好地展示低运算强度
# plt.yscale('log')  # 使用对数刻度以便更好地展示高 FLOPS 值
plt.xlim(0, 20)
plt.ylim(0, 15)

ax = plt.gca()
# ax.spines['bottom'].set_visible(False)
# ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 填充 compute-bound 区域（下方）
plt.fill_between(arithmetic_intensity, flops, color='gray', alpha=0.2)

# 填充 memory-bound 区域（上方）
plt.fill_between(arithmetic_intensity, flops, color='wheat', alpha=0.2, where=flops > 0)

# plt.rcParams['font.sans-serif'] = ['SimSun'] # 修改中文字體

plt.text(7.3, 2.2, "I", fontdict={'family': 'Times New Roman', 'weight': 'normal', 'size': 20})

plt.text(14.8, 4.5, "II", fontdict={'family': 'Times New Roman', 'weight': 'normal', 'size': 20})

#显示网格线
plt.grid(True)
#同时设置
plt.grid(color='lightgray',linewidth=0.5,alpha=0.8) 

# plt.show()
plt.tight_layout()

plt.savefig('roofline.pdf')