public class TestAll {
    public static void main(String[] args) {
        // 1. DList
        List<Integer> mylist = new DList<>();

        System.out.println("1. DList");
        System.out.println("append를 이용한 값 3 추가");
        mylist.append(3);
        System.out.println(mylist);
        System.out.println("insert를 이용한 값 0번 인덱스에 1 추가");
        mylist.insert(0, 1);
        System.out.println(mylist);
        System.out.println("insert를 이용한 값 0번 인덱스에 4 추가");
        mylist.insert(0, 4);
        System.out.println(mylist);
        System.out.println("append를 이용한 값 10 추가");
        mylist.append(10);
        System.out.println(mylist);
        System.out.println("insert를 이용한 값 1번 인덱스에 5 추가");
        mylist.insert(1, 5);
        System.out.println(mylist);
        System.out.println("remove를 이용한 값 1번 인덱스값 제거");
        mylist.remove(1);
        System.out.println(mylist);
        System.out.println("update를 이용한 값 0번 인덱스값 9로 변경");
        mylist.update(0,9);
        System.out.println(mylist);
        System.out.println("length를 이용한 값 길이출력");
        System.out.println(mylist.length());
//        System.out.println("clear를 이용한 초기화");
//        mylist.clear();
//        System.out.println(mylist.length());

        ListIterator<Integer> itr = mylist.listIterator();
        System.out.println("listIterator를 이용한 다음값 접근");
        while(itr.hasNext()) {
            System.out.print(itr.next() + " ");
        }
        System.out.println();
        System.out.println("listIterator를 이용한 이전값 접근");
        while(itr.hasPrevious()) {
            System.out.print(itr.previous() + " ");
        }
        System.out.println();
        System.out.println("clear를 이용한 초기화");
        mylist.clear();
        System.out.println(mylist.length());

        // 2. ArrayStack
        Stack<Integer> arrayStack = new ArrayStack<>();
        System.out.println();
        System.out.println();
        System.out.println("2. ArrayStack");
        System.out.println("0부터 4까지 push를 이용해 값 추가");
        for(int i=0; i<5; i++) {
            arrayStack.push(i);
        }
        System.out.println(arrayStack);
        System.out.println("pop을 이용한 제일 마지막 값 제거");
        arrayStack.pop();
        System.out.println(arrayStack);
        System.out.println("topValue를 이용한 top 출력");
        System.out.println(arrayStack.topValue());
        System.out.println("length를 이용한 길이 출력");
        System.out.println(arrayStack.length());
        System.out.println("clear를 이용한 초기화");
        arrayStack.clear();
        System.out.println(arrayStack.length());

        // 3. LinkedQueue
        Queue<Integer> linkedQueue = new LinkedQueue<>();
        System.out.println();
        System.out.println();
        System.out.println("3. LinkedQueue");
        System.out.println("0부터 4까지 enqueue를 이용해 값 추가");
        for (int i=0; i<5; i++) {
            linkedQueue.enqueue(i);
        }
        System.out.println(linkedQueue);
        System.out.println("frontValue 이용해 제일 앞의 값 출력");
        System.out.println(linkedQueue.frontValue());
        System.out.println("dequeue를 이용해 제일 앞의 값 제거");
        System.out.println(linkedQueue.dequeue());
        System.out.println("dequeue를 이용해 제일 앞의 값 제거 확인");
        System.out.println(linkedQueue);
        System.out.println("dequeue를 이용해 제일 앞의 값 제거");
        System.out.println(linkedQueue.dequeue());
        System.out.println("dequeue를 이용해 제일 앞의 값 제거 확인");
        System.out.println(linkedQueue);
        System.out.println("length를 이용한 길이 출력");
        System.out.println(linkedQueue.length());
        System.out.println("clear를 이용한 초기화");
        linkedQueue.clear();
        System.out.println(linkedQueue.length());
    }


}