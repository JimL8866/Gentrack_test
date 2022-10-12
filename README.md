# 1. What was done:
1). created a reader class with xml_reader and data_validation functions. 

2). xml_reader function to parse xml file and get the CSVIntervalData content.

3). data_validation function inculdes all the data rules and then to validate the data in CSVIntervalData.

4). if data is valid then create each csv files.

5). csv file named from the second field in the "200" row, with "100" row as header, starting "200" row, inclduing "300" row and stop until the next "200" row or hit "900" row.

6). removed leading and trailing white spaces, tabs, additional newlines.

7). created automated tests with edge cases and verified code works.

# 2. What wasn't done:
1). add 900 row as trailer for each csv file.

# 3. What would be done with more time:
1). add 900 row as trailer for each csv file.

2). created more testing cases to test code.

3). format each row in csv file

# update:
fixed code and added 900 row as the trailer for each csv file