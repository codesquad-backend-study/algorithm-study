package programmers.sully.week38;

import java.util.*;

class Node {

    int x;
    int y;
    int index;
    Node left;
    Node right;

    public Node(int x, int y, int index) {
        this.x = x;
        this.y = y;
        this.index = index;
        this.left = null;
        this.right = null;
    }

}

class BinaryTree {

    Node root;
    List<Integer> preAnswer;
    List<Integer> postAnswer;

    public BinaryTree() {
        this.root = null;
        this.preAnswer = new ArrayList<>();
        this.postAnswer = new ArrayList<>();
    }

    public Node insert(Node parent, Node current) {
        // 처음을 위해서만 해주는 것 (위에 아무것도 없으니)
        if (parent == null) {
            parent = current;
        }

        // 현재 노드가 부모 노드보다 왼쪽에 존재한다면, 현재 노드는 당연히 부모 노드보다 왼쪽에 위치함
        if (current.x < parent.x) {
            parent.left = insert(parent.left, current);
        } else if (current.x > parent.x) {
            parent.right = insert(parent.right, current);
        }

        return parent;
    }

    public void create(List<Node> nodeList) {
        for (Node node : nodeList) {
            root = insert(root, node);
        }
    }

    public void preorder(Node current) {
        preAnswer.add(current.index);

        if (current.left != null) {
            preorder(current.left);
        }

        if (current.right != null) {
            preorder(current.right);
        }
    }

    public void postorder(Node current) {
        if (current.left != null) {
            postorder(current.left);
        }

        if (current.right != null) {
            postorder(current.right);
        }

        postAnswer.add(current.index);
    }

}

class Solution {

    public int[][] solution(int[][] nodeinfo) {
        int[][] answer = new int[2][nodeinfo.length];
        List<int[]> newNodeinfo = new ArrayList<>();

        for (int i = 0; i < nodeinfo.length; i++) {
            int currentX = nodeinfo[i][0];
            int currentY = nodeinfo[i][1];
            newNodeinfo.add(new int[]{currentX, currentY, i + 1});
        }

        newNodeinfo.sort((a, b) -> Integer.compare(b[1], a[1]));

        List<Node> nodeList = new ArrayList<>();
        for (int[] newNode : newNodeinfo) {
            nodeList.add(new Node(newNode[0], newNode[1], newNode[2]));
        }

        BinaryTree binaryTree = new BinaryTree();
        binaryTree.create(nodeList);
        binaryTree.preorder(binaryTree.root);
        binaryTree.postorder(binaryTree.root);

        for (int i = 0; i < binaryTree.preAnswer.size(); i++) {
            answer[0][i] = binaryTree.preAnswer.get(i);
            answer[1][i] = binaryTree.postAnswer.get(i);
        }

        return answer;
    }

}

class FindDirection {

    public static void main(String[] args) {
        int[][] nodeinfo = {{5, 3}, {11, 5}, {13, 3}, {3, 5}, {6, 1}, {1, 3}, {8, 6}, {7, 2}, {2, 2}};
        Solution s = new Solution();
        System.out.println(Arrays.deepToString(s.solution(nodeinfo)));
    }

}
