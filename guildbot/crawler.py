from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

url = "https://plancke.io/hypixel/guild/name/ULTRATRYHARDS"

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

def getmemberdetails():
  guildrole = soup.find_all()
  guildrolelist2 = []
  guildrolelist = []

  uuid = []
  name = []
  role = []
  first_join = []
  last_join = []

  for role in guildrole:
    if role.name == 'td':
      guildrolelist2.append(role.text)

  guildrolelist = [guildrolelist2[n:n+6] for n in range(0, len(guildrolelist2), 6)]

  for i in guildrolelist:
    name.append(i[2])

  for i in guildrolelist:
    uuid.append(i[0])

  for i in guildrolelist:
    role.append(i[3])

  for i in guildrolelist:
    first_join.append(i[4])

  for i in guildrolelist:
    last_join.append(i[5])
  
  guildmemberdict = {
    'uuid' : uuid,
    'name' : name,
    'role' : role,
    'First Join' : first_join,
    'Last Join' : last_join
    }

  return guildmemberdict

def getguildinfo():
  guildinfo = soup.find('div', class_='card-box')
  guildinfolist2 = []
  guildinfolist = []

  guildinfo = str(guildinfo)

  guildinfo = guildinfo.split('</b>')

  for i in guildinfo:
    guildinfolist2.append(i.replace('<br/>', ''))

  for i in guildinfolist2:
    guildinfolist.append(i.split('<b>'))

  guildinfolist = sum(guildinfolist, [])

  tag = guildinfolist[6].replace(guildinfolist[6][0:30], '')

  tag = [str(tag).replace('</span>', '')]

  guildinfolist = guildinfolist[3:6] + tag + guildinfolist[7:13] + guildinfolist[22:24]
  #make a list with only the data we want

  return guildinfolist
  
class Crawler:
  def  infoToCsv():
    members_details = getmemberdetails()
    info = getguildinfo()

    guildinfo = {'Guild Info': info}

    raw_data = guildinfo.copy()
    raw_data.update(members_details)

    df = pd.DataFrame.from_dict(raw_data, orient='index')
    df = df.transpose()

    df.to_csv('guildlist.csv')