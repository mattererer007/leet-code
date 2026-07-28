

struct Solution;

impl Solution {
    pub fn is_palindrome(s: String) -> bool {


        let mut list: Vec<char> = Vec::new();
        let lowercase_s = s.to_lowercase();


        for c in lowercase_s.chars(){   
            if c.is_ascii_alphanumeric(){
                list.push(c);
            }
        }

        if list.len() <= 1 {
            return true;
        } else {
            let mut back_cursor = list.len()-1;
            let mut forward_cursor = 0;

            while forward_cursor <= back_cursor {
                if list[forward_cursor] == list[back_cursor]{
                    forward_cursor += 1;
                    back_cursor -= 1;
                } else {
                    return false;
                }

            }
        }
        true

        
    }
}


fn main() {

    let test_string = String::from("aa");

    let result = Solution::is_palindrome(test_string);

    println!("{:?}", result);

}
