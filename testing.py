from tool_complexity import mytool, CrazyTransformer


test = mytool("Fastp")
test.PE_reads = 100000
test.SE_reads = 0
a = test.time_complexity()
b = test.memory_complexity()
print(test)