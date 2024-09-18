# DSDM_Denis_Angad_Coding_Challenge
BSE DSDM Coding Challenge with Python code and analysis

Objective : The research goal of this assignment is to find interesting correlation in world bank country level data and using python code to establish a meaningful trend.

Approach: 

1) We first downloaded World Bank country level data from World Bank repository for 2023, 2022 and 2021(Link : https://databank.worldbank.org/reports.aspx?source=2&series=SP.POP.TOTL&country=&_gl=1*1qc3e8l*_gcl_au*MTk4NTc2MzI2LjE3MjE2NDE2MjM.#)

2) Then we cleaned the data on python and identified variables, which have at least 70% fill rate.

3) Post clean up we computed the Correlation matrix across all variables and studied the outcomes.

Outcome :

1) We observed that GNI per capita, Atlas method (current US$) and Age dependency ratio, old (% of working-age population) are well correlated with each other. This implies that high employment of working age population is strongly related to increased GNI per capita.

2)  We also observed that the correlation is stable across time periods 2022 & 2021, making the result fairly robust.

3)  The Commented python codes & output images are posted on Github for review.

Limitations :

1) The study is fairly limited in design and further relations can be explored for more nuanced findings, which was left out of scope for this assignment.
2) Furthermore, there could be sampling and data collection issues in the data collected across geographies, which could further impact the result and the actual inference from the correlation.
3) Correlation does not imply causation, so inferences in the result should be made with care. 





