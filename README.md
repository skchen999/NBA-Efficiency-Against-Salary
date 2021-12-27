# NBA-Efficiency-Against-Salary

W200 (Spring 2021) Final Project with Kelly Wen, Chi Ma, and Reece Koe


Like other professional sports, analytics are taking shape on the professional basketball court. The league has committed to data driven decisions in a big way. Almost every team now has an NBA analytics department in the front office. Using data analytics to pick players has become a trend in today’s NBA trading market. The purpose of this report is to analyze the NBA players’ efficiencies against their salaries and help the intended audience (team managers and coaches) to determine how the team should go forward with their signings.

## Cleaning up the Data
run `python process_raw_data_total.py` to clean up the raw data
in `NBA_Player_Advanced_20-21_raw.csv` and `NBA_Player_Stats_20-21_raw.csv`

from
```
8	Jarrett Allen	TOT	C	9.9	1.7	0.5	1.7	13.1	1.5	1.6	13.1
9	Jarrett Allen	BRK	C	10.4	1.7	0.6	1.6	11.2	1.8	1.8	11.2
10      Jarrett Allen	CLE	C	9.7	1.7	0.4	1.7	13.8	1.3	1.5	13.8
```
to
```
8	Jarrett Allen	CLE	C	9.9	1.7	0.5	1.7	13.1	1.5	1.6	13.1
```
and new data will be saved in `NBA_Player_Advanced_20-21.csv` and `NBA_Player_Stats_20-21.csv`
