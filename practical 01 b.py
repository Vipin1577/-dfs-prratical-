# dfs prratical 1 b

def dfs(visited, graph, start):
    if start not in visited:
        visited.add(start)
        print(start)
        for neighbour in graph[start]:
            dfs(visited, graph, neighbour)

graph ={
    '0':set(['1','2']),
    '1':set(['0' ,'3', '4']),
    '2':set(['0' ,'4']),
    '3':set(['1' ,'4']),
    '4':set(['1' ,'2','3']),
    }
visited = set()
start='0'
dfs(visited,graph,start)
