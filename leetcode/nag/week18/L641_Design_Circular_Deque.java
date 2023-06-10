import java.util.Arrays;

class MyCircularDeque {

    private final int[] deque;
    private final int length;
    private int front = 0;
    private int rear = 0;

    public MyCircularDeque(int k) {
        this.deque = new int[k];
        for (int i = 0; i < deque.length; i++) {
            deque[i] = -1;
        }
        this.length = k;
    }
    
    public boolean insertFront(int value) {
        if (isFull()) {
            return false;
        }
        front = (front - 1 + length) % length;
        deque[front] = value;
        return true;
    }
    
    public boolean insertLast(int value) {
        if (isFull()) {
            return false;
        }
        deque[rear] = value;
        rear = (rear + 1 + length) % length;
        return true;
    }
    
    public boolean deleteFront() {
        if (isEmpty()) {
            return false;
        }
        deque[front] = -1;
        front = (front + 1 + length) % length;
        return true;
    }
    
    public boolean deleteLast() {
        if (isEmpty()) {
            return false;
        }
        rear = (rear - 1 + length) % length;
        deque[rear] = -1;
        return true;
    }
    
    public int getFront() {
        if (isEmpty()) {
            return -1;
        }
        return deque[front];
    }
    
    public int getRear() {
        if (isEmpty()) {
            return -1;
        }
        return deque[(rear - 1 + length) % length];
    }
    
    public boolean isEmpty() {
        if ((rear == front) && deque[front] == -1) {
            return true;
        }
        return false;
    }
    
    public boolean isFull() {
        if ((rear == front) && deque[front] != -1) {
            return true;
        }
        return false;
    }


}
