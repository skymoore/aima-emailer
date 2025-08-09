.PHONY: build
build:
	docker buildx build --platform=linux/amd64,linux/arm64 -t ghcr.io/skymoore/aima-emailer:latest --push .

default: build
