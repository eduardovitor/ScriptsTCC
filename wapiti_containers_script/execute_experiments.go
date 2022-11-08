package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"strconv"
)

func executeExperiment(index int, line string) {
	lineToWrite := []byte(line)
	fileName := "cidade_" + strconv.FormatInt(int64(index+1), 10)
	imageId := "d9996f00f450"

	err := os.WriteFile(fileName, lineToWrite, 0644)
	if err != nil {
		fmt.Println(err)
	}

    volumeBind := "/home/eduardovitor/teste_volume:/home/wapiti_reports"
	docker_cmd := "docker"
	envArg := "URLS_PATH=" + fileName
	container_name := "wapiti" + strconv.FormatInt(int64(index+1), 10)
	cmd := exec.Command("sudo", docker_cmd, "run", "--env", envArg, "--name", container_name, "-v", volumeBind, "-dt", imageId)
	stdout, err := cmd.Output()
	if err != nil {
		fmt.Println(err.Error())
	}
	fmt.Println(string(stdout))
}

func main() {

	filePath := "lista_urls_atualizada.txt"
	readFile, err := os.Open(filePath)

	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)
	var fileLines []string

	for fileScanner.Scan() {
		fileLines = append(fileLines, fileScanner.Text())
	}

	readFile.Close()

	for i, line := range fileLines {
		if i == 5 {
			break
		}
		fmt.Println(line)
		executeExperiment(i, line)
	}

}
