# Note on supported file formats

YouGov Poll supports datasets provided in following format:

|Question 1|Question 2|Question 3| ... |Question n-1|Question n|
|---|---|---|---|---| --- |
| T  | T  | F  | ...  | U   | F 
| ...  | ...  | ...  | ...  | ...   |
|   |   |   |   |   |
Fig. 1: **Tabelaric example**

```csv
unemployed,imprisoned, (...),previous_polls,
T,T,(...),F,
F,U,(...),U,
```
Fig. 2: **Text example**

In the header of the file there shall be list of comma-separated values of questions for the respondents.

In the following lines, there should be list of comma-sepparated answers of the respondents.

Possible answers are:

* `T` if respondent answered True to the question
* `F` if the respondent answered False to the question
* `U` if the respondent did not answer the question.

New values are appended to the file or to the new file after Save File Dialog.

Software detects only answers described above. 

It is possible to have multiple questions, not only five stated in the task.

YouGov Polls automatically detects how many questions are in the dataset and adjusts its 
behavior accordingly.

Also, it re-calculates statistics and suitability of the respondent on-the-fly.
