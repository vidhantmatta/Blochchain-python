import block
from chain import blockchain

chain = blockchain.Blockchain()

data={'Aadhar':'124456783454','Salary':'120000','Propertyworth':'4500000'}


first = block.Block(data['Aadhar'])
second = block.Block(data['Salary'])
third = block.Block(data['Propertyworth'])

chain.add_block(first)
chain.add_block(second)
chain.add_block(third)

first.update_data('so broke')

print(chain.broken)  # True

chain.repair()

print(chain.broken)  # False