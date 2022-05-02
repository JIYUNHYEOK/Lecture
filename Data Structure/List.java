public interface List<E> { // gerneric 유연하게 선언할때 설정 가능
    public void clear(); // void: return이 없음
    public void insert(int pos, E item);
    public void append(E item);
    public void update(int pos, E item);
    public E getValue(int pos);
    public E remove(int pos); // 지우면서 값을 출력
    public int length();
}