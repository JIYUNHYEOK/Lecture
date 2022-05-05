import java.util.Arrays;

public class ArrayList<E> implements List<E> {
    private static int DefaultSize = 10;
    private E[] data;
    private int listSize;

    public ArrayList(){
        this(DefaultSize);
    }

    public ArrayList(int size){
        listSize = 0;
        data = (E[]) new Object[size];
    }

    public void clear() {
        listSize = 0;
    }

    public void insert(int pos, E item) {
        for (int i=listSize; i>pos; i--) {
            data[i] = data[i-1];
        }
        data[pos] = item;
        listSize++;
    }

    public void append(E item) {
        // data[listSize] = item;
        // listSize += 1;
        data[listSize++] = item;
    }


    public void update(int pos, E item) {
        data[pos] = item;
    }

    public E getValue(int pos) {
        return data[pos];
    }

    public E remove(int pos) {
        E ret = data[pos];
        listSize--;


        for (int i=pos; i<listSize; i++) {
            data[i] = data[i+1];
        }

        return ret;
    }

    public int length() {
        return listSize;
    }

    public String toString() {
        String a = "";
        for (int i = 0; i < listSize; i++) {
            a += data[i] + ", ";
        }
        return a;
    }

    public static void main(String[] args) {

        ArrayList<Integer> mylist = new ArrayList<>();
        // mylist.append(3);
        // System.out.println(Arrays.toString(mylist.data));
        // mylist.append(5);
        // System.out.println(Arrays.toString(mylist.data));
        // mylist.insert(0, 10);
        // System.out.println(Arrays.toString(mylist.data));
        // mylist.remove(2);
        // System.out.println(Arrays.toString(mylist.data));
        mylist.append(3);
        mylist.append(5);
        mylist.append(6);
        mylist.append(7);
        mylist.append(8);
        mylist.append(9);
        System.out.println(Arrays.toString(mylist.data));


        ListIterator<Integer> itr = mylist.listIterator();
        while(itr.hasNext()) {
            System.out.print(itr.next() + " ");
        }

        System.out.println(mylist.length());
    }

    public ListIterator<E> listIterator() {
        return new ListIterator<E>() {

            int pos = 0;

            public boolean hasNext() { return pos < listSize; }

            public E next() { return data[pos++]; }

            public boolean hasPrevious() { return pos>0; }

            public E previous() { return data[--pos]; }
        };
    }

}
