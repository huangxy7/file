import xlrd
import xlwt


#去读xlsx表内容
def re_xlsx():
    book = xlrd.open_workbook("1.xlsx")
    #获取第一个表单
    sh = book.sheet_by_index(0)
    for s in book.sheets():
        for r in range(s.nrows):
            print(s.row(r))
#re_xlsx()

#新增一个表写入内容
def wr_xlsx():
    #创建xls文件对象
    wb = xlwt.Workbook()
    #新增一个表单
    sh = wb.add_sheet("test_sheet")
    #按位置添加数据
    sh.write(0,0,5272)
    sh.write(1,0,8888)
    sh.write(2,0,"hello")
    sh.write(2,1,"mylove")
    #保存文件
    wb.save("test.xls")
#wr_xlsx()


