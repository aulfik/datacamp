Slicing is a technique for selecting consecutive elements from objects.

Here are the dog breeds, this time as a list.

To slice the list, you pass first and last positions separated by a colon into square brackets. Remember that Python positions start from zero, so 2 refers to the third element, Chow Chow. Also remember that the last position, 5, is not included in the slice, so we finish at Labrador, not Chihuahua.

If you want the slice to start from the beginning of the list, you can omit the zero. Here, using colon-3 returns the first three elements.

Slicing with colon on its own returns the whole list.

You can also slice DataFrames, but first, you need to sort the index. Here, the dogs dataset has been given a multi-level index of breed and color; then, the index is sorted with sort_index.

To slice rows at the outer level of an index, you call loc, passing the first and last values separated by a colon.

The full dataset is shown on the right for comparison.

There are two differences compared to slicing lists. Rather than specifying row numbers, you specify index values. Secondly, notice that the final value is included. Here, Poodle is included in the results.

The same technique doesn't work on inner index levels. Here, trying to slice from Tan to Grey returns an empty DataFrame instead of the six dogs we wanted.

It's important to understand the danger here. pandas doesn't throw an error to let you know that there is a problem, so be careful when coding.

The correct approach to slicing at inner index levels is to pass the first and last positions as tuples. Here, the first element to include is a tuple of Labrador and Brown.

Since DataFrames are two-dimensional objects, you can also slice columns. You do this by passing two arguments to loc.

The simplest case involves subsetting columns but keeping all rows. To do this, pass a colon as the first argument to loc. As with slicing lists, a colon by itself means "keep everything."

The second argument takes column names as the first and last positions to slice on.

You can slice on rows and columns at the same time: simply pass the appropriate slice to each argument. Here, you see the previous two slices being performed in the same line of code.

An important use case of slicing is to subset DataFrames by a range of dates. To demonstrate this, let's set the date_of_birth column as the index and sort by this index.

You slice dates with the same syntax as other types. The first and last dates are passed as strings.

One helpful feature is that you can slice by partial dates. Here, the first and last positions are only specified as 2014 and 2016, with no month or day parts.

pandas interprets this as slicing from the start of 2014 to the end of 2016; that is, all dates in 2014, 2015, and 2016.

You can also slice DataFrames by row or column number using the iloc method. 

This uses a similar syntax to slicing lists, except that there are two arguments: one for rows and one for columns.

Notice that, like list slicing but unlike loc, the final values aren't included in the slice. In this case, the fifth row and fourth column aren't included.

Time for a nice slice!
