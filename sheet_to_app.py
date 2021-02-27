import gspread
from oauth2client.service_account import ServiceAccountCredentials


def NPK_DATA():
    scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("NPK_Credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("NPK_Soil_Data").sheet1

    list1 = [sheet.col_values(1),sheet.col_values(2),sheet.col_values(3),sheet.col_values(4),sheet.col_values(5),sheet.col_values(6)]

    return list1

#NPK_DATA()
#print(NPK_DATA()[0])