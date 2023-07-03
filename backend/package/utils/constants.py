import os
from storage import get_sheet, get_spreadsheet

CREDENTIALS = os.environ.get("CREDENTIALS")
SHEET_KEY = os.environ.get("SHEET_KEY")
SHEET_INDEX = 1

SPREADSHEET = get_spreadsheet(CREDENTIALS, SHEET_KEY)
SHEET = get_sheet(SPREADSHEET, SHEET_INDEX)

COL_NAME = 1
COL_SETS = 2
COL_WINS = 3
COL_LOSS = 4
COL_SCORES = 5
