# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: The Impact of the 2016 SAT Format on SAT Scores 2017 and 2018

## Overview

Agenda:
- Problem Statement
- Datasets
- Data Dictionary
- Deliverables
- Conclusion

For our first project, we're going to take a look at aggregate SAT and ACT scores and participation rates in the United States.

The SAT and ACT are standardized tests that many colleges and universities in the United States require for their admissions process. This score is used along with other materials such as grade point average (GPA) and essay responses to determine whether or not a potential student will be accepted to the university.

The SAT has two sections of the test: Evidence-Based Reading and Writing and Math ([*source*](https://www.princetonreview.com/college/sat-sections)). The ACT has 4 sections: English, Mathematics, Reading, and Science, with an additional optional writing section ([*source*](https://www.act.org/content/act/en/products-and-services/the-act/scores/understanding-your-scores.html)). They have different score ranges, which you can read more about on their websites or additional outside sources (a quick Google search will help you understand the scores for each test):
* [SAT](https://collegereadiness.collegeboard.org/sat)
* [ACT](https://www.act.org/content/act/en.html)

Standardized tests have long been a controversial topic for students, administrators, and legislators. Since the 1940's, an increasing number of colleges have been using scores from sudents' performances on tests like the SAT and the ACT as a measure for college readiness and aptitude ([*source*](https://www.minotdailynews.com/news/local-news/2017/04/a-brief-history-of-the-sat-and-act/)). Supporters of these tests argue that these scores can be used as an objective measure to determine college admittance. Opponents of these tests claim that these tests are not accurate measures of students potential or ability and serve as an inequitable barrier to entry.

### Problem Statement

Since the new format for the SAT was released in March 2016([*source*](https://www.pcsb.org/cms/lib/FL01903687/Centricity/Domain/6701/New%20SAT.pdf)), the College Board - the organization that administers the SAT - would like to assess statewide adaptability to the new format and endeavors to detect states which may need assistance for SAT preparation for their students.

---

### Datasets

#### Provided Data

There are 4 datasets included in the [`data`](./data/) folder for this project:

* [`act_2017.csv`](./data/act_2017.csv): 2017 ACT Scores by State ([source](https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows))
* [`act_2018.csv`](./data/act_2018.csv): 2018 ACT Scores by State ([source](https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows))

* [`sat_2017.csv`](./data/sat_2017.csv): 2017 SAT Scores by State ([source](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/))
* [`sat_2018.csv`](./data/sat_2018.csv): 2018 SAT Scores by State ([source](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/))

---

### Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|state|object|sat_2017.csv|Name of the state|
|2017_sat_participation|float64|sat_2017.csv|SAT 2017 participation rate|
|2017_sat_read_write|float64|sat_2017.csv|SAT 2017 Evidence-Based Reading and Writing Score|
|2017_sat_math|float64|sat_2017.csv|SAT 2017 Math Score|
|2017_sat_total|float64|sat_2017.csv|SAT 2017 Total Score|
|2017_act_participation|float64|sat_2017.csv|ACT 2017 participation rate|
|2017_act_english|float64|act_2017.csv|ACT 2017 English Score|
|2017_act_math|float64|act_2017.csv|ACT 2017 Math Score|
|2017_act_reading|float64|act_2017.csv|ACT 2017 Reading Score|
|2017_act_science|float64|act_2017.csv|ACT 2017 Science Score|
|2017_act_composite|float64|act_2017.csv|ACT 2017 Composite Score|
|2018_sat_participation|float64|sat_2018.csv|SAT 2018 participation rate|
|2018_sat_read_write|float64|sat_2018.csv|SAT 2018 Evidence-Based Reading and Writing Score|
|2018_sat_math|float64|sat_2018.csv|SAT 2018 Math Score|
|2018_sat_total|float64|sat_2018.csv|SAT 2018 Total Score|
|2018_act_participation|float64|act_2018.csv|ACT 2018 participation rate|
|2018_act_composite|float64|act_2017.csv|ACT 2018 Composite Score|

---

### Deliverables

For this initial project it will comprise:
- This README markdown file the provides an introduction and overview of the project.
- A Jupyter notebook that describes your data with visualizations & statistical analysis.
- Your presentation slideshow rendered as a .pdf file.

---

### Conclusion

* **Key Takeaways**:
- The new SAT format impacted the scores of bottom 5 performing states
- Top 5 performing states adapted well to the new SAT format
- Bottom 5 states saw drops in scores after the new format was implemented

* **Recommendation**:
- More SAT preparation support for the lowest 5 performing states, particularly for Utah which saw a noticeable drop in score
- Specific support on Evidence-Based Reading and Writing SAT Section should be given to Utah students
- Improve the exam format based on continuous feedback after encouraging more participation across the states

* **Limitations**:
- Our data on SAT scores may not be an accurate measurement of students’ ability in a particular state if participation rates vary widely across all states




---
