package main

import (
    "fmt"
    "os"
    "bufio"
    "net"
    "io/ioutil"
)

func main(){
    args := os.Args
    if len(args) < 2 {
        panic("No server address given. Provide ip:port of the server you want to listen to.")
    }
    address := args[1]
    conn, err := net.Dial("tcp", address)
    defer conn.Close()
    if err != nil {
        panic("Cannot connect to the network")
    }
    fmt.Println("Connected to server successfully.")
    fmt.Println(conn)
    for {
        reader := bufio.NewReader(os.Stdin)
        fmt.Print(">>> ")                  // py style prompt
        msg, _ := reader.ReadString('\n')  // read a newline
        conn.Write([]byte(msg + "\n"))
        fmt.Println("")
        // wait until server doesn't send any data
        received_msg, err := ioutil.ReadAll(conn)
        if err == nil {
            fmt.Println("<<<", string(received_msg))
        } else {
            fmt.Println(err)
        }
    }
}
