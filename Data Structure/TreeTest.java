package btree;

public class TreeTest {
	public static void main(String[] args) {
		
		BinNode<String> d = new INode<>("D", null, null);
		BinNode<String> g = new INode<>("G", null, null);
		BinNode<String> h = new INode<>("H", null, null);
		BinNode<String> i = new INode<>("I", null, null);
		BinNode<String> j = new INode<>("J", null, null);
		
		BinNode<String> b = new INode<>("B", j, d);
		BinNode<String> e = new INode<>("E", g, null);
		BinNode<String> f = new INode<>("F", h, i);
		
		BinNode<String> c = new INode<>("C", e, f);
		BinNode<String> a = new INode<>("A", b, c);
		
//		System.out.println(a.right().left().left().element());
//		System.out.println(a.right().right().left().element());
		
		preorder(a); // ABDCEGFHI
		System.out.println();
		inorder(a);
		System.out.println();
		postorder(a);
	}
	
	static public <E> void preorder(BinNode<E> rt) {
		if (rt == null) return;
		System.out.print(rt.element()); // visit
		preorder(rt.left());
		preorder(rt.right());
	}
	
	static public <E> void inorder(BinNode<E> rt) {
		if (rt == null) return;
		inorder(rt.left());
		System.out.print(rt.element()); // visit
		inorder(rt.right());
	}
	
	static public <E> void postorder(BinNode<E> rt) {
		if (rt == null) return;
		postorder(rt.left());
		postorder(rt.right());
		System.out.print(rt.element()); // visit
	}
}
