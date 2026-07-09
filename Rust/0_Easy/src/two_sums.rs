struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        // i32 auto copies so can be referenced multiple times
        
        for (i, &number) in nums.iter().enumerate(){ // nums.iter() gives you: (usize, &i32)
            // need the & to dereference it to the actual i32 for comparison            
            let complement = target - number;
            // .iter() borrows a vector enabling looping with the vec being cleared from memory
            for (j, &other_number) in nums.iter().enumerate(){
                if complement == other_number && j != i {
                    return vec![i as i32, j as i32]
                }
            }
        }

        vec![]
    }
}


fn main() {

    let nums = vec![1,2,10,5,-1];
    let target = 7;

    let result = Solution::two_sum(nums, target);
    println!("{:?}", result);

}
