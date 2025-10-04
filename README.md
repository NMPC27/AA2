
# Randomized Algorithm for the Minimum Weight Dominating Set

This project implements a **randomized algorithm** to approximate the **Minimum Weight Dominating Set (MWDS)** in an undirected weighted graph.  
It provides a heuristic solution that balances **execution time** and **solution quality**, making it a practical alternative to exhaustive search for large instances of NP-hard problems.



##  Project Overview

A **Minimum Weight Dominating Set (MWDS)** of a graph G(V,E)G(V, E)G(V,E) is a subset of vertices such that:

-   Every vertex in the graph either belongs to this subset or is adjacent to at least one vertex in it.
    
-   The sum of the vertex weights in the subset is **as small as possible**.
    

This project presents a **randomized heuristic** approach that generates and evaluates random subsets of vertices to find an approximate solution faster than traditional exhaustive methods.



##  Methodology

1.  **Random Subset Generation:**
    
    -   The algorithm starts by generating random subsets of vertices (initially with half the size of the graph).
        
    -   Each subset is tested to determine if it forms a dominating set.
        
2.  **Adaptive Subset Sizing:**
    
    -   If a dominating set is found, smaller subsets are tested.
        
    -   If not, larger subsets are used until a dominating set is found.
        
3.  **Evaluation and Refinement:**
    
    -   The algorithm avoids re-analyzing previously tested subsets.
        
    -   It continues refining until a near-optimal MWDS is found.
        

This approach significantly reduces computation time compared to the exhaustive search while maintaining acceptable accuracy.



##  Computational Complexity

-   **Best Case:** Between quadratic and cubic — O(n^2)   to O(n^3)
    
-   **Worst Case:** Cubic — O(n^3)
    

The algorithm’s efficiency depends on the **graph density**:

-   Higher density → faster results (easier to find dominating sets).
    
-   Lower density → slower performance (fewer connections).
    



##  Experimental Results

Results are available in the **`RandomSearch.xlsx`** file, which includes:

-   Number of vertices and edges
    
-   Graph density (0%, 12.5%, 25%, 50%, 75%, 100%)
    
-   Computations, operations, time taken, and resulting weights
    
-   Comparative plots and tables
    

**Accuracy Observations:**

-   Best performance at **lower densities (12.5–25%)** with relative error under 25%.
    
-   Accuracy decreases as density increases (more possible dominating sets).
    



##  Key Findings

-   **Trade-off achieved** between speed and accuracy.
    
-   **Random search** is far faster than exhaustive search but may not always return the optimal MWDS.
    
-   For large instances of NP-hard problems, this method provides **feasible, near-optimal solutions** in practical time.
    
-   Complexity verified empirically to match the formal analysis (O(n²–n³)).
    



##  Estimated Execution Time

-   **Worst Case (0% density):** grows by ≈ 3% per additional vertex
    
-   **Example:**
    
    -   100 vertices → ~1682 s
        
    -   200 vertices → ~32326 s (~9 hours)
        
-   **Best Case (100% density):** grows by ≈ 2% per additional vertex
    



##  Files


|File|Description|
|----------------|-------------------------------|
|`main.py` |Implementation of the randomized MWDS algorithm|
|`RandomSearch.xlsx`|Experimental data and performance charts|
|`report.pdf`|Full technical report and analysis|



##  Conclusion

The **randomized search algorithm** provides an efficient heuristic for solving the MWDS problem.  
While it may not always find the optimal solution, it achieves a close approximation much faster than exhaustive search, making it well-suited for **large-scale or time-sensitive applications**.



##  Reference

> [1] _Hybrid metaheuristic algorithms for minimum weight dominating set_, ScienceDirect, Nov 2022.  
> [Link](https://www.sciencedirect.com/science/article/pii/S1568494612003092)
    



##  Author

**Nuno Cunha** – Student ID 98124  
2rd Project: Randomized Algorithm for the Minimum Weight Dominating Set
