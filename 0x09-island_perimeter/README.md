# Island perimeter

*Explanation:* 
The function iterates over each cell in the grid, and if the cell contains land, it adds 4 to the perimeter. Then, it checks if the cell to the left and the cell above also contain land. If either of them does, it subtracts 2 from the perimeter because those adjacent cells will share a side with the current cell.

This approach works because each internal edge between two adjacent cells of land is counted twice, once by each cell. Subtracting 2 from the perimeter for each internal edge ensures that these edges are only counted once. The perimeter of the island is the sum of all edges of land cells that are adjacent to water cells or to the edge of the grid.