import gspread_asyncio
from google.oauth2.service_account import Credentials
from loader import SHEET_LINK

link = SHEET_LINK
def get_creds():
    creds = Credentials.from_service_account_file("key.json")
    scoped = creds.with_scopes([
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ])
    return scoped


agcm = gspread_asyncio.AsyncioGspreadClientManager(get_creds)
async def get_sheet(agcm=agcm):
    agc = await agcm.authorize()
    ss = await agc.open_by_url(link)
    zero_ws = await ss.get_worksheet(0)
    return zero_ws

async def append_user(id: str, username: str, code):
        sheet = await get_sheet()
        cell = await sheet.find(str(id))
        if cell is None:
            await sheet.append_row([id, username, code])
        else:
            await sheet.update_cell(cell.row, 5, '1')
            await sheet.update_cell(cell.row, 3, code)

async def set_team_name(id: str, name: str):
        sheet = await get_sheet()
        cell = await sheet.find(str(id))
        if cell is None:
            print(f'not found {id}')
            return
        else:
            await sheet.update_cell(cell.row, 4, name)
            

async def implement_score(id, level, amount):
    sheet = await get_sheet()
    cell = await sheet.find(str(id))
    if cell is None:
        return
    row_number = cell.row
    cell = await sheet.cell(row_number, level + 5)
    if cell.value:
        await sheet.update_cell(row_number, level + 5, amount + int(cell.value))
    else:
        await sheet.update_cell(row_number, level + 5, amount)
         

async def set_current_level(id, level):
    sheet = await get_sheet()
    cell = await sheet.find(str(id))
    if cell is None:
        return
    row_number = cell.row
    await sheet.update_cell(row_number, 5, level)
    if int(level) in [1, 2, 5]:
         await sheet.update_cell(row_number, 5 + level, 0)
         
