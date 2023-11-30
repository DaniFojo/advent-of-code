use std::fs;


fn main() {
    let file_path = "in.txt";
    let contents = fs::read_to_string(file_path)
    .expect("File not found");
    let parts = contents.split("\n");
    let mut current_sum = 0;
    let mut v: Vec<u32> = vec![];
        for part in parts {
        if !part.is_empty() {
            let n: u32 = part.parse().expect("NAN");
            current_sum = current_sum + n;
        } else {
            v.push(current_sum);
            current_sum = 0;
        }
    };
    v.sort();
    let sliced = &v[v.len()-3..v.len()];
    let sum: u32 = sliced.iter().sum();
    println!("{sum}");
}
