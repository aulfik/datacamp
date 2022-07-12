In the previous video,

we created the dictionary "world", which basically is a set of key value pairs. You could easily access the population of Albania, by passing the key in square brackets, like this.

For this lookup to work properly, the keys in a dictionary should be unique. If you try to add another key:value pair to world with the same key, Albania, for example, you'll see that the resulting world dictionary still contains three pairs. The last pair that you specified in the curly brackets was kept in the resulting dictionary.

Also, these unique keys in a dictionary should be so-called immutable objects. Basically, the content of immutable objects cannot be changed after they're created. Strings, booleans, integers and floats are immutable objects, but the list for example is mutable, because you can change its contents after it's created.

That's why this dictionary, that has all immutable objects as keys, is perfectly valid.

This one, however, that uses a list as a key, is not valid, so we get an error.

So now that you have an idea of how to build a valid dictionary and how to access it using square brackets, let's see how we can add more data to a dictionary that already exists.

Say for example that you, an employee of the World Bank, decide to acknowledge the Principality of Sealand. Sealand is an unrecognized micronation, on an offshore platform located in the North Sea. At the moment, it has 27 inhabitants.

To add this information, simply write the key sealand in square brackets and assign 27 expressed in millions to it with the equals sign.

If you check out "world" again, indeed, sealand is in there. To check this with code, you can also write "sealand in world", which gives you True if the key sealand is in there.

With the same syntax, you can also change values, for example, to update the population of sealand to 28. Because each key in a dictionary is unique, Python knows that you're not trying to create a new pair, but want to update the pair that's already in there.

You can see this from the printout here.

Suppose now that your boss didn't see the humour of adding Sealand to the list, and asks you to remove it again. You can do this with del, again pointing to sealand inside square brackets. If you print world again, Sealand is no longer in there. Good riddance!

If you remember the discussion of lists from the intro course, you'll notice that using lists

and dictionaries is pretty similar. You can

select, update and remove elements with square brackets.

There are some big differences though. The list is a sequence of values

that are indexed by a range of numbers. The dictionary, on the other hand,

is indexed by unique keys, that can be any immutable type. When to use which one, I hear you ask?

Well, if you have a collection of values

where the order matters, and you want to easily select entire subsets of data, you'll want to go with a list. If, on the other hand, you need some sort of

look up table, where looking for data should be fast and where you can specify unique keys, a dictionary is the preferred option.

Now off to some more exercises on dictionaries! I'll see you back here soon.

