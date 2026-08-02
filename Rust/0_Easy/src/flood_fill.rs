use std::collections::{HashSet, VecDeque};


struct Solution;

impl Solution {
    pub fn flood_fill(image: Vec<Vec<i32>>, sr: i32, sc: i32, color: i32) -> Vec<Vec<i32>> {

        let mut image = image;
        let mut has_visited: HashSet<(usize, usize)> = HashSet::new();
        let mut fifo: VecDeque<(usize, usize)> = VecDeque::new();
        let u_sr = sr as usize;
        let u_sc = sc as usize;
        fifo.push_front((u_sr,u_sc));

        // Safer way of doing let designated_color_change = image[sr][sc];
        // honestly overkill but on the offchance that a Null could be passed...

        let designated_color_change = image[u_sr][u_sc];

        let y_length = image.len();
        let x_length = image[0].len();

        while !fifo.is_empty() {
            // not necessary with the while loop checking but just to be safe
            if let Some((y_l, x_l)) = fifo.pop_front() {
                if !has_visited.contains(&(y_l, x_l)) {
                    if y_l < y_length && x_l < x_length {
                        if image[y_l][x_l] == designated_color_change {
                            image[y_l][x_l] = color;
                            has_visited.insert((y_l,x_l));

                            if y_l > 0 {
                                fifo.push_back((y_l-1,x_l));   //up
                            }
                            if x_l > 0 {
                                fifo.push_back((y_l,x_l-1));   //left
                            }                        
                            fifo.push_back((y_l+1,x_l));   //down
                            fifo.push_back((y_l,x_l+1)); //right
                        }
                    }   
                }
            }
        }



        return image;
        
    }
}

fn main () {

    let matrix = vec![vec![1,1,1], vec![1,1,0], vec![1,0,1]];
    let sr = 1;
    let sc = 1;
    let color = 2;

    println!("{:?}", matrix);
    println!("{:?}", Solution::flood_fill(matrix, sr, sc, color));


}