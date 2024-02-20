import traceback

import openpyxl


class Excel:
    @staticmethod
    def get_data(xl_path, sheet_name, row, col):
        try:
            wb = openpyxl.open(xl_path)
            sheet = wb[sheet_name]
            data = sheet.cell(row, col).value
            print('XL Data:', data)
        except:
            print('Err in reading XL data')
            data = None
            traceback.print_exc()
        return data
