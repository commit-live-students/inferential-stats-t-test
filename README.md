# T-Test
## A study was conducted to examine the differences in perceived life satisfaction between older and younger adults.  
Ten older adults and ten younger adults were give a life satisfaction test (known to have high reliability and validity). 
Scores on the measure range from 0 to 60 with high scores indicative of high life satisfaction; 
low scores indicative of low life satisfaction.

The data are presented below.

    Older Adults = [45, 38, 52, 48, 25, 39, 51, 46, 55, 46]

    Younger Adults = [34, 22, 15, 27, 37, 41, 24, 19, 26, 36]

### Write a function *t\_test* that:

##### Takes 3 parameters:
    dataset1: List
    dataset2: List
    significance_level: float

##### Returns: 
    True, if set1 and set2 are significantly different.
    False, if they are significantly not different.