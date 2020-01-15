package main


import (
    "fmt"
    "net"
    "bufio"
    "os"
    "strings"
    "strconv"
)


var MOD = 1000007


func fact(n int) int {
    // writing the worst implementation of factorial number
    // such that server takes lots of time per bigger requests of client.

    // assuming number is a positive number
    if n < 2 {
        return 1
    }
    return ( n * fact(n - 1) ) % MOD
}


func fact_sum(n int) (sum int){
    for i := 0; i <= n; i++ {
        sum += fact(i) % MOD
    }
    return
}


func main() {
    if len(os.Args) < 2 {
        panic("Enter a four digit host number....")
    }
    host := os.Args[1]
    listener, _ := net.Listen("tcp", ":" + host)
    // infinite loop to accept all the connections.
    for {
        conn, err := listener.Accept()
        fmt.Println("Connection Received From:", conn.RemoteAddr().String())
        if err == nil {
            // anonymous function to handle client.
            go func(c net.Conn){
                addr := strings.Split(conn.RemoteAddr().String(), ":")[1]
                // listen to all the data from client
                for {
                    // read new line from the client connection 
                    numStr, err := bufio.NewReader(c).ReadString('\n')
                    num, _ := strconv.Atoi(strings.TrimSuffix(numStr, "\n"))
                    fmt.Println(fmt.Sprintf("%s :: Processing Request(n=%d)", addr, num))
                    res := fact_sum(num)
                    if err == nil {
                        c.Write([]byte(fmt.Sprintf("Sum(fact(0..%d)) = %d\n", num, res)))
                    }
                    fmt.Println(fmt.Sprintf("%s :: End Req(n=%d)", addr, num))
                }
            }(conn)
        }
    }
}

