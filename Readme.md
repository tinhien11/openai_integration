Init db and run application
```bash
export OPENAI_API_KEY=''
flask --app app init-db
flask --app app run --debug
```

Test:
```bash
# Empty prompt
curl --location 'http://127.0.0.1:5000/openai-completion' \
--header 'Content-Type: application/json' \
--data '{"prompt": ""}'

# Non-empty prompt
curl --location 'http://127.0.0.1:5000/openai-completion' \
--header 'Content-Type: application/json' \
--data '{"prompt": "hello"}'
```

### Rubric:
API Functionality (30%): Done
OpenAI API Integration (30%): Done
Database Logging (20%): Done
Edge Case and Error Handling (10%): Done
Code Quality and Documentation (10%): Done
