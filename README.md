# InsightCodingChallenge_HiteshDas
Implementation of two features: 
(1) Clean and extract the text from the raw JSON tweets that come from the Twitter Streaming API, and track the number of tweets that contain unicode. 
(2) Calculate the average degree of a vertex in a Twitter hashtag graph for the last 60 seconds, and update this each time a new tweet appears.

Solution:
The coding is done in Python language. The single python code handles both the features. It is invoked by "run.sh" script. 
The python code name is "features.py".
I used Cloud 9 IDE to develop and execute the code. Paths for input and output files in the python code are ('/home/ubuntu/workspace/tweets.txt') and ('/home/ubuntu/workspace/ft1.txt', '/home/ubuntu/workspace/ft2.txt') respectively. The run.sh and features.py scripts were kepts in same workspace i.e., "/home/ubuntu/workspace/" during execution in Cloud 9 IDE.
The file "tweets.txt" (inside tweet_input folder) contains the test data that I used for execution.
The file "ft1.txt" (inside tweet_output folder) contains the output obtained for first feature.
The file "ft2.txt" (inside tweet_output folder) contains the output obtained for second feature.
The "time" module is imported for the 60 second window feature.
