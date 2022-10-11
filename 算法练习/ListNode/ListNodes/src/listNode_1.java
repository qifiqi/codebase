public class listNode_1 {

    static class ListNode {
        int val;
        ListNode next;

        public ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public static ListNode reverseList(ListNode head){
        if (head==null || head.next==null){
            return head;
        }
        ListNode p = reverseList(head.next);
        head.next.next=head;
        head.next=null;
        return p;
    }

    public static ListNode iterate(ListNode head) {
        ListNode pave=null, next;
        ListNode curr = head;
        while (curr != null) {
            next = curr.next;
            curr.next = pave;
            pave = curr;
            curr = next;
        }
        return pave;
    }

    public static void main(String[] args) {
        ListNode node5 = new ListNode(5, null);
        ListNode node4 = new ListNode(4, node5);
        ListNode node3 = new ListNode(3, node4);
        ListNode node2 = new ListNode(2, node3);
        ListNode node1 = new ListNode(1, node2);
//        ListNode prev  = iterate(node1);
//        System.out.println(prev);
        ListNode prev1 = reverseList(node1);
        System.out.println(prev1);
    }
}
