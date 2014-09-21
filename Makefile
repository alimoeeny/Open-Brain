
get-deps:
	go get github.com/alimoeeny/gomega

test:
	go test ./...

build:
	go build ./...

run:
	go build ./...
	./open-brain
