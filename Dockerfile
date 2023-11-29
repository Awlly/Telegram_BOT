FROM python:3.11-slim
ENV TOKEN='token'
COPY . .
RUN pip install -r req.txt
CMD python bot.py
