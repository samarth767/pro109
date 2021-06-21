import statistics
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("pro109data.csv")
math_score =  df["math score"].tolist() 

fig = ff.create_distplot([math_score], ["Math score"], show_hist=False) 
fig.show()

mean = statistics.mean(math_score)
median = statistics.median(math_score)
mode = statistics.mode(math_score)
stdev = statistics.stdev(math_score)

print("Mean of the data is", mean)
print("Median of the data is", median)
print("Mode of the data is", mode)

first_stdev_start, first_stdev_end = mean-stdev, mean + stdev
second_stdev_start, second_stdev_end = mean - (2*stdev), mean + (2*stdev)
third_stdev_start, third_stdev_end = mean - (3*stdev), mean + (3*stdev) 

score_list_within_first_stdev = [result for result in math_score if result > first_stdev_start and result < first_stdev_end]
score_list_within_second_stdev = [result for result in math_score if result > second_stdev_start and result < second_stdev_end] 
score_list_within_third_stdev = [result for result in math_score if result > third_stdev_start and result < third_stdev_end]

print("{}% of data lies within 1 standard deviation of maths score of students".format(len(score_list_within_first_stdev)*100.0/len(math_score))) 
print("{}% of data lies within 2 standard deviation of maths score of students".format(len(score_list_within_second_stdev)*100.0/len(math_score))) 
print("{}% of data lies within 3 standard deviation of math score of students".format(len(score_list_within_third_stdev)*100.0/len(math_score))) 