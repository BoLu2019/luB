var fibonacci = (n) => {
    if (n <= 0){
	return 0;
    }
    else if (n == 1){
	return 1;
    }
    else{
	return fibonacci(n-2)  + fibonacci(n -1);
    }
    
}

//console.log(fibonacci(0))

//console.log(fibonacci(1))

//console.log(fibonacci(2))

//console.log(fibonacci(3))

var gcd = (a, b) => {
    c = a % b;
    if (c == 0){
	return b;
    }
    else {
	return gcd(b, c);
    }
}

var students = []

var randomStudent = () => {
    
}
