python-test:
	pytest

clean:
	rm -rf ./dist

python:
	rm -rf docs && \
	rm -rf conekta/models && \
	docker run --rm \
    -v ${PWD}:/local openapitools/openapi-generator-cli:v7.9.0 generate \
	-i https://raw.githubusercontent.com/conekta/openapi/main/_build/api.yaml \
	-g python \
	-o /local \
	-c /local/config-python.json \
	--global-property modelTests=false
