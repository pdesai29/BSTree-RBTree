/////////////////////// PRANAY //////////////////////////////
// 1)
// bs_tree
// implemented
// constructor , destructor , remove_all {for releasing memory}
// insert
// convert , inorder_Traverse(bs_tree_node* x, int* array) {helper for convert}
// output (prints tree in BFS form)
// inorder_output(bs_tree_node* x, int level) {prints tree in DFS form}

#include "bs_tree.h"
#include <list>
#include <iostream>
#include <string>

using namespace std;
int counterBS = 0;

bs_tree::bs_tree()
{
    T_nil = new bs_tree_node;
    T_nil->key = 0;
    T_nil->left = T_nil;
    T_nil->right = T_nil;
    T_nil->p = T_nil;
    T_root = T_nil;
}

bs_tree::~bs_tree()
{
    remove_all(T_root);
    delete T_nil;
}

void bs_tree::insert(int key, bs_tree_i_info &t_info)
{
    bs_tree_node *y = T_nil;
    bs_tree_node *x = T_root;

    while (x != T_nil)
    {
        y = x;

        if (key < x->key)
        {
            x = x->left;
        }
        else if (key > x->key)
        {
            x = x->right;
        }

        // 1) if (k == x->key) returning without inserting and incrementing t_info.i_duplicate
        else
        {
            // cout << "duplicate key:" << key << endl;
            t_info.i_duplicate++;
            return;
        }
    }

    bs_tree_node *z = new bs_tree_node;
    z->key = key;
    z->left = T_nil;
    z->right = T_nil;
    z->p = y;

    if (y == T_nil)
    {
        T_root = z;
    }
    else if (key < y->key)
    {
        y->left = z;
    }
    else
    {
        y->right = z;
    }
}

// helper for convert
void bs_tree::inorder_Traverse(bs_tree_node *x, int *array)
{
    if (x != T_nil)
    {
        inorder_Traverse(x->left, array);
        array[counterBS] = x->key;
        counterBS++;
        inorder_Traverse(x->right, array);
    }
}

// 2) convert method which returns new number of nodes
int bs_tree::convert(int *array, int n)
{
    inorder_Traverse(T_root, array);
    n = counterBS;
    return n;
}

void bs_tree::remove_all(bs_tree_node *x)
{   /*<<<*/
    /*
     * recursively remove all tree elements
     */
    if (x != T_nil)
    {
        remove_all(x->left);
        remove_all(x->right);

        delete x;
    }
}

// output prints tree in BFS form
void bs_tree::output(bs_tree_node *x, int r_level)
{
    list<pair<bs_tree_node *, int>> l_nodes;
    pair<bs_tree_node *, int> c_node;
    int c_level;

    c_level = r_level;
    l_nodes.insert(l_nodes.end(), pair<bs_tree_node *, int>(x, r_level));
    cout << "Printing tree in BFS order:" << endl;
    while (!l_nodes.empty())
    {
        c_node = *(l_nodes.begin());

        if (c_level < c_node.second)
        {
            cout << endl;
            c_level = c_node.second;
        }

        cout << "(" << c_node.first->key;

        if (c_node.first->p == T_nil)
            cout << ",ROOT) ";
        else
            cout << ",P:" << c_node.first->p->key << ") ";

        if (c_node.first->left != T_nil)
            l_nodes.insert(l_nodes.end(), pair<bs_tree_node *, int>(c_node.first->left,
                                                                    c_node.second + 1));
        if (c_node.first->right != T_nil)
            l_nodes.insert(l_nodes.end(), pair<bs_tree_node *, int>(c_node.first->right,
                                                                    c_node.second + 1));
        l_nodes.erase(l_nodes.begin());
    }

    cout << endl;
}

// inorder_output print tree in in-order form
void bs_tree::inorder_output(bs_tree_node *x, int level)
{

    if (x != T_nil)
    {
        inorder_output(x->left, level + 1);
        cout << "(" << x->key << "," << level << ")" << endl;
        inorder_output(x->right, level + 1);
    }
}
