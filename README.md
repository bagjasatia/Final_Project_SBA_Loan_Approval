# Final_Project_SBA_Loan_Approval

by: Bagja Satiaraharja

Dataset: SBAnational.csv [gdrive](https://drive.google.com/file/d/10cSCOrt7y2XY05J7AeX5FmIbLa3wLtQV/view?usp=sharing)

*The dataset is separate from the repository because it exceeds the github file size limit.


Source : [kaggle](https://www.kaggle.com/mirbektoktogaraev/should-this-loan-be-approved-or-denied)



PROJECT DESCRIPTION
---

The dataset is from the U.S. Small Business Administration (SBA)

The U.S. SBA was founded in 1953 on the principle of promoting and assisting small enterprises in the U.S. credit market (SBA Overview and History, US Small Business Administration (2015)). Small businesses have been a primary source of job creation in the United States; therefore, fostering small business formation and growth has social benefits by creating job opportunities and reducing unemployment. There have been many success stories of start-ups receiving SBA loan guarantees such as FedEx and Apple Computer. However, there have also been stories of small businesses and/or start-ups that have defaulted on their SBA-guaranteed loans.

In this final project, I will build a Flask-based web app that can recommend whether the loan is approved or not based on the given term and loan condition.

PROJECT GOALS
---

The goal of the project is to reduce the risk of charge off credit loans for Small Business Administration institutions by making machine learning-based applications to determine the loan request based on historical data. 

APPS
---
HOME PAGE
![](https://github.com/x-conx/Purwadhika_Projct_Finale/blob/master/presentation%20pic/home.png)

PREDICTION PAGE 
![](https://github.com/x-conx/Purwadhika_Projct_Finale/blob/master/presentation%20pic/input.png)

The application user can input data as described below:
- `How many bank account?` : number of bank account that customer cuurently holding
- `Household size`         : indication of approximate customers' current house size judgement from scale 1 to 6, 1 for very small and 6 for very large
- `Owned Current Home`     : if customer currently stay at personal home or not
- `Credit Rating`          : the rating that given by bank system (rating of an ability in term of financial performance)
- `Average Balance`        : the average amount of moneny that present in the customer's bank account fot the last 12 months or last financial year
- `Q1 Balance`             : first quarter balance from last financial year
- `Q2 Balance`             : second quarter balance from last financial year
- `Q3 Balance`             : third quarter balance from last financial year
- `Q4 Balance`             : fourth quarter balance from last financial year
- `Customer Reward`        : the current reward that applied to customer
- `Mailer Type`            : how customer will receive the current credit card advertising
- `Customer Income`        : an approximation of customer's level of income in low, medium, and high
- `Card Overdraw Protection`: the current status of cutomer's credit card, either their card can be used over the limit or not
- `Own Number CC`          : most of the customer already have credit card before they receive or decided to create a new one
- `Home(s) Owned`          : number of home(s) that under customer's name

PREDICTION RESULT
---
Customer will agree to create new credit card
![](https://github.com/x-conx/Purwadhika_Projct_Finale/blob/master/presentation%20pic/agree.png)
Customer will not create a new credit card
![](https://github.com/x-conx/Purwadhika_Projct_Finale/blob/master/presentation%20pic/decline.png)

VISUALISATION PAGE
---
![](https://github.com/x-conx/Purwadhika_Projct_Finale/blob/master/presentation%20pic/vis.png)

ABOUT
---
![](https://github.com/x-conx/Purwadhika_Projct_Finale/blob/master/presentation%20pic/about.png)
