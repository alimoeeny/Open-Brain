package main

import (
	"errors"
)

type OBError error

var (
	ERROR_INPUT_MISMATCH               = errors.New("input size does not match the number of input neurons")
	ERROR_INPUT_LABELED_LINE_NOT_FOUND = errors.New("the input labeled line does not exist")
)
