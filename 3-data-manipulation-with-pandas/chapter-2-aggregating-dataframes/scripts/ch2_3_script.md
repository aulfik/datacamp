So far, you've been calculating summary statistics for all rows of a dataset, but summary statistics can be useful to compare different groups.

While computing summary statistics of entire columns may be useful, you can gain many insights from summaries of individual groups. For example, does one color of dog weigh more than another on average? Are female dogs taller than males? 

You can already answer these questions with what you've learned so far!

We can subset the dogs into groups based on their color, and take the mean of each. But that's a lot of work, and the duplicated code means you can easily introduce copy and paste bugs.

That's where the groupby method comes in. 

We can group by the color variable, select the weight column, and take the mean. This will give us the mean weight for each dog color.

This was just one line of code compared to the five we had to write before to get the same results.

Just like with ungrouped summary statistics, we can use the agg method to get multiple statistics. Here, we pass a list of functions into agg after grouping by color. This gives us the minimum, maximum, and sum of the different colored dogs' weights.

You can also group by multiple columns and calculate summary statistics. Here, we group by color and breed, select the weight column and take the mean. This gives us the mean weight of each breed of each color.

You can also group by multiple columns and aggregate by multiple columns.

Now that we've talked about grouping, it's time to practice grouped summary statistics.

