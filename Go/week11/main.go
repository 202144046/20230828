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
	// for i < 4 {
	// for idx, prime := range primes { // 선언하고 변수를 사용안함. 컴파일 에러

	sum := 0
	for _, prime := range primes { // 인덱스 사용 안함
		// fmt.Println(prime)
		sum = sum + prime
		i++
	}
	fmt.Println(sum)
	fmt.Println(float64(sum) / float64(len(primes)))
	fmt.Printf("%.2F\n", float64(sum)/float64(len(primes)))
}
