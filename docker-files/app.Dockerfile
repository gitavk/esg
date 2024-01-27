FROM python:3.11-slim

COPY ./requirements ./requirements
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r ./requirements/prod.txt

WORKDIR app/
COPY src/ src/
EXPOSE 8000
RUN useradd -ms /bin/bash appuser
RUN chown appuser -R /app
USER appuser

CMD ["uvicorn", "src.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
