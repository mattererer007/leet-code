use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut vec: Vec<char> = Vec::new();
        let map = HashMap::from([
            ('}', '{'),
            (']', '['),
            (')', '('),
        ]);

        for c in s.chars(){
            if map.contains_key(&c) {
                let open = vec.pop();
                if map.get(&c) == open.as_ref() {
                    continue;
                } else {
                    return false;
                }
            } else {
                vec.push(c);
            }
        }

        vec.is_empty()
        
    }
}


fn main() {

    let s = String::from("()[]{}");

    let result = Solution::is_valid(s);
    println!("{:?}", result);

}
