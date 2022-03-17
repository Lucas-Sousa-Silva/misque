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

# ### Utilitites ################################################################
access-database:# Access the database with psql >>> SO USEFUL
	docker exec -it misque-database-1 psql --username="${PG_USER}" --password

# ### Run the project
run-misque:
	docker compose -f docker-stuff/docker-compose.misque.yml\
		--env-file docker-stuff/environment.misque.env\
		up -d

stop-misque:
	docker compose down docker-stuff/docker-compose.misque.yml
