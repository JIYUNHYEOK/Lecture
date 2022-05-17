package btree;

public interface BinNode<E> {
	public E element(); // �ش� item�� ������ ��
	public E setElement(E item); // �ش� element�� ����
	public BinNode<E> left(); // ���� �ڽ� ���󰡴� ��
	public BinNode<E> right(); // ������ �ڽ��� ���󰡴� ��
	public boolean isLeaf(); // ������Ʈ���� �Ǻ�
}




