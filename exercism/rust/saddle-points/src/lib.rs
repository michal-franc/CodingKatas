//     0  1  2 
//     -------
// 0 | 9, 5, 6
// 1 | 8, 3, 6
// 2 | 7, 2, 7
//
//
//
// for each x check if row is greater or equal
// for each x check if column is smaller or equal


pub fn find_saddle_points(input: &[Vec<u64>]) -> Vec<(usize, usize)> {

    let xSize = input.len();
    let ySize = input[0].len();
    let mut results = vec![];

    for x in 0..xSize {
        for y in 0..ySize {
            let mut ok = true;
            let cur = input[x][y];
            for item in &input[x] {
               if item > &cur {
                   ok = false
               }
            }

            if ok == true {
                for i in 0..xSize {
                   if input[i][y] < cur {
                       ok = false
                   }
                }
            }

            if ok {
                results.push((x,y))
            }
        }
    }

    results
}
