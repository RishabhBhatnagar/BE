package main


import (
    "bufio"
    "fmt"
    "net"
    "os"
    "strconv"
    "strings"
)


func main(){
    if len(os.Args) < 2 {
        panic("Required ip:host")
    }
    socket := os.Args[1]
    conn, _ := net.Dial("tcp", socket)
    addr := strings.Split(conn.LocalAddr().String(), ":")[1]
    fmt.Println("Current ID:", addr)
    // client will ask for sum of all first n natural numbers mod 1000007.
    var n int
    for {
        fmt.Print(">>> ")
        _, err := fmt.Scanf("%d\n", &n)
        if err == nil {
            // writing current data to server connection
            conn.Write([]byte(strconv.Itoa(n) + "\n"))

            // wait until server sends some message.
            response, _ := bufio.NewReader(conn).ReadString('\n')
            fmt.Print("<<< ", response)
        }
    }
}
