struct Solution;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {

        if prices.len() <= 1 {
            0
        } else {
            // able to do this safely because of the check prior
            // would need a more dynamic solution if unknown variables in list
            let mut min_buy = prices[0];
            let mut max_profit = 0;

            // while I could just do `for price in prices {}...`
            // Using the reference preserves prices for future use
            for &price in &prices {
                if price < min_buy {
                    min_buy = price;
                } else if price - min_buy > max_profit {
                    max_profit = price - min_buy;
                }                
            
            }
            max_profit    
        }
    }
}

fn main() {
    let stock_prices = vec![2,1,2,1,0,1,2];

    let result = Solution::max_profit(stock_prices);

    println!("{:?}", result);


}