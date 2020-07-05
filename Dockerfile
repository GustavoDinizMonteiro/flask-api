FROM pypy:latest

# Set environment variables.
ENV HOME /root
# Define working directory.
WORKDIR /root

RUN pip install pipenv

# Cloning and install dependencies
RUN \
    apt-get install git && \
    git clone https://github.com/GustavoDinizMonteiro/sheetgo-challenge-backend.git

RUN cd sheetgo-challenge-backend  && \
    pipenv --python pypy3 && \
    pipenv run python -m pip install --upgrade pip && \
    pipenv install --skip-lock

# Define working directory.
WORKDIR /root/sheetgo-challenge-backend