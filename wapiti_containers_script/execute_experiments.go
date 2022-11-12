package main

import (
	"fmt"
	"os"
	"os/exec"
	"strconv"
)

func executeExperiment(index int) {
	cityfileName := "cidade_" + strconv.FormatInt(int64(index+1), 10)
	imageId := "06b7967ea520"
	hostBind := "/home/eduardovitor/teste_volume"
	containerBind := "/home/wapiti_reports"
	volumeBind := fmt.Sprintf("%s:%s", hostBind, containerBind)
	dockerCmd := "docker"
	expRoundEnv := 1
	urlsPathEnv := cityfileName
	cityDictEnv := "url_cidade_dict.txt"
	severityDictEnv := "owasp_severity_dict_pyformat.txt"
	envVars := "EXP_ROUND=" + strconv.FormatInt(int64(expRoundEnv), 10) +
		"\n" +
		"URLS_PATH=" + urlsPathEnv +
		"\n" +
		"CITY_DICT_PATH=" + cityDictEnv +
		"\n" +
		"SEVERITY_DICT_PATH=" + severityDictEnv
	envFilePath := "envfile.txt"

	err := os.WriteFile(envFilePath, []byte(envVars), 0644)
	if err != nil {
		fmt.Println(err)
	}

	container_name := "wapiti" + strconv.FormatInt(int64(index+1), 10)
	cmd := exec.Command("sudo", dockerCmd, "run", "--name", container_name, "--env-file", envFilePath, "-v", volumeBind, "-dt", imageId)
	stdout, err := cmd.Output()
	if err != nil {
		fmt.Println(err.Error())
	}
	fmt.Println(string(stdout))
}

func main() {
	urlNumber := 101
	for i := 0; i <= urlNumber; i++ {
		if i == 2 {
			break
		}
		executeExperiment(i)
	}

}
