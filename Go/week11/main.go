package main

import "fmt"

func main() {
	// var primes [3]int
	// primes[0] = 2
	// primes[1] = 3
	// primes[2] = 5
	// fmt.Println(primes, primes[1])

	// var primes [3]int = [3]int{2, 3, 5} // 배열 리터럴로 primes 배열 초기화
	// fmt.Println(primes, primes[1])

	primes := [3]int{2, 3, 5}
	fmt.Println(primes, primes[1])

	test := [5]bool{true, true, true} // 초기화 하지 않은 배열 원소의 제로값은 기본적으로 false
	fmt.Println(test[3])

	// for i :=; i < 3; i++ {
	// 	fmt.Println(priprimes[i])
	// }

	i := 0
	for i < 3 {
		fmt.Println(primes[i])
		i++
	}
}
