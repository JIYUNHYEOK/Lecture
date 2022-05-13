public class LinkedQueue<E> implements Queue<E> {
    private Link<E> front;
    private int size;

    public LinkedQueue() {
        front = new Link<E>(null, null);
        size = 0;
    }

    public void clear() {
        front.next = null;
        front = null;
        size = 0;
    }

    public void enqueue(E it) {
        Link<E> curr = front;
        for (int i=0; i<size; i++) {
            curr = curr.next;
        }

        curr.next = new Link<E>(it, null);
        curr = curr.next;
        size++;
    }

    public E dequeue() {
        E ret = front.next.item; // 가장 앞의 값은 null값으로 front를 지정
        front = front.next;
        size--;
        return ret;
    }

    public E frontValue() {
        return front.next.item;
    }

    public int length() {
        return size;
    }

    public String toString() {
        String a = "";
        Link<E> curr = front;
        for (int i=0;i<size; i++) {
            a += curr.next.item;
            if (i != size-1) {
                a += " ";
            }
            curr = curr.next;
        }
        return a;
    }
}