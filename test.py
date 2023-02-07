import requests
import json
import gspread
import pandas as pd
import time

json_key_path = r'C:\Users\user\Downloads\SB\GSPREAD\marine-clarity-374714-9033ac32cec8.json'
gc = gspread.service_account(json_key_path)

spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1yIWY3grNALTPae_KaAyfmGD5Ys5MMENj5hp4tCmdz7A/edit#gid=1384360909'

# 스프레스시트 문서 가져오기 
doc = gc.open_by_url(spreadsheet_url)

# 시트 선택하기



#-------------

headers = {
    'accept': 'application/json',
    'authorization': 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyIsImtpZCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyJ9.eyJpc3MiOiJodHRwczovL2x1ZHkuZ2FtZS5vbnN0b3ZlLmNvbSIsImF1ZCI6Imh0dHBzOi8vbHVkeS5nYW1lLm9uc3RvdmUuY29tL3Jlc291cmNlcyIsImNsaWVudF9pZCI6IjEwMDAwMDAwMDAwODc4NTYifQ.Kz1Q31XCxpow-7vQUhjx8sejfVuQHi0T7BLfVoIXd4LErYMYJZ82oc9PX3Ls19rVxgvnNrwnpu2a2Ctg3vX8qO0214NgAh1Ab8M2hPPEksai7LY2enjhBGu7nvs8Ic9eq43p4DiGlpHQ68zZBbTo1WFbumayIrWkVAD-m7AHbkuguM0pMuXv8qL7ar6ZR-vVUsOetOuAannv6OpFhss3db1n4PuJM6S1TPyo2-Uo6T2FTp5Ue9C8TmIFnj97ZESorEU5KttbZ9qkL8yYnsK1A6glbYQksGMkCS0zQCp87BRQPccKAw41WlybHWcdjU3Zz3iDtMmQ5zv0GI_s0tzEmQ',
    'Content-Type': 'application/json',
}

dic = {'50000':'재련재료','60000':'배틀','90000':'생활'}
for key, value in dic.items():
     for t in range(1,20) :
          json_data_upload = {
          'Sort': '',
          'CategoryCode': key,
          'CharacterClass': '',
          'ItemTier': 0,
          'ItemGrade': '',
          'ItemName': '' ,
          'PageNo': t,
          'SortCondition': 'ASC',
          }
          wks = doc.worksheet(value)
          print(key,value,t)
          try:
               response =requests.post('https://developer-lostark.game.onstove.com/markets/items', headers=headers, json=json_data_upload)
               content = response.json()
               item = json.dumps(content["Items"]).replace("[","").replace("]","").replace("}, {","}${")
               if '$' in item:
                    for i in range(len(item.split('$'))):
                         json.loads(item.split('$')[i])
                         wks.update_acell('a'+str(i+1+(t-1)*10),json.loads(item.split('$')[i])["Name"])
                         wks.update_acell('b'+str(i+1+(t-1)*10),json.loads(item.split('$')[i])["CurrentMinPrice"])
                         time.sleep(1.5)
                         
               else:
                    single_item = json.loads(item)
                    single_search = doc.worksheet('검색')
                    single_search.update_acell('a1',single_item["Name"])
                    single_search.update_acell('b1',single_item["RecentPrice"])
          except Exception as e :
               print(e)
                    
          

     







# print(oreha_json["RecentPrice"]) : 상급 오레하 최근가격
# print(upper_oreha_json["RecentPrice"]) : 최상급 오레하 최근가격

#업데이트 = wks.update_acell('a2',oreha_json["RecentPrice"])

# dump_json = json.dumps(json_data)
# print("dump_json = json.dumps(json_data) is ",  type(dump_json))
# print("json.loads(dump_json) is ", type(json.loads(dump_json)))

df = pd.read_excel(r'C:\Users\user\Downloads\SB\GSPREAD\Market_test.xlsx', sheet_name='시트1',header=0)

# print(df.to_dict())

