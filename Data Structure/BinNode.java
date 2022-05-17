package btree;

public interface BinNode<E> {
	public E element(); // 해당 item을 가지고 옴
	public E setElement(E item); // 해당 element를 설정
	public BinNode<E> left(); // 왼쪽 자식 따라가는 것
	public BinNode<E> right(); // 오른쪽 자식을 따라가는 것
	public boolean isLeaf(); // 리프노트인지 판별
}




