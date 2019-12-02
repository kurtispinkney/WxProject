FROM python:3.7

RUN pip install --upgrade pip
COPY requirements.txt .

RUN pip install docker-py feedparser nosexcover prometheus_client pycobertura pylint pytest pytest-cov requests setuptools sphinx
RUN pip install -r requirements.txt 
RUN wget -qO /usr/local/bin/qcoverage  https://github.com/qnib/qcoverage/releases/download/v0.1/qcoverage_v0.1_Linux \
 && chmod +x /usr/local/bin/qcoverage
