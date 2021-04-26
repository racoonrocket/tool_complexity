# tool_complexity
Trying to forecast how much will it take to run bioinformatics tools

#Add new tools to the yaml file 

#Use mytool class

If you want to know how much will it take to run a fastp:
call mytool class
'''
myfastp = mytool("fastp")
'''
Add variables asked by mytool class
'''
myfastp.PE_reads = 0

myfastp.SE_reads = 1000000
'''
Use time_complexity() and memory_complexity() to evaluate the time and memory it will take to run you tool with these params.

'''
print(myfastp.time_complexity())
print(myfastp.memory_complexity())
'''
