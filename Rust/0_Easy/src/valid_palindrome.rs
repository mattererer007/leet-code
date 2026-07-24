

struct Solution;

impl Solution {
    pub fn is_palindrome(s: String) -> bool {

        let mut forward = String::new();
        let mut backward = String::new();

        for c in s.chars() {
            if c.is_ascii_alphanumeric() {
                // convert the char to lowercase via an iterator (to_lowercase)
                // .next() pulls the first item which will be the character as there is only 1 item 
                // .map(|char| ...) checks if there is anything via .next() and if so then adds to string
                c.to_lowercase().next().map(|c| forward.push(c));
                c.to_lowercase().next().map(|c| backward.insert(0,c));
            } 
        }

        println!("{}\n", forward);
        println!("{}", backward);

        forward == backward

        
    }
}


fn main() {

    let test_string = String::from("A man, a plan, a canal: Panama");

    let result = Solution::is_palindrome(test_string);

    println!("{:?}", result);

}
