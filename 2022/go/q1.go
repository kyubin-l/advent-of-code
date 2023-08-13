package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
)

func Solve_Q1() {
	questionNo := 1
	elf := load(questionNo)
	mostCals := part_1(elf)
	fmt.Println("Part 1: ", mostCals)
	sumMostThree := part_2(elf)
	fmt.Println("Part 2: ", sumMostThree)
}

func part_1(elf [][]int) int {
	var cur int
	var max int
	for _, cals := range elf {
		cur = 0
		for _, cal := range cals {
			cur += cal
		}
		if cur >= max {
			max = cur
		}
	}
	return max
}

func part_2(elf [][]int) int {
	sums := []int{}
	for _, cals := range elf {
		cur := 0
		for _, cal := range cals {
			cur += cal
		}
		sums = append(sums, cur)
	}
	sort.Ints(sums)
	n := len(sums)
	return sums[n-1] + sums[n-2] + sums[n-3]
}

func load(q int) [][]int {
	var elf [][]int
	filepath := fmt.Sprintf(
		"/Users/klee/workspace/advent-of-code/2022/inputs/2022_q%v.txt",
		q,
	)
	file, err := os.Open(filepath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var cur []int
	for scanner.Scan() {
		if scanner.Text() != "" {
			cal, err := strconv.Atoi(scanner.Text())
			if err != nil {
				log.Fatal(err)
			}
			cur = append(cur, cal)
		} else {
			elf = append(elf, cur)
			cur = []int{}
		}
	}
	elf = append(elf, cur)
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	return elf
}
