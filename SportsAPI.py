import requests,os,bs4,json,datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from flask import Flask
from flask import request,jsonify
import json
app=Flask(__name__)
posts={"cric-news":[]}
months = {
              1  :  "JANUARY",
              2  :  "FEBRUARY",
              3  :  "MARCH",
              4  :  "APRIL",
              5  :  "MAY",
              6  :  "JUNE", 
              7  :  "JULY",
              8  :  "AUGUST",
              9  :  "SEPTEMBER",
              10 :  "OCTOBER",
              11 :  "NOVEMBER",
              12 :  "DECEMBER"
}

class Barclay:

    def documentation(self):
        return """This page will contain documentation for Web SportsAPI <br>
        <br>
        The sportsAPI is hosted at http://cherry-shortcake-81993.herokuapp.com <br>
 <br>
The API at present contains data for Football and Cricket.<br>
<br>
More Sports will be added later so stay tuned :) <br>
<br>
To access Cricket data :- <br>
<br>
for cricket live scores : go to /cric/live/ <br>
<br>
for cricket news : go to /cric/news/ <br>
<br>
for cricket upcoming match list : go to /cric/matches/ <br>
<br>
for cricket player stats : go to /cric/player_stats/?player-name="PLAYER_NAME"  # In the double quotes player name will be provided <br>
                   <br>
<br>
To access Football data :- <br>
<br>
for football live scores : go to /foot/live/ <br>
<br>
for football latest match results : go to /foot/results/ <br>
<br>
for football news : go to /foot/news/ <br>
<br>
for football pointstable : go to /foot/pointstable/ <br>
<br>
for football player stats : go to /foot/stats/?player-name=PLAYER_NAME          # There will be no double quotes hii"""
        

    def get_news_headlines(self, get_club_news=False, type_return='string'):
        """
        Parameters
        ----------
        get_club_news : Bool, default to False
                        If true , returns news about clubs too.

        type_return : String, to specify the return type
                      Defaults to `string`
        Returns
        -------
        String : A collection of news headlines and links
        """
        url = "http://www.premierleague.com/en-gb.html"
        res = requests.get(url,stream=True)
        soup = bs4.BeautifulSoup(res.text,'lxml')
        all_updated = False
        news_headline = []
        news_list = soup.select('.newsfeaturetitle')
        for i in range(len(news_list)):
            news_headline.append(str(news_list[i].text))
        news_url = []
        urls = soup.select('.newsfeature a')
        for i in urls:
            news_url.append("http://www.premierleague.com/"+i.get('href'))
        if get_club_news is True:
            news_list = soup.select('.feed li a')
            for i in range(len(news_list)):
                    news_headline.append(str(news_list[i].text))
            urls = soup.select('.feed li a')
            for i in urls:
                    news_url.append(i.get('href'))
        return_dict = {}
        for i, name in enumerate(news_headline):
            return_dict[name] = news_url[i]

        #if type_return == 'dict':
        return_dict=json.dumps(return_dict)
        return str(return_dict)

    def next3Fixtures(self, type_return='string'):
        now = datetime.datetime.now()
        url = "http://www.premierleague.com/en-gb/matchday/league-table.html?season=2015-2016&month=" +\
                months[now.month] + "&timelineView=date&toDate=1451433599999&tableView=NEXT_3_FIXTURES"
                
        res = requests.get(url, stream=True)
        soup = bs4.BeautifulSoup(res.text,'lxml')
        team_names = soup(template = '.next3FixturesTable')
        for i in range(len(team_names)):
            team_names[i] = str(team_names[i].text)

        next_3_fixtures = soup.select('.club-row .col-fixture')
        for i in range(len(next_3_fixtures)):
            next_3_fixtures[i] = str(next_3_fixtures[i].text)

        return_dict = {}
        for i in range(len(team_names)):
            return_dict[team_names[i]] = next_3_fixtures[i]

        if type_return == 'dict':
            return_dict=json.dumps(return_dict)
            return return_dict

    def pointsTable(self, type_return='string'):
        url = 'http://www.premierleague.com/en-gb/matchday/league-table.html'

        res = requests.get(url, stream=True)
        soup = bs4.BeautifulSoup(res.text,'lxml')

        team_name = soup(template = '.leagueTable-Club')
        for i in range(len(team_name)):
            team_name[i] = str(team_name[i].text)

        matches_played = soup(template = '.leagueTable-P')
        for i in range(len(matches_played)):
            matches_played[i] = str(matches_played[i].text)

        matches_won = soup(template = '.leagueTable-W')
        for i in range(len(matches_won)):
            matches_won[i] = str(matches_won[i].text)

        matches_drew = soup(template = '.leagueTable-D')
        for i in range(len(matches_drew)):
            matches_drew[i] = str(matches_drew[i].text)

        matches_lost = soup(template = '.leagueTable-L')
        for i in range(len(matches_lost)):
            matches_lost[i] = str(matches_lost[i].text)

        goals_difference = soup(template = '.leagueTable-GD')
        for i in range(len(goals_difference)):
            goals_difference[i] = str(goals_difference[i].text)

        points = soup(template = '.leagueTable-Pts')
        for i in range(len(points)):
            points[i] = str(points[i].text)

        return_dict = {}
        for i in range (len(team_name)):
            return_dict[team_name[i]] = [matches_played[i], matches_won[i], matches_drew[i], matches_lost[i], goals_difference[i], points[i]]

        return_dict=json.dumps(return_dict)
        return return_dict

    def topScorers(self, type_return='string'):
        url = "http://www.premierleague.com/en-gb.html"

        res = requests.get(url, stream=True)
        soup = bs4.BeautifulSoup(res.text,'lxml')

        top_scorers = soup.select('.statsranking-topscorers .statsranking-table .statsranking-name a')
        for i in range(len(top_scorers)):
            top_scorers[i] = str(top_scorers[i].text)

        top_scorers_goals = []
        top_scorers_temp = soup.select('.statsranking-topscorers .statsranking-table tbody tr td')

        for i in range(2, len(top_scorers_temp), 3):
            top_scorers_goals.append(str(top_scorers_temp[i].text))

        return_dict = {}
        for i in range(len(top_scorers)):
            return_dict[top_scorers[i]] = top_scorers_goals[i]

        
        return str(return_dict).encode("utf-8")

    def Fixtures(self, return_type='string'):
        url = "http://www.premierleague.com/en-gb/matchday/matches.html?paramClubId=ALL&paramComp_8=true&view=.dateSeason"

        res = requests.get(url, stream=True)
        soup = bs4.BeautifulSoup(res.text,'lxml')
        fixtures_time = []
        fixtures_location = []
        fixtures_clubs = []
        fixture_table = soup.select('.contentTable')
        for tables in fixture_table:
            date = tables.select('th')
            date[0] = str(date[0].text)
            fixtures_t = tables.select('.time')
            for i in range(len(fixtures_t)):
                fixtures_time.append(str(fixtures_t[i].text)+', ' +date[0])

            fixtures_c = tables.select('.clubs a')
            for i in range(len(fixtures_c)):
                fixtures_clubs.append(str(fixtures_c[i].text))

            fixtures_l = tables.select('.location a')
            for i in range(len(fixtures_l)):
                fixtures_location.append(str(fixtures_l[i].text))

        return str(list(zip(fixtures_clubs, fixtures_time, fixtures_location)))

    def Results(self, type_return='string'):
        url = "http://www.premierleague.com/en-gb.html"

        res = requests.get(url, stream=True)
        soup = bs4.BeautifulSoup(res.text,'lxml')

        results_time = soup.select('.megamenu-date span')
        for i in range(len(results_time)):
            results_time[i] = str(results_time[i].text)

        results_time = results_time[0:20]
        results_time.reverse()

        results_clubs = soup.select('.megamenu-matchName span')
        for i in range(len(results_clubs)):
            results_clubs[i] = str(results_clubs[i].text)
        results_clubs = results_clubs[0:60]

        results_clubs_temp = []
        for i in range(20):
            j = i*3
            results_clubs_temp.append([results_clubs[j], results_clubs[j+1], results_clubs[j+2]])
        results_clubs = results_clubs_temp
        results_clubs.reverse()

        results_location = soup.select('.megamenu-venue')
        for i in range(len(results_location)):
            results_location[i] = str(results_location[i].text)
        results_location = results_location[0:20]
        results_location.reverse()
        if len(str(zip(results_time, results_clubs, results_location)))!=0:
          return str(zip(results_time, results_clubs, results_location))
        else :
            return "NO data found"

    def liveScore(self):
        self.url = 'http://www.premierleague.com/en-gb.html'
        self.res = requests.get(self.url, stream=True)
        self.soup = bs4.BeautifulSoup(self.res.text,'lxml')

        matches = self.soup.select('.LIVE  .MEGAMENU-MATCHnAME')
        live_matches = []
        for i in matches:
            temp = i.text.split()
            temp = ' '.join(temp)
            live_matches.append(temp)

        return str(live_matches)

    def playerStats(self):
        try:
            self.url = 'http://www.premierleague.com/en-gb/players/profile.html/'
            player_name=request.args.get("player-name")
            self.url += player_name
            self.res = requests.get(self.url, stream=True)
            self.soup = bs4.BeautifulSoup(self.res.text,'lxml')

            stats = self.soup.select('.left td')
            temp = []
            statsDict = {}
            for i in stats:
                temp.append(i.text)

            statsDict[temp[0]] = temp[1]
            statsDict[temp[8]] = temp[9]
            statsDict[temp[12]] = temp[13]
            statsDict[temp[16]] = temp[17]
            statsDict = json.dumps(statsDict)
            return str(statsDict)
        
        except:
            raise ValueError('Name not found, enter a valid name of player!')

class Cricket(object):
    def get_player_stats(self, type_return='string'):
        base_url="http://www.espncricinfo.com"
        playerName=request.args.get("player-name")
        url="http://www.espncricinfo.com/ci/content/player/search.html?search="
        url=url+playerName
        res=requests.get(url)
        res.raise_for_status()
        soup=bs4.BeautifulSoup(res.text,"lxml")
        playerStatLink=soup.select(".ColumnistSmry") 
        playerStatLink=playerStatLink[1]
        temp_url=playerStatLink.get('href')
        url=base_url+temp_url
        res=requests.get(url)
        soup=bs4.BeautifulSoup(res.text,"lxml")
        player_info=soup.select(".ciPlayerinformationtxt")
        player_stats={}   
        for item in player_info[0:len(player_info)]:
            b=item.find('b')
            if b.string=="Major teams":
                span=item.findAll('span')
                temp=""
                for it in span:
                    temp+=it.string+" "
            else:
                temp=item.find('span')
                temp=temp.string
            player_stats[b.string]=temp
        if type_return == 'dict':
            return player_stats
        else:
            player_stats = json.dumps(player_stats)
            return str(player_stats)

    def live_score(self, type_return='string'):

        response = requests.get('http://www.cricbuzz.com/live-scores')
        soup = bs4.BeautifulSoup(response.text,"lxml")
        team_mate = soup.findAll("div", {"class" : "cb-lv-main"})
        scores = []
        for i in team_mate:
            scores.append(i.text)
        if type_return == 'dict':
            return scores
        return str(scores)

    def list_matches(self, type_return='string'):
        response = requests.get('https://cricket.yahoo.com/matches/schedule')
        soup = bs4.BeautifulSoup(response.text,"lxml")
        head_list = soup.findAll("em", {"class": "ycric-table-heading"})
        invited_team_list = soup.findAll("div", {"class": "ycric-table-sub-heading"})
        no_list = soup.findAll("td", {"class": "sno"})
        tour_dates_list  = soup.findAll("span", {"class" : "matchDateTime"})
        match_list = soup.findAll("td", {"class": "smatch"})
        venue_list= soup.findAll("td", {"class": "svenue"})
        result_list = soup.findAll("td", {"class": "sresult"})
        heading = 0
        nos = []
        tour_date = []
        team_list = []
        venue = []
        result = []
        ans = []
        cnt = 0
        for i in match_list:
            if i.text != "Match":
                team_list.append(i.text)
        for i in no_list:
            if i.text !="#":
                nos.append(i.text)
        for i in venue_list:
            if i.text!="Venue":
                venue.append(i.text)
        for i in result_list:
            if i.text!="Result":
                result.append(i.text)
        cnt =len(nos)

        check = 0

        matches = {}
        for i in range(cnt):
            if nos[i]=="1":
                header = head_list[heading].text.lstrip()
                matches[header] = []
                heading = heading+1
            matches[header].append((team_list[i].lstrip(), tour_dates_list[i].text.lstrip(), venue[i].lstrip(), result[i].lstrip()))
        if type_return == 'dict':
            return matches
        matches = json.dumps(matches)
        return str(matches)

    def news(self, type_return='string'):
         
         base_url='http://www.cricbuzz.com/cricket-news/latest-news'
         res=requests.get(base_url)
         soup = bs4.BeautifulSoup(res.text,"html.parser")
         news = soup.select(".cb-nws-hdln a")
         news_dict={}
         url="www.cricbuzz.com"
         for all_news in news:
             if str(all_news.get("title"))!="More Photos" and str(all_news.get("title"))!="None":
                 news_dict[all_news.get("title")]=url+all_news.get("href")
         if type_return == 'dict':
            return news_dict
         news_dict = json.dumps(news_dict)
         return str(news_dict)
		
       

if __name__=='__main__':
    cricc =  Cricket()
    app.add_url_rule('/cric/news/',view_func=cricc.news)
    app.add_url_rule('/cric/matches/',view_func=cricc.list_matches)
    app.add_url_rule('/cric/live/',view_func=cricc.live_score)
    app.add_url_rule('/cric/player_stats/',view_func=cricc.get_player_stats)
    
    foot=Barclay()
    app.add_url_rule('/',view_func=foot.documentation)
    app.add_url_rule('/foot/news/',view_func=foot.get_news_headlines)
    app.add_url_rule('/foot/nxt3fixtures/',view_func=foot.next3Fixtures)
    app.add_url_rule('/foot/pointstable/',view_func=foot.pointsTable)
    app.add_url_rule('/foot/topscorers/',view_func=foot.topScorers)
    app.add_url_rule('/foot/results/',view_func=foot.Results)
    app.add_url_rule('/foot/live/',view_func=foot.liveScore)
    app.add_url_rule('/foot/stats/',view_func=foot.playerStats)
    #myvar = request.GET["myvar"]
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port,debug=True)
    """
	#app.add_url_rule('/cric/player_stats/',view_func=attr.player_stats)

	player_stats=attr.get_player_stats("Virender Sehwag")
	print (player_stats)
	print (attr.live_score())
	print (attr.list_matches())
	print (attr.news())
   """
