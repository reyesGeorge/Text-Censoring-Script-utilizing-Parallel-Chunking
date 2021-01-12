# Text-Censoring-Script-utilizing-Parallel-Chunking
This is a script that takes in a large text file, breaks it up into chunks under ~4MB and passes them in to a word censoring package to return your censored text.

The schema of the .txt file should be [body, id] -> (body = string text, id=identifier for that text)

If you have another schema for your .txt file then change the for loop to accomodate your specific needs.

# Performance
This script can parse through each GB in 12-16 seconds depending on your hardware and how large your chunks are.
