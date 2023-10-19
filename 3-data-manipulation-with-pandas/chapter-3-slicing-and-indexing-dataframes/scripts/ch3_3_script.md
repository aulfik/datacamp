You saw how to create pivot tables with pandas in chapter two. In this lesson, you'll perform subsetting and calculations on pivot tables.

Here's a larger version of the dog dataset. The extra dogs mean we have something to compute on.

Recall that you create a pivot table by calling dot-pivot_table. The first argument is the column name containing values to aggregate. The index argument lists the columns to group by and display in rows, and the columns argument lists the columns to group by and display in columns.

We'll use the default aggregation function, which is mean.

Pivot tables are just DataFrames with sorted indexes. That means that all the fun stuff you've learned so far this chapter can be used on them.

In particular, the loc and slicing combination is ideal for subsetting pivot tables, like so.

The methods for calculating summary statistics on a DataFrame, such as mean, have an axis argument.

The default value is "index," which means "calculate the statistic across rows." Here, the mean is calculated for each color. That is, "across the breeds." The behavior is the same as if you hadn't specified the axis argument.

To calculate a summary statistic for each row, that is, "across the columns," you set axis to "columns." Here, the mean height is calculated for each breed. That is, "across the colors."

For most DataFrames, setting the axis argument doesn't make any sense, since you'll have different data types in each column. Pivot tables are a special case since every column contains the same data type.

Time to play with pivot tables!
