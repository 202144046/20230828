package main

import (
	"fmt"
	"math"
	"reflect"
	"strings"
)

func main() {

	// koreanzombie := "정찬성" // 문법적으로는 문제없지만 커뮤니티 관례를 따르자.
	KoreanZombie := "정찬성"
	fmt.Println(KoreanZombie)

	// var 7c string 변수명은 알파벳 대소문자로 시작해야 한다.(숫자 안됨)

	// var G string	 외부로 노출되어야하는 변수명은 대문자로 시작해야 한다.

	var c string
	var d int
	var e bool
	var f float64

	fmt.Println(c, d, e, f) // c =  , d = 0, e = false, f = 0

	// var a int // 선언
	// a = 7     // assign value

	// var a int = 7

	// var a = 7

	a := 7
	fmt.Println(a, reflect.TypeOf(a))

	// b := 8.34 // float64
	var b float32 = 8.34
	fmt.Println(b, reflect.TypeOf(b))

	fmt.Println(a * int(b))
	fmt.Println(float32(a) > b)

	fmt.Println('Z', '2', '\n', '김', '인', '하') // rune literals(int 32) 0, 5, 100, 465
	fmt.Println(reflect.TypeOf('Z'), reflect.TypeOf('2'), reflect.TypeOf("Hi"), reflect.TypeOf(4.99), reflect.TypeOf(false))
	// fmt.Println(math.Floor("삼.오"), math.Ceil("이백십칠쩜칠"), math.Sqrt("sixteen"))
	// fmt.Println(strings.Title(3.147592))
	fmt.Println(math.Floor(2.17), math.Ceil(2.17), math.Sqrt(16))
	fmt.Println(strings.Title("open source\t programming\n\"go\"!")) // 각 단어의 앞글자가 대문자
	// fmt.Println(strings.Title("오픈소스 프로그래밍"))
	// fmt.Println("Open Source Programming~")

}
