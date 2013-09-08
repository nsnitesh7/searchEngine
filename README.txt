First create xml file by running the batch file
------------------------------------------
python batchFile.py cacm.all

Then run the create index program:
------------------------------------------
python createIndex.py stopwords.txt testCollection.txt testIndex.txt titleIndex.txt

Then run the query index program:
-------------------------------------------
python queryIndex.py stopwords.txt testIndex.txt titleIndex.txt

Description of files:
---------------------------------------------
->stopwords.txt is the stopwords file
->testCollection.txt is the collection file
->IndexFile.txt is the index file(posting list of words)
->titleIndex.txt is the title index

