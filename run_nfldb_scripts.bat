echo off
title Run nfldb data collection scripts
:: See the title at the top
cd C:\Users\Alan\Documents\Github\nfldb_ml
echo ==================================================================
echo ******run RB script******
echo ==================================================================
python rb_stats.py
echo ==================================================================
echo ******run WR script******
echo ==================================================================
python wr_stats.py
echo ==================================================================
echo ******run QB script******
echo ==================================================================
python qb_stats.py
echo ==================================================================
echo ******run TE script******
echo ==================================================================
python te_stats.py