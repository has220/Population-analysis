#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10        20        30          40         50        60         70         80
#-------------------------------------------------------------------------------


#Function 1
def read_annual(filename,report=None):
    
    myfile = open(filename,'r')   #open the file for reading
    mydata = myfile.readlines() 
    #read every line of the file, store it in a list
    
    
    years =  []                  #create an empty list 
    myreport = {}                #create an empty dictionary
    
    
    
    for val in mydata:            #go through the elements in the list 
        if mydata.index(val) == 0:  #check if the first index is reached
           #first index always contains the header information (State)
            newlis = val.split(",")  #split by the comma and create a new list
            for next_val in newlis:      #go through the new list  
                if "." in next_val:   #check if any element contains a period
                    next_val = next_val.strip(".") #remove the period
                    mykey = next_val   #store the element in a variable mykey
        
                if next_val == newlis[3]:   
                #check if the last index is reached (third column)
                    next_val = next_val.replace("\\n","") 
                    #replace all of the newlines 
                    next_val = int(next_val)     
                    #change the element (year) to a number
                    years = []      #reset the years list to be empty
                    years.append(next_val)  #add the year to the years list
                
        else:   #everything else in the mydata list contains population data
            newlis = val.split(',"')  
            #split the elements by comma and double quote
            
            for next_val in newlis:  #go through the elements in the new list
                if "." in next_val:  #check if there is a period
                    next_val = next_val.strip(".")  #remove the period
                    next_val = next_val.strip(",") #remove all of the comma's
                    mykey = next_val   
                    #store the element in a variable my key
            
                if next_val == newlis[3]:  
                #check if last index is reached (third column)
                #last index always contains population data
                    next_val = next_val[:-2]         
                    #slice the string, get rid of newline 
                    next_val = next_val.replace(",","") #replace all comma's 
                    next_val = int(next_val)  #change the string to a number
                    years = []     #reset the years list to be empty
                    years.append(next_val)    
                    #add the population data to the years list
            
        
        myreport[mykey] = years    
        #update the dictionary for every key value pair
        #keys are the elements and values is the list years
        
    
    
    
    if report != None:   #check if report argument is not equal to None 
        
        #update the values of the State key for report dictionary
        report["State"] = report["State"] + myreport["State"]
        report["State"].sort()      #sort the years in ascending order
        
        
        
        filecopy = filename   #make a copy of the string argument filename
        filecopy = filecopy[:4]   
        #slice the string so it only contains the year number
            
        filecopy = int(filecopy)   #change string to number
        
        myindex = report["State"].index(filecopy)  
     #myindex is the index where the year is located at in the State key
     #myindex determines where to place the population data in the report 
     #dictionary values 
       


        for key in report:          #go through the report keys
            for next_key in myreport:    #go through myreport keys
                if next_key == "State":   #ignore the State key
                    continue 
                if key == next_key:    #if keys are the same
                    if report[key] == myreport[next_key]:   
                    #if values are the same
                        report = report   #keep the report dictionary
                    else:
                        for other_key in myreport[key]:   
                        #go through the values of myreport
                            report[next_key].insert(myindex,other_key) 
                        #insert the population data from myreport into the 
                        #correct index in the report dictionary
            
                else:
                    continue    
                    #continue until the end of the dictionary is reached


        return report   #return the updated report (if report is not None)
        
            
    
    
    
    
    myfile.close()         #close the file
    
    return myreport     #return myreport (if report is None)
    
    

    
    
    
    
    
#Function 2   
def build_rate(report):
    
    rate = report.copy()     #make a copy of the report argument to avoid
                             #modifying the original report
    rate.pop("State")     #remove the State key and values, don't need it
                          #for calculating the rate
    
    for key in rate:        #go through the rate keys
        start = (rate[key][0])   #starting year is the first index of list
        ending = (rate[key][-1]) #ending year is the last index of list
        change = ((ending-start)/start) #the rate is the difference of
              #the last year from the first year divided by first year
    
        rate[key] = change #update the rate dictionary key's with the
                         #change calculated above        
    
    
    
    
    
    return rate          #return the rate dictionary
    
    

    
    
    
    
    
#Function 3
def build_statistics(report,rate):

    
    #total increase
   
    copreport = report.copy() 
    #make a copy of the report to avoid modifying the original
    copreport.pop("State")   #remove the State key and values
    mylis = []               #create an empty list
    for key in copreport:       #go through the copied dictionary 
        endyear = (copreport[key][-1]) #end year is the last index of list
        startyear = (copreport[key][0]) #start year is the first index of list
        increase = endyear-startyear  #increase in population is end - start
        mylis.append(increase)    #add all of the states increase to mylis

    sum = 0               #start a sum
    for val in mylis:     #go through all increases in mylis
        sum = sum + val   #add up all of the increases
    totincr = sum         #total increase is the sum of all increases
    
    
    
    
    
    
    
    #most populous and least populous
    
    firstcopy = report.copy()    
    #make a copy of report to avoid modifying the original
    firstcopy.pop("State")      #remove the State key and values
    for key in firstcopy:          #go through the copied dictionary
        firstcopy[key] = firstcopy[key][-1]  
        #update the dictionary keys with the 
        #last index of the list (ending year)
    
    mylis1 = []                #create an empty list
    for next_key in firstcopy: #go through the updated copied dictionary
        mylis1.append(firstcopy[next_key]) #add the ending years to mylis
    
    newmx = max(mylis1)        #find the max of the list
    newmn = min(mylis1)        #find the min of the list
    for other_key in firstcopy:          
    #go through the copied dictionary again
        if firstcopy[other_key] == newmx:  
        #check which key matches the maximum
            mostpop = other_key           
            #most populous is the key that matches the max
        if firstcopy[other_key] == newmn:  
        #check which key matches the minimum 
            leastpop = other_key          
            #least populous is the key that matches the min
   

    
    
    
    
    
    #largest increase
    
    copied = report.copy()      
    #make a copy of report to avoid modifying the original
    for key in copied:       #go through the copied dictionary
        start = copied[key][0]   #start year is the first index
        end = copied[key][-1]    #end year is the last index
        increase = end-start   
        #difference of end - start is the increase
        copied[key] = increase   
        #update the copied dictionary values with each states increase

    mylis2 = []                #create an empty list
    for next_key in copied:  #go through the updated copied dictionary
        mylis2.append(copied[next_key]) 
        #add all the increases to the list

    increasemax = max(mylis2)    
    #find the largest increase by taking max of list

    for other_key in copied:      #go though the copied dictionary
        if copied[other_key] == increasemax:   
        #check which key matches the maximum
            largincr = other_key           
            #largest increase is the key that matches the max

    
    
    
    
    
    #fastest growing
    
    mylis3 = []           #create an empty list
    for key in rate:      #go through the rate dictionary 
        mylis3.append(rate[key])   
        #add all the rate values to the list
     
    newmax = max(mylis3)    #take the max of the list

    for next_key in rate:   #go through rate dictionary
        if rate[next_key] == newmax:   
        #check which key matches the max
            fastrate = next_key      
            #fastest rate is the key that matches the max
    
    
    
    
    
    
    
    #decreasing
    
    mylis4 = []          #create an empty list
    for key in rate:     #go through the rate dictionary
        if rate[key] < 0:   
        #check if any value in the dictionary is negative
            mylis4.append(key)  
            #add that key with the negative value to the list
    decrease = mylis4           
    #list of decreasing states
    decrease.sort()      
    #sort the list in alphabetical order
    
    
    
    
    
    
    
    #create the statistics dictionary
    statistics = {"total increase":totincr, "most populous":mostpop, 
    "least populous":leastpop,"largest increase":largincr,
    "fastest growing":fastrate,"decreasing":decrease}
    
    
    
    return statistics          #return the statistics dictionary

    


    
    
    
    
#Function 4
def write_report(r,filename):

    myfile = open(filename,'w')    #open file for writing
    
    r_copy = r.copy()  #make copy of report to avoid modifying original
    for key in r_copy:                 #go through the report dictionary
        r_copy[key] = str(r_copy[key])      #change the values to strings
        for next_key in r_copy[key]:    #go through the values of report
            r_copy[key] = r_copy[key].strip("[]")  
            #remove the brackets for each list value

    
    
    
    mylis = []                  #create an empty list
    otherlis = []               #create a second empty list
    for key,val in r_copy.items():  #go through the items in the report dictionary
        line = (key,val)       #change each item into a tuple
        otherlis = []          #reset the otherlis 
        for next_val in line:        #go through the elements of the tuple
            next_val = next_val.split(",")  
            #create a list, split by the comma
            
            for other_val in next_val:    #go through the split list 
                
                other_val = other_val.strip(" ")  
                #remove all of the whitespace
                otherlis.append(other_val)  
                #add this value to the otherlis
        
        
    
        
        mytup = tuple(otherlis)  #change the otherlis to a tuple
        mystr = ""             #create an empty string
        for new_val in mytup:  #go through the elements of the tuple
            
            mystr = mystr + '"' + "," + '"' + new_val   
            #add the strings together
            newstr = mystr + '"' + "\n"   
            #add a newline at the end of each string
        mylis.append(newstr)            
        #add the strings to a list

    
    
    
    
    
    
    newlis = []         #create another empty list
    for val in mylis:      #go through the elements in mylis
        val = val[2:]      
        #slice each string to remove extra characters at beginning
        newlis.append(val)  
        #add the sliced strings to the newlis
    
        
    newlis.sort()   #sort the newlis in alphabetical order
    for val in newlis:     #go through the elements of newlis
        if "State" in val:  
        #look for the element that contains the header information
            statevar = val    
            #store the header information in a variable
            myindex = newlis.index(val)  
            #find the index where the "State" was at  
                                      
            newlis.pop(myindex)  
            #remove the "State" in the newlis since it 
            #was sorted in alphabetical order
    
    newlis = [statevar] + newlis  
    #add the header information to the beginning of the list
    
    
    for val in newlis:    #go through the elements in the newlis
        myfile.write(val) #write each element to the file
    
    myfile.close()        #close the file
    
    
    
    
    
    
    
    
    return         #return None
    
    
    
 



 
#Function 5
def write_statistics(stats,filename):

    myfile = open(filename,'w')    #open file for writing
    
    mylis = []                  #create an empty list
    for key,val in stats.items():    
    #go through the items in the stats dictionary
        line = (key,val)      #change each item into a tuple
        mystr = ""          #create an empty string
        for new_val in line:   #go through each element in the tuple
            new_val = str(new_val)   #change everything to a string
            mystr = mystr + '"' + "," + '"' + new_val  
            #add up all of the strings
            newstr = mystr + '"' + "\n"   
            #add a newline at the end of each string
    
        mylis.append(newstr)            
        #add the strings to mylis
    

    mysortlis = (sorted(mylis,reverse=True))  
   #sort the list in reverse order
   #the statistics output is listed in reverse alphabetical order
    
    newsortlis = []    #create an empty list again
    for val in mysortlis:  #go through the reversed sorted list
        val = val[2:]       #slice each string 
       #remove extra characters at beginning of the string
        newsortlis.append(val) #add each string into the new list 
    
    
    
    
    newsortlis = ['"Statistic","Value"\n'] + newsortlis   
    #add the header information at the beginning of the list

    for next_val in newsortlis:  
    #go through each element in the list
        myfile.write(next_val)  
        #write each element to the file


    myfile.close()    #close the file 
    
    
    
    
    return     #None
    
 
    
    
    
    

        

