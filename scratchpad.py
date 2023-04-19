from autogpt.config import Config
import openai

CFG = Config()

openai.api_key = CFG.openai_api_key

# Doesn't work
openai.ChatCompletion.create(
                    deployment_id="textdavinci003-model",
                    model="textdavinci003-model",
                    messages=[{"role": "system", "content": "You are a helpful assistant."}],
                    temperature=0,
                    max_tokens=4000,
                )

# works
openai.ChatCompletion.create(
    engine="gpt35turbo-model",
    messages=[{"role": "user", "content": "You are a helpful assistant."}]
    )

# Doesn't work
openai.ChatCompletion.create(
    deployment_id="gpt35turbo-model",
    messages=[{"role": "user", "content": "You are a helpful assistant."}]
    )


# works
openai.Completion.create(engine="textdavinci003-model", prompt="Write a tagline for an ice cream shop.", max_tokens=10)
