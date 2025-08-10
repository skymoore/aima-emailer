.PHONY: build
build:
	docker buildx build --platform=linux/amd64,linux/arm64 -t ghcr.io/skymoore/aima-emailer:v0.4.0 --push .

default: build
