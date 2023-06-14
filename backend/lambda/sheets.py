import gspread

def get_sheet(credentials, key):
    creds = gspread.service_account_from_dict(credentials)
    spreadsheet = creds.open_by_key(key)
    return spreadsheet




