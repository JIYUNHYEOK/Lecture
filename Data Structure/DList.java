public class DList<E> implements List<E> {

    DLink<E> head, tail;
    int size;

    public DList() {
        head = new DLink<E>(null, null, null); // item, prev, next
        tail = new DLink<E>(null, head, null); // item, prev, next
        head.setNext(tail);
        size = 0;
    }

    public void clear() {
        head.setNext(tail);
        tail.setPrev(head);
        size = 0;
    }

    public void insert(int pos, E item) {
        DLink<E> curr = head;
        for (int i=0; i<pos; i++) {
            curr = curr.next();
        }

        curr.setNext(new DLink<E>(item, curr, curr.next())); // item, prev, next
        curr.next().next().setPrev(curr.next()); // curr 뒤에 삽입
        size++;
    }

    public void append(E item) {
        tail.prev().setNext(new DLink<E>(item, tail.prev(), tail)); // tail 전에 새로운 값 삽입
        tail.setPrev(tail.prev().next()); // tail의 prev 변경
        size++;
    }

    public void update(int pos, E item) {
        DLink<E> curr = head;
        for (int i=0; i<pos; i++) {
            curr = curr.next();
        }

        curr.next().setItem(item);
    }

    public E getValue(int pos) {
        DLink<E> curr = head;
        for (int i=0; i<pos; i++) {
            curr = curr.next();
        }
        return curr.next().item();
    }

    public E remove(int pos) {
        DLink<E> curr = head;
        for (int i=0; i<pos; i++) {
            curr = curr.next();
        }
        E ret = curr.next().item();
        curr.setNext(curr.next().next());
        curr.next().setPrev(curr);
        size--;

        return ret;
    }

    public int length() {
        return size;
    }

    public String toString() {
        String a = "";
        DLink<E> curr = head;
        for (int i=0; i<size; i++) {
            a += curr.next().item() + ", ";
            curr = curr.next();
        }
        return a;
    }

    @Override
    public ListIterator<E> listIterator() {
        return new ListIterator<E>() {
            DLink<E> curr = head;
            @Override
            public boolean hasNext() {
                return curr != tail;
            }

            @Override
            public E next() {
                curr = curr.next();
                return curr.item();
            }

            @Override
            public boolean hasPrevious() {
                return curr != head;
            }

            @Override
            public E previous() {
                curr = curr.prev();
                return curr.next().item();
            }
        };
    }

    public static void main(String[] args) {
        List<Integer> mylist = new DList<>();

        mylist.append(3);
        System.out.println(mylist);
        mylist.insert(0, 1);
        System.out.println(mylist);
        mylist.insert(0, 4);
        System.out.println(mylist);
        mylist.append(10);
        mylist.insert(1, 5);
        System.out.println(mylist);
        mylist.remove(1);
        System.out.println(mylist);
        mylist.update(0,9);
        System.out.println(mylist);
        System.out.println(mylist.length());
//        mylist.clear();
//        System.out.println(mylist.length());

        ListIterator<Integer> itr = mylist.listIterator();
        while(itr.hasNext()) {
            System.out.print(itr.next() + " ");
        }
        System.out.println();
        while(itr.hasPrevious()) {
            System.out.print(itr.previous() + " ");
        }
        System.out.println(mylist.length());
    }
}
