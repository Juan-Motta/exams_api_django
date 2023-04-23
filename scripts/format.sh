#!/bin/bash

black --config pyproject.toml .  
isort --settings-path=pyproject.toml .