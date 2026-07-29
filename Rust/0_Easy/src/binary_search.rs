use std::cmp::Ordering;

struct Solution;


impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {

        if nums.len() == 1 {
            if nums[0] == target {
                return 0;
            } else {
                return -1
            }
        }

        let mut high_bound = nums.len() - 1;
        let mut low_bound = 0;

        while low_bound <= high_bound {

            let pointer = (high_bound + low_bound) / 2;

            match nums[pointer].cmp(&target){
            Ordering::Equal => return pointer as i32,
            Ordering::Less => low_bound = pointer + 1,
            Ordering::Greater => if pointer > 0 {high_bound = pointer - 1} else {return -1},
            }        

        }

        -1
        
    }
}



fn main() {
    
    let nums = vec![2,5];
    let target = 0;

    let result = Solution::search(nums, target);
    println!("{:?}", result);

}