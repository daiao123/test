# -*- coding: utf-8 -*-

from xlrd import open_workbook
from xlutils.copy import copy
from xlwt.Workbook import Workbook


class ExcelHelper():
    
    def __init__(self):
        self.wb = ''
        self.sheet = ''
        self.content = []
    
    def get_sheet(self):
        wb = open_workbook(self.wb) 
        sheet = wb.sheet_by_name(self.sheet)
        return sheet
        
    def read_by_row(self, start_row, start_col, end_col=None):
        row_values = self.get_sheet().row_values(start_row, start_col, end_col)
        return row_values  
          
    def read_by_col(self, start_col, start_row, end_row=None):
        col_values = self.get_sheet().col_values(start_col, start_row, end_row)
        return col_values
    
    def read_by_cell(self, row_number, col_number): 
        cell_value = self.get_sheet().cell_value(row_number, col_number)
        return cell_value

    def read_all(self, start_row, start_col):
        total = []
        for i in range(start_row, self.get_sheet().nrows):
            total.append(self.get_sheet().row_values(i, start_col))
        print(total)

    def create_and_write(self, sheet_name, types, row, col, text, savepath):
        wb = Workbook('utf-8')
        sheet = wb.add_sheet(sheet_name)
        if types == 'one':
            sheet.write(row, col, text)
        elif types == 'row':
            for i in range(len(self.content)):
                sheet.write(row, col + i, self.content[i])
        elif types == 'list':
            for j in range(len(self.content)):
                for k in range(len(self.content[j])):
                    sheet.write(5 + j, 7 + k, self.content[j][k])   
        else:
            raise print('对不起,只能输入one,row,list,否则无法写入任何数据')  
        wb.save(savepath)
        return self.content
    
    def copy_and_write(self, sheet_index, start, end, col_number, text):
        old_xls = open_workbook(self.wb, formatting_info=True)
        new_xls = copy(old_xls)
        new_sheet = new_xls.get_sheet(sheet_index)
        for i in range(start, end):
            new_sheet.write(i, col_number, text)
        new_xls.save(self.wb)

# eh = ExcelHelper()
# eh.wb = r'e:\mendao.xls'
# eh.sheet = '员工表'
# eh.read_by_row(10,4)
# eh.read_by_col(5,7,10)
# eh.read_by_cell(8,6)
# eh.read_all(15,10)
# eh.create_and_write(eh.sheet,1,1,'cc',eh.wb)
# eh.content = [11, 222, 33, 4, 5, 6, 6, 7]
# eh.content=[[10,'测试部'],[20,'研发部'],[30,'运营部']]
# eh.create_and_write(eh.sheet, 'list', 4, 5, eh.content, eh.wb)
# eh.copy_and_write(1, 30, 40, 5, 'baobao')
