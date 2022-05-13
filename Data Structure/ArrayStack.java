public class ArrayStack<E> implements Stack<E> {
    private static int DefaultSize = 10;
    private int maxSize;
    private int top;
    private E [] listArray;

    public ArrayStack(int size) {
        maxSize = 0;
        top = 0;
        listArray = (E[]) new Object[size];
    }

    public ArrayStack() {
        this(DefaultSize);
    }

    /** Reinitialize the stack. */
    public void clear() {
        maxSize = 0;
        top = 0;
    }

    /** Push and element onto the top of the stack.
     @param it The element being pushed onto the stack. */
    public void push(E it) {
        listArray[top] = it;
        top++;
        maxSize++;
    }

    /** Remove and return the element at the top of the stack.
     @return The element at the top of the stack. */
    public E pop() {
        E ret = listArray[top];
        listArray[top] = null;
        top--;
        maxSize--;
        return ret;
    }

    /** @ return A copy of the top element. */
    public E topValue() {
        return listArray[top-1];
    }

    /** @return The number of elements in the stack. */
    public int length() {
        return maxSize;
    }

    public String toString() {
        String a = "";
        for (int i=0; i<maxSize; i++) {
            a += listArray[i];
            if (i != maxSize-1) {
                a += " ";
            }
        }
        return a;
    }
}