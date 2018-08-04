// find a + b + c == 1000
// a^2 + b^2 = c^2
//
// c == 1000 - (a+b)
// a^2 + b^2 = (1000 - (a+b))^2
// a^2 + b^2 = 1000000 - 2000(a+b) + (a+b)^2
// a^2 + b^2 = 1000000 - 2000(a+b) + a^2 + b^2 + 2ab
// 2000(a+b) - 2ab = 1000000
// 1000(a+b) - ab = 500000
//
const STOP: u32 = 1000;

fn check(a: u32, b: u32) -> bool {
    1000 * (a + b) - a * b == 500000
}

fn brute() -> Option<u32> {

    for a in 1..STOP {
        for b in 1..STOP {
            if check(a, b) { 
                println!("a: {}, b: {}, c: {}", a, b, (1000 - (a + b)));
                return Some(a * b * (1000 - (a + b)))
            }
        }
    }

    None
}

pub fn find() -> Option<u32> {
    return brute()
}
