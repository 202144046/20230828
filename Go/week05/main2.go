package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	fmt.Print("Input score : ")
	reader := bufio.NewReader(os.Stdin)
	inputScoreString, err := reader.ReadString('\n')
	// inputScore := reader.ReadString('\n') 		// 1 variable but reader.ReadString returns 2 values
	// inputScore, err := reader.ReadString('\n') 	// err declared and not used
	// inputScore, _ := reader.ReadString('\n') 	// option 1
	//inputScore, err := reader.ReadString('\n') // option 2
	// log.Fatal(err)                             // 프로그램 종료 (에러 감지 후 리포팅 하기 위해 사용)
	if err != nil {
		log.Fatal(err)
	}

	inputScoreString = strings.TrimSpace(inputScoreString)
	inputScore, err := strings.ParseFloat(inputScoreString, 32)
	var grade string

	if inputScore >= 90 {
		grade = "A grade!"
		// fmt.Println("You got", grade)
	} else {
		grade = "under A grade..."
		// fmt.Println("You got", grade)
	}

}
