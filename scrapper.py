import bs4 as bs
from selenium import webdriver
import mysql.connector
import requests
import os


# get the webdriver so you can visit dynamic js
driver = webdriver.Chrome()

driver.get("https://www.espn.com/nba/team/stats/_/name/gs/golden-state-warriors")

res = driver.execute_script("return document.documentElement.outerHTML")

driver.quit()
######################################################################################
################################## leaders ###########################################
######################################################################################


# get the stats of the leaders
soup = bs.BeautifulSoup(res, 'lxml')

box = soup.find("section", {"class": "StatLeaders flex"})

leaders = box.find_all("h2", {"class": "clr-gray-03 h8 mb2"})

leaders = [leader.text for leader in leaders]

names = box.find_all("h3", {"class": "di n8"})

names = [name.text for name in names]

names = [names[i][:len(names[i]) - 2] for i in range(len(names))]

values = box.find_all("div", {"class": "clr-gray-01 pr3 hs2"})

values = [value.text for value in values]

leader_stats = zip(leaders, names, values)
leader_stats = [(leader, name, value) for leader, name, value in leader_stats]
print(leader_stats)

######################################################################################
################################## all players #######################################
######################################################################################
sec = soup.find_all("section", {
    "class": "Table2__responsiveTable Table2__table-outer-wrap Table2--hasFixed-left mt5 remove_capitalize"})
sec = sec[0]   # gets the first section
tb = sec.find_all("tbody")
ld = tb[0]
table_names = ld.find_all("a")
player_names = []
for name in table_names:
    if ' ' in name.text:
        player_names.append(name.text)
ps = tb[2]
stats_raw = ps.find_all("tr", {"class": "Table2__tr Table2__tr--sm Table2__even"})
stats = []
k = 0
for row in stats_raw:
    temp = [player_names[k]]
    for stat in row:
        temp.append(stat.text)
    k += 1 if k < 16 else 0
    stats.append(tuple(temp))
stats = stats[:len(stats) - 1]
print(len(stats))
print(stats)
args = "(" + ("".join(["%s," for i in range(15)])) + ")"

args = args[0:len(args) - 2] + args[len(args) - 1]
sql = "INSERT INTO player_stats (NAME, GP, GS, MIN, PTS, OFR, DR, REB, AST, \
STL, BLK, TNO, PF, AST_TNO, PER) VALUES {}".format(args)

######################################################################################
################################## shooting stats ####################################
######################################################################################
sec = soup.find_all("section", {
    "class": "Table2__responsiveTable Table2__table-outer-wrap Table2--hasFixed-left mt5 remove_capitalize"})
ss_sec = sec[1]

ss_body = ss_sec.find_all("tbody", {"class": "Table2__tbody"})

rows = ss_body[1].find_all("tr", {"class" : "Table2__tr"})



ss = []
k = 0
for row in rows:
    temp = [player_names[k]]
    for stat in row:
        temp.append(stat.text)
    if k < len(player_names) - 1:
        k += 1
    ss.append(tuple(temp))
ss = ss[:len(ss)-1]
'''
name VARCHAR(50),
    FGM FLOAT,
    FGA FLOAT,
    FG FLOAT,
    _3PM FLOAT,
    _3PA FLOAT,
    _3PP FLOAT,
    FTM FLOAT,
    FTA FLOAT,
    FTP FLOAT,
	_2PM FLOAT,
    _2PA FLOAT,
    _2PP FLOAT,
    SC_EFF FLOAT,
    SH_EFF FLOAT
'''
sql_ss = "INSERT INTO shooting_stats (name, FGM, FGA, FG, _3PM, _3PA, _3PP,"\
         "FTM, FTA, FTP, _2PM, _2PA, _2PP, SC_EFF, SH_EFF) VALUES {}".format(args)
# connect to database


mydb = mysql.connector.connect(
    user="root",
    password="Garrysmod1^3",
    host="localhost",
    database="gswdb",
    auth_plugin="mysql_native_password"
)

#mycursor = mydb.cursor()


#mycursor.executemany(sql_ss, ss)
#mydb.commit()

# load the leaders into the database

# mycursor.execute("CREATE DATABASE gswdb")

# mycursor.executemany("INSERT INTO leaders (leader_in, name, value) VALUES (%s, %s, %s)",leader_stats)

# mycursor.executemany(sql,stats)

# mydb.commit()
