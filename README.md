# Election_Analysis
## Overview of Election Audit:
	The purpose of this audit is to analyze congressional election results by candidate and the overall turnout of voters in three counties in Colorado: Arapahoe, Jefferson and Denver. Using the raw election data provided, we will: 
1.	Calculate the total number of votes
2.	Get the list of candidates who received votes
3.	Calculate the number of votes cast for each candidate
4.	Compute the percentage of votes the candidates received and determine the winner
5.	Analyze the turnout for each county by calculating what percentage of votes came from each county.
### Resources:
1.	Data Source: election_results.csv
2.	Software: Python 3.7.6, Visual Studio Code
#### Election-Audit Results: 
-	The total number of votes is 369,711.
-	The breakdown of total votes by county in the precinct is as follows
    	Jefferson: 10.5% which is equal to 38,855 votes
    	Denver: 82.8% or 272, 892 votes
    	Arapahoe: 6.7% or 24,801 votes
-	The largest vote (~83%) came from Denver County.
-	There three candidates and their respective votes
    	Charles Casper Stockham: 23.0% (85,213 votes)
    	Diana DeGette: 73.8% (272,892 votes)
    	Raymon Anthony Doane: 3.1% (11,606 votes)
-	The winner of the congressional election is Diana DeGette with 272,892 votes which was a little under 74% of the total vote. 
##### Election-Audit Summary: 
	This script can be used to analyze other elections with varying number of candidates and counties. Generally, if the code would remain more or less that same for changes in total votes or number of candidates as it would loop through any given number of votes. This code could be used to analyze the demographics of the residents of the counties. A breakdown of bipartisanship, socio-economic, gender and educational level could be studied to help candidates address different demographics. The code would then need to be tweaked to include these new columns. A business proposal for the election committee would encompass an investigation of why counties have such a low voter-turnout. Another proposal would be to suggest factor in the total number of residents in each county and compare it to the overall turnout to assess if there are underlying causes of low turnout. 
