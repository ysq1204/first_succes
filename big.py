'''
1.输入刀数N
2.第1刀2块
3.累加，第n刀增加n块
4.输出总块数
'''

slice=1         # 片数
N=int(input())  # 输入需要切的刀数
i=1
for i in range(N):
    i+=1
    slice=slice+i
print(slice)










