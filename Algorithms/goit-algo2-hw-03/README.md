# goit-algo2-hw-03

## Task 1: maximum flow for goods logistics

- Algorithm: Edmonds–Karp.
- Network: terminals → warehouses → stores.
- Vertices: 22, including 20 physical nodes, a super-source and a super-sink.
- Maximum flow: **115 units**.

### Terminal-to-store flows

| Terminal   | Store    | Actual flow (units) |
|:-----------|:-----------|--------------------------:|
| Terminal 1 | Store 1  |                        15 |
| Terminal 1 | Store 2  |                        10 |
| Terminal 1 | Store 4  |                        15 |
| Terminal 1 | Store 5  |                         5 |
| Terminal 1 | Store 7  |                        15 |
| Terminal 2 | Store 10 |                        20 |
| Terminal 2 | Store 11 |                        10 |
| Terminal 2 | Store 5  |                         5 |
| Terminal 2 | Store 6  |                         5 |
| Terminal 2 | Store 7  |                         5 |
| Terminal 2 | Store 8  |                        10 |

### Analysis

Terminal 1 supplied 60 units and Terminal 2 supplied 55 units, so Terminal 1 delivered the larger total.

The lowest-capacity routes include Warehouse 2 → Store 5 (10 units), Warehouse 4 → Store 13 (5 units), and Warehouse 1 → Store 2 (10 units). These constraints create bottlenecks.

Stores 3, 9, 12, 13 and 14 received no goods in the reported solution. Increasing relevant capacities or adding alternative warehouse routes could improve their supply.

Other limitations include the number of warehouse exits, heavy Terminal 2 traffic through Warehouse 4, and missing direct routes to some stores. Potential improvements are additional warehouse-to-store routes, more terminal-to-warehouse links, and better-balanced flows.

## Task 2: OOBTree versus dictionary range queries

The appropriate structure depends on the query. A range query on an attribute other than the key needs an appropriate index. OOBTree is effective when the range concerns its ordered key. Optimize for the actual data and query pattern, and confirm theoretical expectations with measurements.
