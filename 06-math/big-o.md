# Big-O

From best to worst:
1. O(1): A **constant-time** algorithm does not depend on input size.
2. O(logn): A **logarithmic** algorithms halves the input time at every step.
3. O(n): A **linear** algorithm iterates through input a constant "n" number of times.
4. O(n logn): Usually for sorting.
5. O(n^2): A **quadratic** algorithm contains nested loops.
6. O(n^2 logn)
7. O(n^3)
8. O(2^n): Usually for iterating through all subsets.
9. O(n!): Usually for iterating all permutations.

Note: An exponential function a^n where a > 1 grows faster than any polynomial n^b where b is any constant.

<table>
  <tbody>
    <tr>
      <th>Data Structure</th>
      <th colspan="8">Time Complexity</th>
      <th>Space Complexity</th>
    </tr>
    <tr>
      <th></th>
      <th colspan="4">Average</th>
      <th colspan="4">Worst</th>
      <th>Worst</th>
    </tr>
    <tr>
      <th></th>
      <th>Access</th>
      <th>Search</th>
      <th>Insertion</th>
      <th>Deletion</th>
      <th>Access</th>
      <th>Search</th>
      <th>Insertion</th>
      <th>Deletion</th>
      <th></th>
    </tr>
    <tr>
      <td><a href="01-arrays-and-strings">Array</a></td>
      <td style="color:green">O(1)</td>
      <td style="color:#CCCC00" colspan="3">O(n)</td>
      <td style="color:green">O(1)</td>
      <td style="color:#CCCC00" colspan="4">O(n)</td>
    </tr>
    <tr>
      <td><a href="02-linked-lists">Linked List</a></td>
      <td style="color:#CCCC00" colspan="2">O(n)</td>
      <td style="color:green" colspan="2">O(1)</td>
      <td style="color:#CCCC00" colspan="2">O(n)</td>
      <td style="color:green" colspan="2">O(1)</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td><a href="03-stacks-and-queues">Stack</a></td>
      <td style="color:#CCCC00" colspan="2">O(n)</td>
      <td style="color:green" colspan="2">O(1)</td>
      <td style="color:#CCCC00" colspan="2">O(n)</td>
      <td style="color:green" colspan="2">O(1)</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td><a href="03-stacks-and-queues">Queue</a></td>
      <td style="color:#CCCC00" colspan="2">O(n)</td>
      <td style="color:green" colspan="2">O(1)</td>
      <td style="color:#CCCC00" colspan="2">O(n)</td>
      <td style="color:green" colspan="2">O(1)</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td>Hash Table</td>
      <td style="color:gray">N/A</td>
      <td style="color:green" colspan="3">O(1)</td>
      <td style="color:gray">N/A</td>
      <td style="color:#CCCC00" colspan="4">O(n)</td>
    </tr>
    <tr>
      <td><a href="04-trees-and-graphs">Binary Search Tree</a></td>
      <td style="color:#9acd32" colspan="4">O(log(n))</td>
      <td style="color:#CCCC00" colspan="5">O(n)</td>
    </tr>
  </tbody>
</table>

<table class="table table-bordered table-striped">
  <tbody>
    <tr>
      <th>Algorithm</th>
      <th colspan="3">Time Complexity</th>
      <th>Space Complexity</th>
    </tr>
    <tr>
      <th></th>
      <th>Best</th>
      <th>Average</th>
      <th>Worst</th>
      <th>Worst</th>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Quicksort">Quicksort</a></td>
      <td style="color:orange">Ω(n log(n))</td>
      <td style="color:orange">Θ(n log(n))</td>
      <td style="color:red">O(n^2)</td>
      <td style="color:#9acd32">O(log(n))</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Merge_sort">Mergesort</a></td>
      <td style="color:orange">Ω(n log(n))</td>
      <td style="color:orange">Θ(n log(n))</td>
      <td style="color:orange">O(n log(n))</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Heapsort">Heapsort</a></td>
      <td style="color:orange">Ω(n log(n))</td>
      <td style="color:orange">Θ(n log(n))</td>
      <td style="color:orange">O(n log(n))</td>
      <td style="color:green">O(1)</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Bubble_sort">Bubble Sort</a></td>
      <td style="color:#CCCC00">Ω(n)</td>
      <td style="color:red">Θ(n^2)</td>
      <td style="color:red">O(n^2)</td>
      <td style="color:green">O(1)</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Insertion_sort">Insertion Sort</a></td>
      <td style="color:#CCCC00">Ω(n)</td>
      <td style="color:red">Θ(n^2)</td>
      <td style="color:red">O(n^2)</td>
      <td style="color:green">O(1)</td>
    </tr>
    <tr>
      <td><a rel="tooltip" title="Constant number of digits 'k'" href="http://en.wikipedia.org/wiki/Radix_sort">Radix Sort</a></td>
      <td style="color:green">Ω(nk)</td>
      <td style="color:green">Θ(nk)</td>
      <td style="color:green">O(nk)</td>
      <td style="color:#CCCC00">O(n+k)</td>
    </tr>
  </tbody>
</table>