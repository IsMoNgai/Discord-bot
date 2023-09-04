import pandas as pd
from crawler import Crawler

Crawler.infoToCsv()

df = pd.read_csv('guildlist.csv')

class string:
  def guildmemberlist():
    GM = sum(df.loc[df['role'] == 'Guild Master', ['name']].values.tolist(), [])
    Founder = sum(df.loc[df['role'] == 'Guild Founder', ['name']].values.tolist(), [])
    CM = sum(df.loc[df['role'] == 'Cute Master', ['name']].values.tolist(), [])
    SD = sum(df.loc[df['role'] == 'Staff', ['name']].values.tolist(), [])
    UC = sum(df.loc[df['role'] == 'Ultra Crystal', ['name']].values.tolist(), [])
    UM = sum(df.loc[df['role'] == 'Ultratrthards M', ['name']].values.tolist(), [])

    lengGM = len(GM)
    lengFounder = len(Founder)
    lengCM = len(CM)
    lengSD = len(SD)
    lengUC = len(UC)
    lengUM = len(UM)

    Founder = ", ".join(x for x in Founder)
    CM = ", ".join(x for x in CM)
    SD = ", ".join(x for x in SD)
    UC = ", ".join(x for x in UC)
    UM = ", ".join(x for x in UM)

    string = '**Guild Master >> ' + str(lengGM) + "**" + '```\n'  + GM[0] + '```\n' + ' ' + '\n' + '**Guild Founder >> ' + str(lengFounder) + "**" + '```\n'  + Founder + '```\n' + ' ' + '\n' + '**Cute Master >>  ' + str(lengCM) + "**" + '```\n'  + CM + '```\n' + ' ' + '\n' + '**Staff >> ' + str(lengSD)+ "**" + '```\n'  + SD + '```\n' + ' ' + '\n' + '**Ultra Crystal >> ' + str(lengUC) + "**" + '```\n'  + UC + '```\n' + ' ' + '\n' + '**Ultratrthards M >> ' + str(lengUM) + "**" + '```\n'  + UM + '```\n'

    return string

  def getguildinfo():
    GuildName = df['Guild Info'].iloc[1]
    Tag = df['Guild Info'].iloc[3]
    Created = df['Guild Info'].iloc[5]
    Members = df['Guild Info'].iloc[7]
    Level = df['Guild Info'].iloc[9]
    OnlinePlayer = df['Guild Info'].iloc[11]

    InfoList = [GuildName, Tag, Created, Members, Level, OnlinePlayer]

    return InfoList
    
