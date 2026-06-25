// rust重写 （rust兼具安全性和极致性能）

struct MinStack {
    stack: Vec<i32>,
    min_stack: Vec<i32>,
}

impl MinStack {
    fn new() -> Self {
        MinStack {
            stack: Vec::new(),
            min_stack: Vec::new(),
        }
    }
    
    fn push(&mut self, val: i32) {
        self.stack.push(val);
        
        //使用 match 或 if let 处理空栈
        match self.min_stack.last() {
            Some(&min) => self.min_stack.push(val.min(min)),
            None => self.min_stack.push(val),
        }
    }
    
    fn pop(&mut self) {
        self.stack.pop();
        self.min_stack.pop();
    }
    
    fn top(&self) -> i32 {
        self.stack.last().copied().unwrap()
    }

    fn get_min(&self) -> i32 {
        self.min_stack.last().copied().unwrap()
    }
}
