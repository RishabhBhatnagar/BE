package main


import (
    "os"
    "net"
    "fmt"
    "io/ioutil"
)


func handleClient(conn *net.Conn){
    fmt.Println("Connected to:", (*conn).RemoteAddr().String())
    for {
        clientData, err := ioutil.ReadAll(*conn)
        if err == nil {
            fmt.Println("Data read from client:", clientData)
            _, err = (*conn).Write([]byte("sent d messages"))
            fmt.Println(err)
        } else {
            fmt.Println(err)
        }
    }
}


func main(){
    args := os.Args
    if len(args) < 2 {
        panic("Provide Port Number")
    }
    portNumber := args[1]
    listener, err := net.Listen("tcp", ":" + portNumber)
    if err != nil {
        panic("Can't listen to the given port")
    }
    defer listener.Close()   // close listener after function exits.

    for {
        conn, _ := listener.Accept()
        go handleClient(&conn)
    }
}
