package main

import (
	"fmt"
	"strings"
	"time"
)

func main() {
	var now time.Time = time.Now()
	now = time.Now()
	//var year int = now.Year()
	var year = now.Year()
	month := now.Month()
	fmt.Println(year, month, now.Day(), now.Hour(), now.Minute(), now.Second())

	HotSpurs := "hm ? j madi?"
	replacePlayer := strings.NewReplacer("?", "son")
	player := replacePlayer.Replace(HotSpurs)
	fmt.Println(player)
}
