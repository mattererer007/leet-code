use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {

        if s.len() != t.len() {
            return false
        } else {
            let mut map_s = HashMap::new();

            for char in s.chars(){
                // checks if these is already an entry and returns the enum(Occupied, Vacant)
                map_s.entry(char)
                // |count| denotes the value to be operated on, *count += 1 derefences the value and performs the operations
                .and_modify(|count| *count += 1)
                // if Vacant, then creates entry of 1
                .or_insert(1);

            }

            for char in t.chars() {

                if map_s.contains_key(&char) {

                    map_s.entry(char)
                    .and_modify(|count| *count -= 1);

                    if map_s.get(&char) == Some(&0) {
                        map_s.remove(&char);
                    }

                } else{
                    return false
                }
            }

            return true

        }
    
    }
}

fn main() {

    let string1 = String::from("rra");
    let string2 = String::from("arr");

    println!("{:?}", Solution::is_anagram(string1, string2));

}