
/* Hidden stub code will pass a root argument to the function below. Complete the function to solve the challenge. Hint: you may want to write one or more helper functions.

The Node class is defined as follows:
    class Node {
        int data;
        Node left;
        Node right;
     }
*/
    boolean checkBST(Node root) {
        int min = -1;
        int max = 10001;
        boolean output =  helper(root, min, max);
        System.out.println(output);
        return output;
    }

    boolean helper(Node root, int min, int max) {
        if (root == null) {
            return true;
        }
        else if (root.data > min && root.data < max) {
            return (true && helper(root.left, min, root.data) && helper(root.right, root.data, max));
        } else {
            return false;
        }
    }
