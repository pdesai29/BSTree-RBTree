# BSTree-RBTree
<h3>C++ implementations of The Binary-Search Tree vs Red-Black Tree</h3>
<h3>The goal of the project is to calculate and compare the insert and traverse time of The Binary-Search Tree vs Red-Black Tree (Self Balancing Tree)</h3>
<p></p>
<h2> 🏃‍♂️ Run </h2>
<p>1: 'make' - will generate executable 'trees'</p>
<p>2: './trees' - trees expects three command line arguments "[n] [direction] [tree]"</p>

1. `[n]`
   - Input size (number of nodes in the tree)
2. `[direction]`
   - `-1`: Input is sorted in descending order
   - `1`: Input is sorted in ascending order
   - `0`: Input is random
3. `[tree]`
   - `0`: Using binary search tree (BST)
   - `1`: Using red-black tree (RB tree)


<p>Example: `./trees 50 0 0` will generate 50 random numbers and insert them in BST and run BST in order traversal</p>

<p></p>
<h2> 🧪 Tests </h2>
<p>The test file is written python</p>
<h3>Run : python3 automate.py</h3>
<p>It will run the 'trees' executable for these 'n=[50000, 100000, 250000, 500000, 1000000, 2500000, 5000000]' many nodes</p>
<p>and in each direction 'dir=[-1,0,1]' for 10 times each and </p>
<p>will write the results of each execution and an average of 10 execution times in bs_tree.txt and rb_tree.txt </p>
<p>Check out bs_tree.txt and rb_tree.txt files under tests folder for more info</p>
<h2> ‼ Warning ‼ </h2>
<p>The test won't run for BST if the number of nodes is > 100000 and the direction is -1 or 1 </p>
<p>Because sorted and reverse sorted values generate skew trees </p>
<p> It was able to perform insertion for sorted and reverse-sorted data but it 
wasn’t able to traverse the tree because the convert method uses another method called 
“inorder_Traverse(rb_tree_node* x, int* array)” which is recursive method, and if tree is 
unbalanced the call stack will be filled with the height of the tree which exceeded the capacity of my 
laptop and I got an error while running the convert method for the number of nodes>100000.</p>



