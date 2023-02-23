init:
		docker build . -f ./Dockerfile - t airflow-local-v2;
up:
		docker-compose up -d 
down:
		docker-compose down --remove-orphan
cleanup:
		make down