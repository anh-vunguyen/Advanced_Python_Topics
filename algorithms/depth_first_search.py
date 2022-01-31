from collections import defaultdict
class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, x, y):
        """
        Add edge to the graph.

        Parameters
        ----------
        x : start vertex
        y: end vertex

        Returns
        -------
        None
        """
        self.graph[x].append(y)
        self.graph[y].append(x)


    def dfs_helper(self, s, visited):
        """
        Helper method for the depth first search recursion.

        Parameters
        ----------
        s : source vertex of the graph traversal.
        visited : list of visited vertices.

        Returns
        -------
        None
        """
        for node in self.graph[s]:
            if not visited[node]:
                visited[node] = True
                print(node, end="->")
                self.dfs_helper(node, visited)


    def depth_first_search(self, s):
        """
        Print the result of the depth first search of the graph.

        Parameters
        ----------
        s : source node of the graph traversal.

        Returns
        -------
        None
        """

        visited = [False] * (len(self.graph) + 1)
        visited[s] = True
        print(s, end="->")
        self.dfs_helper(s, visited)


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(2, 5)
    graph.add_edge(2, 7)
    graph.add_edge(2, 8)
    graph.add_edge(3, 10)
    graph.add_edge(3, 9)
    graph.add_edge(5, 6)
    graph.add_edge(5, 7)
    graph.add_edge(7, 8)

    print(graph.depth_first_search(1))
