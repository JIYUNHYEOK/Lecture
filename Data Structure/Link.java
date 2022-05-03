public class Link<E> {
    E item;
    Link<E> next;

    public Link(E item, Link<E> next) {
        this.item = item;
        this.next = next;
    }
}
