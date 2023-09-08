// if done file exist kill process 1 if not exist wait a minute and check again until done file exist

package main

import (
	"fmt"
	"os"
	"os/exec"
	"time"
)

func main() {
	// recieve parameter from command line and assign to variable
	if len(os.Args) > 1 {
		fmt.Println("PID to I'll be kill: ", os.Args[1])
	} else {
		fmt.Errorf("no args")
		os.Exit(1)
	}
	pid:= os.Args[1]

	for {
		if _, err := os.Stat("done"); err == nil {
			fmt.Println("done file exist")
			cmd := exec.Command("kill", "-9", pid)
			err := cmd.Run()
			if err != nil {
				fmt.Println(err)
			}
			break
		} else {
			fmt.Println("done file not exist")
			time.Sleep(1 * time.Minute)
		}
	}

	os.Exit(0)
}