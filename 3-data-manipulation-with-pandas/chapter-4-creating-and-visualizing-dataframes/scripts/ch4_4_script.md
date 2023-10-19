You now know how to create your own DataFrames, but typing out your data entry-by-entry isn't usually the most efficient way to get your data into a DataFrame.

In this video, you'll learn how to pull data from CSV files.

CSV, or comma-separated values, is a common data storage file type. 

It's designed to store tabular data, just like a pandas DataFrame. 

It's a text file, where each row of data has its own line, and each value is separated by a comma.

Almost every database, programming language, and piece of data analysis software can read and write CSV files. That makes it a good storage format if you need to share your data with other people who may be using different tools than you.

Remember the dogs from the last video? Their data is stored in a CSV file called new_dogs-dot-csv, which looks like this.

We can put this data in a DataFrame using the handy pandas function, read-underscore-csv, and pass it the file path of the CSV.

Now that the data is in DataFrame form, we can manipulate it using some of the functions from earlier in the course. 

Here, we'll add a body mass index column.

Now that we've changed the data let's create an updated CSV file to share with the dogs' owners.

To convert a DataFrame to a CSV, we can use new_dogs dot to-underscore-csv, and pass in a new file path. 

If we take a look at the new file, it contains the BMI column.

Now it's time to practice getting data in and out of pandas!

