
#### ********************** LOGICAL PROCESSING HOMEWORK *******************####
#### Hannah Van Hollebeke ----------- u0697848 ------------ 20220917-------####


influenza_genome = [19, 15, 7, 9, 12, 6, 17, 20, 29, 14, 22, 8, 15, 12, 21, 25, 11, 10, 30, 4, 6, 24, 18, 21, 28, 22, 13, 19, 4, 23, 16, 25, 13, 28, 16, 29, 4, 3, 25, 13, 10, 26, 26, 18, 25, 28, 24, 18, 3, 9, 11, 29, 30, 16, 24, 5, 5, 25, 14, 7, 1, 15, 6, 6, 19, 19, 15, 2, 14, 7, 21, 5, 26, 25, 18, 18, 9, 7, 27, 4, 1, 23, 30, 25, 24, 29, 11, 16, 20, 15, 2, 9, 8, 13, 1, 13, 5, 17, 29, 25, 16, 13, 3, 30, 10, 21, 9, 18, 20, 14, 20, 19, 6, 4, 20, 5, 14, 5, 12, 27, 18, 28, 13, 30, 6, 9, 12, 9, 29, 4, 14, 22, 7, 25, 11, 12, 5, 24, 6, 3, 8, 3, 20, 24, 8, 23, 22, 11, 22, 10, 13, 14, 2, 6, 22, 22, 7, 6, 18, 28, 25, 4, 6, 24, 10, 24, 15, 18, 12, 24, 10, 16, 24, 21, 19, 24, 8, 8, 8, 10, 8, 15, 26, 14, 21, 18, 6, 10, 23, 2, 20, 15, 1, 4, 20, 8, 6, 1, 4, 15, 21, 26, 25, 1, 24, 15, 27, 8, 23, 4, 30, 22, 1, 3, 7, 16, 18, 29, 11, 4, 1, 29, 30, 16, 30, 10, 2, 26, 26, 7, 10, 15, 6, 25, 4, 7, 12, 24, 5, 8, 23, 16, 8, 3, 16, 1, 9, 4, 27, 26, 9, 25, 7, 14, 27, 21, 27, 28, 2, 2, 27, 22, 3, 23, 14, 16, 30, 12, 14, 8, 10, 5, 16, 12, 24, 3, 28, 9, 21, 7, 25, 9, 5, 3, 27, 7, 29, 25, 13, 11, 25, 21, 2, 14, 8, 17, 18, 23, 22, 12, 7, 26, 11, 25, 1, 23, 9, 12, 2, 4, 17, 27, 9, 13, 19, 15, 10, 12, 21, 25, 5, 1, 16, 17, 28, 23, 18, 10, 15, 18, 1, 11, 14, 10, 18, 12, 1, 23, 23, 25, 13, 27, 27, 6, 9, 11, 23, 6, 23, 14, 9, 15, 11, 24, 11, 29, 18, 6, 19, 16, 14, 26, 2, 14, 15, 25, 6, 21, 23, 25, 27, 5, 1, 17, 4, 7, 18, 8, 9, 10, 5, 21, 29, 9, 6, 2, 22, 12, 1, 13, 19, 6, 17, 21, 22, 26, 21, 10, 29, 8, 13, 10, 29, 6, 29, 16, 30, 5, 25, 14, 15, 15, 9, 24, 13, 5, 28, 18, 11, 21, 15, 12, 5, 16, 5, 29, 29, 29, 3, 10, 24, 16, 16, 12, 14, 6, 22, 21, 10, 10, 2, 14, 9, 29, 29, 2, 26, 11, 6, 7, 28, 10, 3, 24, 30, 2, 23, 9, 29, 27, 19, 1, 15, 11, 5, 7, 9, 26, 28, 27, 10, 20, 23, 29, 10, 15, 30, 13, 2, 11, 5, 9, 2, 30, 27, 14, 11, 20, 19, 1, 12, 10, 8, 6, 16, 3, 25, 5, 10, 24]

# Create a copy of influenza_genome so that the unmodified one can be modified again in 1.4
influenza_genome_OG = [x for x in influenza_genome]


#### ---------------- Problem 1 Stacking logical operators -------------------####

# Given the array influenza_genome, write code that uses for loops and if statements to do the following and print the results(see below for instructions):

# ******************************* 1.1 ********************************************
# 1.1 add 1 to the value at the index 300.
# Original value of index 300
print(influenza_genome[300])

# Modify influenza_genome so that index 300 is now 1 greater than the original value
influenza_genome[300] += 1
print(influenza_genome[300])


# ****************************** 1.2 *********************************************
# 1.2 for the first 30 elements, if the value of the element is divisable by 3, multiply the value by 3.

# Print unmodified values at index 0 to 29, 30 total values
print(influenza_genome[0:30])

# Use a for loop to iterate through these indices and change the values so that they are 3 times greater than initally if they meet the specified condition. 
for el in range(len(influenza_genome[:30])):
    if influenza_genome[el] %3 == 0:
        influenza_genome[el] *= 3

# Print original list again to see that values divisible by 3 are modified 
print(influenza_genome[0:30])


# ****************************** 1.3 *********************************************
# 1.3 for the last 30 elements, if the index value at that point is divisable by 5, replace the value with "a".

# Print original values
print(influenza_genome[-30:])

# Loop through those values by specifying the start (30 from the last index) and end (the last index) indices by using the length function
for el in range((len(influenza_genome) - 30), len(influenza_genome)):
    if influenza_genome[el] %5 == 0:
        influenza_genome[el] = 'a'
 
# Print modified list 
print(influenza_genome[-30:])


# ****************************** 1.4 *********************************************
# 1.4 for all elements between index 200 and 300, if the value of the element is divisable by BOTH 3 AND 5, replace the value with the 10.

# Print original values
print(influenza_genome[201:300])

# Use the same loop as 1.2 and 1.3, but now two conditions need to be met. For range, just specify the indices to start and end with
for el in range(201, 300):  # I am assuming between means not including 200 or 300
    if influenza_genome[el] % 5 == 0 and influenza_genome[el] % 3 == 0:
        influenza_genome[el] = 10
 
# Print modified list       
print(influenza_genome[201:300])



#### ---------------- Problem 2 Loops within loops -------------------------####

# Given the array influenza_genome, write code using both for and while loops that:

# ***************************** 2.1 *********************************************
# 2.1 Create a for loop that iterates over items index 234 through 237 and prints each value (ie there should be 4 items)

# Slice list so that the loop only has to look at the 4 items. The end slice value is non-inclusive
for i in influenza_genome[234:238]:
    print(i)


# ***************************** 2.2 *********************************************
# 2.2 Create a while loop that iterates over items index 234 through 237 and prints each value (ie there should be 4 items)

# Give the while loop a starting value
a = 234

# specify condition that value needs to be within certain range. Print value first, then increase the value by one until condition no longer true.
while a > 233 and a < 238:
    print(influenza_genome[a])
    a += 1 


# **************************** 2.3 *********************************************
 # 2.3 Create a for loop that iterates over items index 234 through 237 and if the index is 236 print the item 7 times.

# Use enumerate so that you can call the index and value separately. Enumerate has an argument where you can start the indexing at a certain index, this isn't required for the function to work, but this way you can specify the condition by the original index. Condition is based on index, but want to print the value. Use range to repeat the loop that prints the value at the specified index 7 times.
for i, val in enumerate(influenza_genome[234:238], start = 234):
    if i == 236:
        for j in range(7):
            print(val)
            
            
#### ------------------------ Problem 3 Functions ----------------------------####

# You are going to implement 3 funtions that will process the influenza_genome list in various ways.

# *************************** 3.1 **********************************************
# 3.1 write a function, that takes in the array as an argument, and outputs 10 values from the dataset, spaced out by indexes that are 25 apart (ie 0, 25, 50, etc) 

# define a function, initialize empty list, loop through the length of the list, the range function takes a third argument that specifies how many steps you want to increase by each time, add value to list, print list outside of loop  
def array_n10_s25(array):
    three_one = []
    for i in range(0, len(influenza_genome), 25):
        three_one.append(array[i])
    print(three_one[:10])
    
# Call function with influenza_genome as the array argument
array_n10_s25(influenza_genome)

# *************************** 3.2 **********************************************
# 3.2 write a function that takes in the dataset as an argument and outputs 20 values from the dataset, spaced out by indexes that are y apart (ie you can decide how far apart they should be iterated as long as they dont exceed the length of the dataset)

# Write same function as 3.1, but now the spacing argument in range is defined when the function is called, y. Because the output is needed in the next funtion, used return in addition to print so that it can be stored as a variable outside the function when the function is called. 
def array_n20_y(array, y):
    three_two = []
    for i in range(0, len(influenza_genome), y):
        three_two.append(array[i])
    print(three_two[0:20])
    return three_two[0:20]
    
# Call the function with list and desired index spacing, 10, as arguments. Store as variable.
three_two = array_n20_y(influenza_genome, 10)

# *************************** 3.3 *********************************************
# 3.3 write a function that takes the output from the function from 3.2 as an argument, then only prints out every other item (ie there should only be 10 outputs)

# Reuse the same function, but now output is the argument. Use 2 for spacing.
def array_n20_skip(output):
    three_three = []
    for i in range(0, len(output), 2):
        three_three.append(output[i])
    print(three_three)
    
# Call function with the variable that stores the output from three_two function as an argument
array_n20_skip(three_two)


#### ------------------- Problem 4 Putting it all Together ----------------####
# ******************************** 4.1 ****************************************
# Write a function that implements the code from problem 1.4, then implements the code from problem 2.3.

# The function should create a modified version of the influenza_genome list as per 1.4, then print the section described in problem 2.3. 

# Print the copy of influenza genome created at the beginning because the 1.4 code has already modifed the other one.
print(influenza_genome_OG[201:300])

# Define function, paste in code from 1.4 and 2.3 sequentially, and not nested withing each other. The first one modifies the list passed in, the second iterates through it to print the specified value.
def array_mod_4(array):
    for el in range(201, 300):
        if array[el] % 5 == 0 and array[el] % 3 == 0:
            array[el] = 10
    for i, val in enumerate(array[234:238], start = 234):
        if i == 236:
            for j in range(7):
                print(val)

# Call the function with the original, influenza_genome_OG.  
array_mod_4(influenza_genome_OG)

# It should be the same as the modified influenza_genome version after 1.4 in the specified range.
print(influenza_genome_OG[201:300])