
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# 1. Setup diagram
plt.figure(figsize=(8, 6))
plt.title("Project Setup Structure")
setup_components = ['TensorFlow', 'NumPy', 'Matplotlib', 'Scikit-learn']
y_pos = np.arange(len(setup_components))
plt.barh(y_pos, [1]*len(setup_components))
plt.yticks(y_pos, setup_components)
plt.xlabel('Components')
plt.savefig('images/setup.png', bbox_inches='tight')
plt.close()

# 2. Data structure diagram
plt.figure(figsize=(10, 6))
data = np.random.rand(10, 30)
plt.imshow(data, aspect='auto', cmap='viridis')
plt.colorbar(label='Feature Values')
plt.title('Data Structure Visualization')
plt.xlabel('30 Features')
plt.ylabel('Samples')
plt.savefig('images/data_structure.png', bbox_inches='tight')
plt.close()

# 3. Network architecture
G = nx.DiGraph()
# Add nodes for each layer
input_nodes = [f'i{i}' for i in range(3)]
hidden_nodes = [f'h{i}' for i in range(3)]
output_nodes = ['o']

# Add nodes with positions
pos = {}
for i, node in enumerate(input_nodes):
    G.add_node(node)
    pos[node] = (0, i)
for i, node in enumerate(hidden_nodes):
    G.add_node(node)
    pos[node] = (1, i)
G.add_node('o')
pos['o'] = (2, 1)

# Add edges
for i in input_nodes:
    for h in hidden_nodes:
        G.add_edge(i, h)
for h in hidden_nodes:
    G.add_edge(h, 'o')

plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', 
        node_size=1000, arrowsize=20)
plt.title('Neural Network Architecture')
plt.savefig('images/network_architecture.png', bbox_inches='tight')
plt.close()

# 4. Training process
epochs = np.arange(20)
acc = 1 / (1 + np.exp(-epochs/5))
loss = 1 - acc

plt.figure(figsize=(10, 6))
plt.plot(epochs, acc, 'g-', label='Accuracy')
plt.plot(epochs, loss, 'r-', label='Loss')
plt.title('Training Process')
plt.xlabel('Epochs')
plt.ylabel('Metrics')
plt.legend()
plt.grid(True)
plt.savefig('images/training_process.png', bbox_inches='tight')
plt.close()
