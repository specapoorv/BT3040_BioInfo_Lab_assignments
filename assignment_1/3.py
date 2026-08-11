#seq : str = input() #should be string can be typecasted
 
seq = "CTCGGATTTGTAAAGATCATGATCTCATACATAGTACCTAGCCA"
seq.upper()

complement_map = {'A':'T', 'T':'A', "G":"C", 'C':'G'}

#o(1) comprehension since hashmap
complementary_strand = "".join([complement_map[base] for base in seq])

print("given strand is", seq)
print("its complement is", complementary_strand)