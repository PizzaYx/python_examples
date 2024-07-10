# excel 自动化
# pip install pandas pip install openpyxl
import pandas as pd

# 读入文件
data = pd.read_excel('movie.xlsx')
data['year'] = data['type'].apply(lambda x: x.split('/')[0].strip())
data['nation'] = data['type'].apply(lambda x: x.split('/')[1].strip())
data['t'] = data['type'].apply(lambda x: x.split('/')[2].strip())

write_data = pd.ExcelWriter('temp.xlsx')
# data.to_excel(write_data, sheet_name='原始数据')
# write_data.close()

# print(data[data['nation'] == '美国'] )
# print(data['year'].unique())
# for i in data['year'].unique():
#     data[data['year'] == i].to_excel(write_data, sheet_name=i)

# 按类型分类
#print(data[data['t'].str.contains('科幻')])
# set 去重
t_list = set(z.strip() for i in data['t'] for z in i.split(','))
for i in t_list:
    data[data['t'].str.contains(i)].to_excel(write_data, sheet_name=i)

write_data.close()

# write_data.close()  # 关闭文件
