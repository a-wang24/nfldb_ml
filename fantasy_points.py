# -*- coding: utf-8 -*-
"""
Created on Sat May 13 18:51:12 2017

@author: Alan
function definitions for fantasy points
"""
def calc_fp(pp, ppr):
    total_points = (float(pp.receiving_yds)/10 + pp.receiving_tds*6 + pp.receiving_rec*ppr +
                    float(pp.rushing_yds)/10 + pp.rushing_tds*6 +
                    float(pp.passing_yds/25 + pp.passing_tds*4) -
                    pp.fumbles_tot*2 - pp.passing_int*2)
    return total_points
    

