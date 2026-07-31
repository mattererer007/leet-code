// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}

struct Solution;

impl Solution {
    pub fn merge_two_lists(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut list1 = list1;
        let mut list2 = list2;

        let mut dummy = ListNode::new(0);
        let mut current = &mut dummy;

        while list1.is_some() && list2.is_some() {
            let val1 = list1.as_ref().unwrap().val;
            let val2 = list2.as_ref().unwrap().val;

            if val1 <= val2 {
                current.next = Some(Box::new(ListNode::new(val1)));
                list1 = list1.unwrap().next;
            } else {
                current.next = Some(Box::new(ListNode::new(val2)));
                list2 = list2.unwrap().next;
            }

            current = current.next.as_mut().unwrap();
        }

        if list1.is_some() {
            current.next = list1;
        } else {
            current.next = list2;
        }

        dummy.next
    }
}


fn main() {
  
  let linkedlist1 = Some(Box::new(ListNode{val: 1, next: Some(Box::new(ListNode { val: 2, next: Some(Box::new(ListNode { val: 3, next: None }))}))}));

  let node1 = ListNode {val: 4, next: None};
  let node2 = ListNode {val: 3, next: Some(Box::new(node1))};
  let linkedlist2 = Some( Box::new(ListNode {val: 1, next: Some(Box::new(node2))}));

  let result = Solution::merge_two_lists(linkedlist1, linkedlist2);

  let mut current = &result;
  while let Some(node) = current{
    println!("{}", node.val);
    current = &node.next;
  }

}