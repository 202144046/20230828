package main

import "fmt"

func main() {
	// a := []string("a", "b", "c", "d")
	// as := a[:2]
	// as[1] = "2"
	// fmt.Println(a, as)

	// b := [4]int{4, 3, 2, 1}
	// bs := b[1:3]
	// fmt.Println(b, bs)

	a := make([]string, 4, 5) // type, length, capacity
	a[0] = "a"
	a[2] = "b"
	a[3] = "c"
	as := a[0:2]
	as[1] = "Z"
	// c := append(a, "y")
	c := append(a, "y", "x")

	fmt.Println(a, len(a), cap(a))
	fmt.Println(c, len(c), cap(c))
}
