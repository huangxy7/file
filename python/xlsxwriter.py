import xlsxwriter

# 创建一个新的 Excel 文件，并添加一个工作表
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

# 设置第一列(A) 单元格宽度为 20
worksheet.set_column('A:A', 20)

# 定义一个加粗的格式对象
bold = workbook.add_format({'bold': True})

# 在 A1 单元格处写入字符串 'Hello'
worksheet.write('A1', 'Hello')

# 在 A2 单元格处写入中文字符串，并加粗字体
worksheet.write('A2', '千锋教育', bold)

# 利用 行和列的索引号方式，写入数字，索引号是从 0 开始的
worksheet.write(2, 0, 100)  # 3 行 1列
worksheet.write(3, 0, 35.8)

# 计算 A3 到 A4 的结果
worksheet.write(4, 0, '=SUM(A3:A4)')

# 在 B5 单元格处插入一个图片
worksheet.insert_image('B5', 'logo.png')

# 关闭 Excel 文件
workbook.close()