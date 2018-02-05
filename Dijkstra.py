# -*- coding: utf-8 -*-


graph = {}

# 使用散列表，表示边的权重
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

# 获取起点的所有邻居
print graph["start"].keys()
# 获悉边的权重
print graph["start"]["a"]
print graph["start"]["b"]

# 添加其他节点及邻居
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
# 终点没有任何邻居
graph["fin"] = {}

# 表示无穷大
infinity = float("inf")

# 开销表
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 存储父节点
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 记录处理过的点
processed = []

# 找出开销最低的节点
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # 遍历所有节点
        cost = costs[node]
        # 如果当前节点的开销更低且未处理过
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost    # 将其视为开销最低的点
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)  # 未处理的节点中找出开销最小的节点
while node is not None:  # 在所有节点处理后结束
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  # 遍历当前节点所有邻居
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:  # 如果经当前节点前往该邻居更近
            costs[n] = new_cost  # 就更新该邻居的开销
            parents[n] = node    # 同时将改邻居的父节点设置为当前节点
    processed.append(node)  # 将当前节点标记为处理过
    node = find_lowest_cost_node(costs)  # 找出接下来要处理的节点，并循环

print graph
print costs
print parents
print processed