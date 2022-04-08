package main

/*
#include <stdint.h>
*/
import "C"
import (
    "runtime/cgo"
)

type user struct {
    name string
}

func (u *user) setName(name string) {
    u.name = name
}

func (u *user) printName() {
    println("user name is ", u.name)
}


//export user_new
func user_new() C.uintptr_t {
    u := new(user)
    h := cgo.NewHandle(u) 
    return C.uintptr_t(h)
}

//export user_set_name
func user_set_name(_h C.uintptr_t, name *C.char) {
    h := cgo.Handle(_h)
    u := h.Value().(*user)
    u.setName(C.GoString(name))
}

//export user_print_name
func user_print_name(_h C.uintptr_t) {
    h := cgo.Handle(_h)
    u := h.Value().(*user)
    u.printName()
}

//export user_free
func user_free(_h C.uintptr_t) {
    h := cgo.Handle(_h)
    h.Delete()
}

//export say
func say() {
    go func() {
        println("Hello to python!")
    }()
}


func main() {}
