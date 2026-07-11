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
                // returns an or Option<Char> OR could be NONE
                let open = vec.pop();
                // Need on_ref() as it is comparing &c (the location of c) to the char as an object
                // Need to compare apples to apples by setting the location of both and then the values are pulled from there and dereferenced
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
