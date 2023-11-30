use std::{fs, cmp::max};


fn main() {
    let file_path = "in.txt";
    let contents = fs::read_to_string(file_path)
    .expect("File not found");
    let parts = contents.split("\n");
    let mut max_found = 0;
    let mut current_sum = 0;
    for part in parts {
        if !part.is_empty() {
            let n: u32 = part.parse().expect("NAN");
            current_sum = current_sum + n;
        } else {
            max_found = max(max_found, current_sum);
            current_sum = 0;
        }
    };

    println!("{max_found}");
}
