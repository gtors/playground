package main

import "C"


//export say
func say() {
    go func() {
        println("Hello to python!")
    }()
}


func main() {}
