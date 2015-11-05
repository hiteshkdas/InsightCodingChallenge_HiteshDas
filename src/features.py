####################################################################################################################################
# Insight data engineering coding challenge
# This code is developed by Hitesh Das. 
# This python code handles both the features. This code was developed and executed on Cloud 9 IDE. 
# Code submission date: Nov 5th, 2015.
#####################################################################################################################################

import time          # Time module is imported to implement the 60 second window feature

f = open('/home/ubuntu/workspace/tweets.txt')      # Open the input file, "tweets.txt" which contains JSON messages
lines = f.readlines()        # Return a list of lines present in "tweets.txt"

no = 0                       # Counter variable to count number of tweets containing unicodes

last_lno = len(lines)         # Variable to keep track of total number of lines in "tweets.txt"

latest_line = lines[last_lno - 1]  # Extracts the last line in "tweets.txt" file


##### Determination of the latest time stamp ######################

start_last = latest_line.find('{"created_at":"') + 19
end_last = latest_line.find('","id"', start_last)
a_latest_line = time.strptime(latest_line[start_last:end_last], '%b %d %H:%M:%S +0000 %Y')
a_latest_line = time.mktime(a_latest_line)

###################################################################


######## Creating an output file, "ft2.txt" for the second feature ###########

fob1_1 = open('/home/ubuntu/workspace/ft2.txt', 'a')
fob1_1.write ("The extracted hash tags in the 60 second window:" "\n")
fob1_1.close()

##############################################################################


#list_of_elements = []
list_of_words = []
hash_tag_list = []
dic_h = {}
dir_a = {}


for line in lines:
    
     testline = line[:line.find('created_at":"') + 43]  # Determination of time stamp of each line present in "tweets.txt" 
    
    
    ## Determination of time difference between the current tweet and the latest (last) tweet #######################
    
     b_current_line = time.strptime(testline[19:], '%b %d %H:%M:%S +0000 %Y')
     b_current_line = time.mktime(b_current_line)
     seconds = a_latest_line - b_current_line  # Time difference 
     
    ################################################################################################################## 
    
    
     start = line.find('{"text":"') + 110
     end = line.find('","source"', start)
     
     
     #### Counting number of tweets containing unicodes #################################################
     
     a = line[start:end]
     b = line[start:end].decode('unicode_escape').encode('ascii','ignore')  # Removal of unicodes from the line
     
     if a == b:
         pass
     else:
         no = no + 1
         
     #####################################################################################################
     
     
     #### Creating an output file, "ft1.txt" for the first feature. The clean text is printed along with the timestamp ######################################
     
     fob = open('/home/ubuntu/workspace/ft1.txt', 'a')
     fob.write ((line[start:end].decode('unicode_escape').encode('ascii','ignore')).replace("\\", "") + " (timestamp: " + testline[15:] + ")" "\n")
     fob.close()
     
     #####################################################################################################################################################
     
     
     if seconds < 61:    # Consider the texts if they fall within the 60 second window
     
        list_of_words += b.split()
     
        for element in list_of_words:
         
            if element.startswith("#"):   # Extraction of hash tags
             
               hash_tag_list.append(element)  # List of hash tags
             
            else:
               pass
        
        
       ############ Printing the hash tags in the output file, "ft2.txt" (for second feature) ###########
        fob1 = open('/home/ubuntu/workspace/ft2.txt', 'a')
        fob1.write (', '.join(hash_tag_list) +" (timestamp: " + testline[15:] + ")" "\n")
        fob1.close()
       ##################################################################################################
       
        ##### Determination of hash tags with respective degrees (Hash tags within 60 second window) ##########################################
        if len(hash_tag_list) < 2:  # Consider the list of hash tags for hash tag graph only if there are at least two hash tags in that list
           pass
        else:
           for hash_element in hash_tag_list:
           
              if dic_h == {}:
                  dir_a[hash_element] = (len(hash_tag_list) -1)  # Creating a directory of hash tags (nodes) with respective degrees
                  
              else:
                 
                for item in dic_h:
                    
                    if hash_element == item:
                        
                       dir_a[hash_element] = (len(hash_tag_list) -1) + dic_h[item]
                       break
                    else:
                     
                       dir_a[hash_element] = (len(hash_tag_list) -1)
                      
        dic_h = dir_a.copy()
        #######################################################################################################################################
        
        
        list_of_words = []
        hash_tag_list = []
     
f.close()    ## Closing the input file, "tweets.txt"

######## Printing the number of tweets containing unicode in the output file, "ft1.txt" (First feature) ############
fob_agn = open('/home/ubuntu/workspace/ft1.txt', 'a')
fob_agn.write ("\n")
fob_agn.write (str(no) + " tweets contained unicode. \n")
fob_agn.close()
####################################################################################################################


#### Printing the degrees of individual hash tag in ft2.txt (part of second feature) ##############################
fob2 = open('/home/ubuntu/workspace/ft2.txt', 'a')
fob2.write ("\n""\n""The degree of each node (hash tag):" "\n")
for item_1 in dir_a:
  fob2.write (item_1 +" : " + str(dir_a[item_1])+"\n")
fob2.close()
###################################################################################################################


## Determination of rolling average degree ########################################################################
memb = 0
tot = 0
avg = 0
for member in dir_a:
    memb = memb + 1
    memb_val = int(dir_a[member])
    tot = memb_val + tot

try:    
    avg = float(tot)/float(memb)
  
except ZeroDivisionError:
    fob3 = open('/home/ubuntu/workspace/ft2.txt', 'a')
    fob3.write ("\n""\n""NO HASH TAGS FOUND IN THE TWEETS" "\n")
    fob3.close()
else:
    
    fob3 = open('/home/ubuntu/workspace/ft2.txt', 'a')
    fob3.write ("\n""\n""The rolling average degree is:" "\n")  # Printing the rolling average degree in ft2.txt (part of second feature)
    fob3.write (str(avg)+"\n")
    fob3.close()
###############################################################################################################################################

