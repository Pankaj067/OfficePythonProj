from win32com import client

xlApp = client.Dispatch("Excel.Application")
books = xlApp.Workbooks.Open('C:/Users/pankaj.kumar1/Desktop/After_US/2018/02Feb-2018/02Feb2018/Python/ExcelFiles/imf-dm-export-20170926 (1).xls')
ws = books.Worksheets[0]
#ws.Visible = 1
ws.ExportAsFixedFormat(0, 'CC:/Users/pankaj.kumar1/Desktop/After_US/2018/02Feb-2018/02Feb2018/Python/new2.pdf')
