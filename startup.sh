#!/bin/sh
docker-compose up -d
docker exec acc3_fenics_1 bash -c "cd ../murtazo/navier_stokes_solver/; python server.py" -d
