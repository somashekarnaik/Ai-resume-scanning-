## Career AI Assistant setup

The assistant uses the OpenAI API to answer career questions. Create `backend/.env`
from `backend/.env.example` and set `OPENAI_API_KEY` to your own API key. You can
optionally set `OPENAI_MODEL`; it defaults to `gpt-4o-mini`.

Install the backend dependencies with `pip install -r requirements.txt`, then restart
the FastAPI server. Keep the API key in the backend environment only; never add it to
frontend code or commit the `.env` file.

The assistant can answer general career questions without an uploaded resume. If the
user has analyzed a resume, the assistant also receives detected skills, the selected
and recommended roles, match score, and format-review findings. It does not receive
the original resume file. Questions and recent chat history are sent to OpenAI, as
disclosed in the chat panel.