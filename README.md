# Its_Learning
# "Its Learning" visual test

Title: Visual test

Description: Check webiste page elementes, are they in grid

Preconditions: Clear cookies before starting

Test Steps:
1. Clear browser cookies
2. Navigate to https://itslearning.com/no/
3. On pop up, accept all cookies
4. Maximize window
5. Try scrolling left and right (Horizontal scroll)
6. Navigate to other pages and do the same
7. Check if all grid elements fits in side grid area

# Expected result:
Fullscreen window. Should not be able to scroll left or right. 

# Result: 
There is a problem with "Nurture Grid" section, because some elements are out of position and it is posible to make horizontal scroll. 
All pages containing "Nurture Grid" section, are effected

# Selenium Test:
Have made a test to navigate to different pages. </br>
Take screenshot of page, then make horizontal scroll and take screenshot again </br>
And the last thing is to compare screenshots. (If you are not able to make horizontal scrolling, so screenshots should be the same) </br>
Used Image HASH for comparison </br>
![alt text](https://raw.githubusercontent.com/Karolis01/visual_test/master/screen.png)

# Screenshot of "Nurture Grid" section
![alt text](https://raw.githubusercontent.com/Karolis01/Its_Learning/master/Tests/Screen/Nurture_grid.png)

