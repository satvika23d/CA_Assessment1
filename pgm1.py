
# Given values
address_field = 200
R1 = 40
memory = {
    200: 500,
    240: 900
}

# a) Immediate Addressing
immediate_operand = 25
print("a) Immediate Addressing")
print("Rule: Operand = Given value")
print("Operand =", immediate_operand)

# b) Direct Addressing
direct_EA = address_field
print("\nb) Direct Addressing")
print("Rule: EA = Address field")
print("Effective Address =", direct_EA)

# c) Indirect Addressing
indirect_EA = memory[address_field]
print("\nc) Indirect Addressing")
print("Rule: EA = Memory[Address field]")
print("Effective Address =", indirect_EA)

# d) Indexed Addressing
indexed_EA = address_field + R1
print("\nd) Indexed Addressing")
print("Rule: EA = Address field + R1")
print("Effective Address =", indexed_EA)
print("Operand =", memory[indexed_EA])
