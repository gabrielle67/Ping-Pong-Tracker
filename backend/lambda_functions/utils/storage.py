import gspread


def get_spreadsheet(credentials, key):
    creds = gspread.service_account_from_dict(credentials)
    return creds.open_by_key(key)


def get_sheet(spreadsheet, index):
    return spreadsheet.get_worksheet(index)


def get_column(sheet, index):
    return sheet.col_values(index)


def get_row(sheet, index):
    return sheet.row_values(index)


def get_full_sheet(sheet):
    return sheet.get_all_records()


def add_row(sheet, body):
    sheet.append_row(body)


def remove_row(sheet, index):
    sheet.delete_row(index)


def find_row(sheet, search):
    cell = sheet.find(search)
    return cell.row if cell is not None else None


def set_cell(sheet, row, col, body):
    sheet.update_cell(row, col, body)
