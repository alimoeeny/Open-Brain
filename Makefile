
get-deps:
	gpm install

test:
	go test ./...

build:
	go build ./...

run:
	go build ./...
	./open-brain
