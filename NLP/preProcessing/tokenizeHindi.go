package main


import (
	"fmt"
	_ "io/ioutil"
	"os"
	_"strings"
)


// tokenizeFile tokenizes the hindi text file.
// It takes file path as an argument where the file is located.
// It returns a list of tokens obtained after tokenization.
func TokenizeFile(path string) (tokens []string, err error) {
	var token string

	// anonymous function that clears out current token appending previous chars.
	refreshToken := func(){
		if token != "" {
			tokens = append(tokens, token)
		}
		token = ""
	}

	file, err := os.Open(path)
	if err != nil {
		return []string{}, err
	}

	// oneByteArray to read one byte at a time.
	oneByteArray := make([]byte, 1)

	// loop until err is not nil. Generally, err is not nil when it is EOF. 
	for err = nil; err == nil; _, err = file.Read(oneByteArray){
		switch char := oneByteArray[0]; char {
		case 32, 58, 39, 10, 44, 45, 63:
			// byte(' '), byte(':'), byte('\''), byte('\n'), byte(','), byte('-'), byte('?')
			// delimiter is found.
			refreshToken()
		case 224:
			// hindi type word found.
			// non-utf8 words start with 224 and are of 3bytes.
			tempBytes := make([]byte, 2)
			file.Read(tempBytes)   // assuming there is always 2 bytes after 224.
			tempBytes = append([]byte{224}, tempBytes...)
			token += string(tempBytes)
		default:
			token += string(char)
		}
	}
	err = nil     // no error in parsing.
	// naked return because data types were defined in the function definition
	return
}



func main() {
	tokens, _ := TokenizeFile("sampleHindi.txt")
	fmt.Println("Identified tokens:", tokens)
}
