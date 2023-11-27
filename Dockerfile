FROM python:3.11-slim
ENV TOKEN = '6723682618:AAGssNs-f1Cz35lYIRtLut4bb1la_3U_gQ4'
COPY . .
RUN pip install -r req.txt
CMD python bot.py