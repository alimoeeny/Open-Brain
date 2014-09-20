package main

import (
	"fmt"
)

var nextId chan string

func init() {
	nextId = make(chan string)
	go func() {
		var counter int64 = 0
		for {
			s := fmt.Sprintf("%x", counter)
			nextId <- s
			counter += 1
		}
	}()
}

func main() {
	fmt.Println("OpenBrain Version: xxx")
	pb := peaBrain()
	fmt.Printf("PeaBrain: %#v", pb)
}
