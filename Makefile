python-test:
	pytest

clean:
	rm -rf ./dist

python:
	rm -rf docs && rm -rf test && \
	rm -rf conekta/models && \
	rm -rf conekta/api && \
	docker run --rm \
    -v ${PWD}:/local openapitools/openapi-generator-cli:v7.24.0 generate \
	-i https://raw.githubusercontent.com/conekta/openapi/refs/heads/release/v2.3.0/_build/api.yaml \
	-g python \
	-o /local \
	-c /local/config-python.json \
	--global-property modelTests=false && \
	sed -i.bak 's/requires-python = ">=3.9"/requires-python = ">=3.10"/' pyproject.toml && \
	rm -f pyproject.toml.bak # workaround: generator v7.24.0 emits >=3.9; fixed upstream, remove on next generator upgrade
