#    ____ ___  (_)________ ___  _____ 
#   / __ `__ \/ / ___/ __ `/ / / / _ \
#  / / / / / / (__  ) /_/ / /_/ /  __/
# /_/ /_/ /_/_/____/\__, /\__,_/\___/ 
#                     /_/             
# Copyright (C) 2022  Lucas Sousa Silva

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

include deployment/misque-deployment.dev.env

### POSTGRESQL ################################################################
# Create and run a container that will host postgres.
build-database:
	docker run -d\
		-e POSTGRES_USER="${PG_USER}"\
		-e POSTGRES_PASSWORD="${PG_PASSWORD}"\
		-v LOCAL_PG_DIR:/var/lib/postgresql/data\
		-p 5432:5432\
		--name=postgres_enem\
		--network=host\
		postgres:14.2-alpine

# Host postgres in a container.
run-database:
	docker start postgres_enem

### Backend REST ##############################################################
# Build the image that host all the REST api things
build-rest-service:
	docker build \
		-f deployment/backend/Dockerfile . \
		--network=host\
		--tag=backend-enem

# Run the rest api
run-rest-service:
	docker run\
		-p 8000:8000\
		--name=backend-enem

### Utilitites ################################################################
access-database:# Access the database with psql >>> SO USEFUL
	docker exec -it postgres_enem psql --username="${PG_USER}" --password
