# -*- coding: utf-8 -*-
"""
Created on Sat May 13 22:04:56 2017

@author: Alan
Write RB data to .csv
"""
import nfldb
import csv
import individual_stats as indst

years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
position = 'RB'
limit = 120
sort_by = ['rushing_yds', 'rushing_tds', 'rushing_att']
ppr_rules = [0, 0.25, 0.5, 1]

for year in years:
    for sort in sort_by:
        for ppr in ppr_rules:
            data = []
            db = nfldb.connect()
            q = nfldb.Query(db)
            with open('output/rb/top'+str(limit)+'_'+str(position)+'_'+str(year)+
                      '_'+str(ppr)+'ppr_by_'+
                      str(sort)+'.csv', 'wb') as csvfile:
                c = csv.writer(csvfile)
                c.writerow(['Player', 'Rec Yds', 'Rec Tar', 'Rec Tds', 'Rec YAC', 
                            'Rush Yds', 'Rush Att', 'Rush Tds', 'Pass Yds', 'Pass Tds',
                            'Pass Att', 'Fumbles', 'Interceptions',
                            'Total Fantasy Pts', 'Team'])
                q.game(season_year = year, season_type = 'Regular')
                q.player(position = position)
                # pp is play_player class 
                # sort is default descending order
                for pp in q.sort(sort).limit(limit).as_aggregate():
                    tfp = indst.calc_fp(pp, ppr)
                    data.append([pp.player, pp.receiving_yds, pp.receiving_tar, pp.receiving_tds,
                                 pp.receiving_yac_yds, pp.rushing_yds, pp.rushing_att, pp.rushing_tds,
                                 pp.passing_yds, pp. passing_tds, pp.passing_att, 
                                 pp.fumbles_tot, pp.passing_int, tfp])
    
                #q.sort(sort).limit(limit)
                for entry in data:
                    pp_list = indst.player_team(year, position, sort, limit, entry[0].full_name)
                    if len(pp_list) == 0:
                        team = ''
                    else:
                        team = pp_list[0].team
                    entry.append(team)
                    c.writerow(entry)                        
                    
                csvfile.close()
