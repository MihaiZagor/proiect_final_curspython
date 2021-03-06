import requests
from bs4 import BeautifulSoup

URL = 'https://lpf.ro/liga-1'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
stage_table = soup.find(class_ = 'clasament_general white-shadow')
team_rows = stage_table.find_all(class_ = 'echipa_row')
print(team_rows)
teams = []
for team in team_rows:
    team_cell = team.find('a')
    team_name = team_cell.text.strip()
    teams.append(team_name)

print(teams)

