use std::io;

fn main() {
    // 입력을 받아서 변경하기 때문에 mut
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let numbers: Vec<i32> = input.split_whitespace()
                            .map(|x| x.parse::<i32>().unwrap())
                            .collect();

    let a = numbers[0];
    let b = numbers[1];

    if a > b {
        print!(">");
    } else if b > a {
        print!("<");
    } else {
        print!("==");
    }

}
