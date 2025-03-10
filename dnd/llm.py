from gpt4all import GPT4All

def create_npc(system_message):
    model = GPT4All('gpt4all-falcon-newbpe-q4_0.gguf')
    context = model.chat_session(system_message)
    context.__enter__()
    return model, context
