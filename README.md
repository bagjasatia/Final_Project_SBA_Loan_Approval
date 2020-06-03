# Final_Project_SBA_Loan_Approval

by: Bagja Satiaraharja

Dataset: SBAnational.csv [gdrive](https://drive.google.com/file/d/10cSCOrt7y2XY05J7AeX5FmIbLa3wLtQV/view?usp=sharing)

*The dataset is separate from the repository because it exceeds github file size limit.


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

HOMEPAGE
---
Home interface:
![](https://github.com/bagjasatia/Final_Project_SBA_Loan_Approval/blob/master/Interface/home-interface.png)

About interface:
![](https://github.com/bagjasatia/Final_Project_SBA_Loan_Approval/blob/master/Interface/about-interface.png)

PREDICTION PAGE 
---
![](https://github.com/bagjasatia/Final_Project_SBA_Loan_Approval/blob/master/Interface/predict-interface.png)

The application user can input data as described below:
- `NewExist`               : Business Condition when the loan is set.
- `RevLineCr`              : Revolving line of credit which means that if the loan has been paid, the borrower can be able to immediately borrow again.
- `LowDoc            `     : LowDoc Loan Program means the borrower can borrow with little administration..
- `NAICS`                  : North American industry classification system code
- `Term`                   : The term provides information on how long the loan will take
- `GrAppv`                 : Gross amount of loan approved by bank
- `SBA_Appv`               : SBA's guaranteed amount of approved loan

PREDICTION RESULT
---
The prediction result interface:
![](https://github.com/bagjasatia/Final_Project_SBA_Loan_Approval/blob/master/Interface/result-interface.png)

VISUALISATION PAGE
---
Histogram
![](https://github.com/bagjasatia/Final_Project_SBA_Loan_Approval/blob/master/Interface/boxplot-interface.png)

Boxplot
![](https://github.com/bagjasatia/Final_Project_SBA_Loan_Approval/blob/master/Interface/histogram-interface.png)

Scatter Plot
![](https://github.com/bagjasatia/Final_Project_SBA_Loan_Approval/blob/master/Interface/scatter-interface.png)

Pie Chart
![](https://github.com/bagjasatia/Final_Project_SBA_Loan_Approval/blob/master/Interface/pie-chart-interface.png)
