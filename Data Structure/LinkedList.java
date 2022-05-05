public class LinkedList<E> implements List<E> {
    
    Link<E> head, tail;
    int size;

    public LinkedList() {
        head = tail = new Link<E>(null, null);
        size = 0;
    }

    public void clear() {
        head.next = null;
        tail = head;
        size = 0;
    }

    public void insert(int pos, E item) {
        Link<E> curr = head;
        for (int i=0; i<pos; i++) {
            curr = curr.next;
        }

        Link<E> n = new Link<>(item, curr.next);
        curr.next = n;

        if (curr == tail) {
            tail = curr.next;
        }

        size++;
    }

    public void append(E item) {
        Link<E> n = new Link<>(item, null);
        tail.next = n;
        tail = n;
        size++;
    }

    public void update(int pos, E item) {
        Link<E> curr = head;
        for (int i=0; i<pos; i++) {
            curr = curr.next;
        }

        curr.next.item = item;
    }

    public E getValue(int pos) {
        Link<E> curr = head;
        for (int i=0; i<pos; i++) {
            curr = curr.next;
        }
        return curr.next.item;
    }

    public E remove(int pos) {
        Link<E> curr = head;
        for (int i=0; i<pos; i++) {
            curr = curr.next;
        }
        E ret = curr.next.item;

        if (curr.next == tail) {
            tail = curr;
        }

        curr.next = curr.next.next;

        size--;

        return ret;
    }

    public int length() {
        return size;
    }

    public String toString() {
        String a = "";
        Link<E> curr = head;
        for (int i=0;i<size; i++) {
            a += curr.next.item + ", ";
            curr = curr.next;
        }
        return a;
    }

    public static void main(String[] args) {
        List<Integer> mylist = new LinkedList<>();

        mylist.append(3);
        mylist.insert(0, 1);
        mylist.insert(0, 4);
        mylist.append(10);
        mylist.insert(1, 5);
        System.out.println(mylist);
        System.out.println(mylist.length());
//        mylist.clear();
//        System.out.println(mylist.length());

        ListIterator<Integer> itr = mylist.listIterator();
        while(itr.hasNext()) {
            System.out.print(itr.next() + " ");
        }
        System.out.println();
        System.out.println(mylist.length());
    }

//    @Override
//    public ListIterator<E> listIterator() {
//        return new ListIterator<E>() {
//            Link<E> curr = head;
//            @Override
//            public boolean hasNext() {
//                return curr != tail;
//            }
//
//            @Override
//            public E next() {
//                curr = curr.next;
//                return curr.item;
//            }
//
//            @Override
//            public boolean hasPrevious() {
//                return curr != head;
//            }
//
//            @Override
//            public E previous() {
//                Link<E> prev = head;
//                while(prev.next != curr) {
//                    prev = prev.next;
//                }
//                curr = prev;
//                return curr.next.item;
//            }
//        };
//    }

    public ListIterator<E> listIterator() {
        return new LinkedListIterator<>();
    }

    class LinkedListIterator<E> implements ListIterator<E> {

        Link<E> curr = (Link<E>) head;

        public boolean hasNext() {
            return curr != tail;
        }

        public E next() {
            curr = curr.next;
            return curr.item;
        }

        public boolean hasPrevious() {
            return curr != head;
        }

        public E previous() {
            Link<E> tmp = (Link<E>) head;
            while (tmp.next != curr) {
                tmp = tmp.next;
            }

            E ret = curr.item;
            curr = tmp;
            return ret;
        }
    }
}
