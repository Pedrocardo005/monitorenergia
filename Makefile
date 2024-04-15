FILE=requirements.txt
DOCKER_COMPOSE=docker-compose.yml

dev:
	python3 -m venv .;
	bin/pip install -r $(FILE);

	docker-compose up -d;