import models
from agent import AgentConfig

def initialize():
    # chat_llm = models.get_openai_chat(model_name="openai/gpt-4o-mini", temperature=0.8) 
    # main chat model used by agents (smarter, more accurate)
    chat_llm = models.get_openai_chat(model_name="together_ai/meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo", temperature=0.8)
    # chat_llm = models.get_ollama_chat(model_name="wizard-vicuna-uncensored:30b", temperature=0)
    # chat_llm = models.get_lmstudio_chat(model_name="lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF", temperature=0)
    # chat_llm = models.get_openrouter_chat(model_name="anthropic/claude-3.5-sonnet", temperature=0.8)
    # chat_llm = models.get_azure_openai_chat(deployment_name="gpt-4o-mini", temperature=0)
    # chat_llm = models.get_anthropic_chat(model_name="claude-3-5-sonnet-20240620", temperature=0)
    # chat_llm = models.get_google_chat(model_name="gemini-1.5-flash", temperature=0.8)
    # chat_llm = models.get_groq_chat(model_name="llama-3.1-70b-versatile", temperature=0)
    
    # utility model used for helper functions (cheaper, faster)
    utility_llm = chat_llm # change if you want to use a different utility model

    # embedding model used for memory
    # embedding_llm = models.get_openai_embedding(model_name="text-embedding-3-small")
    # embedding_llm = models.get_ollama_embedding(model_name="nomic-embed-text")
    embedding_llm = models.get_huggingface_embedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
    # embedding_llm = models.get_lmstudio_embedding(model_name="nomic-ai/nomic-embed-text-v1.5-GGUF")

    # agent configuration
    config = AgentConfig(
        chat_model = chat_llm,
        utility_model = utility_llm,
        embeddings_model = embedding_llm,
        # prompts_subdir = "",
        memory_subdir = "agents/agent0/memory",
        # knowledge_subdir: str = ""
        auto_memory_count = 15,
        # auto_memory_skip = 2,
        # rate_limit_seconds = 60,
        rate_limit_requests = 15,
        # rate_limit_input_tokens = 0,
        # rate_limit_output_tokens = 0,
        # msgs_keep_max = 25,
        # msgs_keep_start = 5,
        # msgs_keep_end = 10,
        max_tool_response_length = 6000,
        response_timeout_seconds = 60,
        #code_exec_docker_enabled = False,
        code_exec_docker_name = "agent-zero",
        code_exec_docker_image = "bpawnzz/agent-zero:current",
        code_exec_docker_ports = { "22/tcp": 50022 },
        # code_exec_docker_volumes = { files.get_abs_path("work_dir"): {"bind": "/root", "mode": "rw"} },
        code_exec_ssh_enabled = True,
        code_exec_ssh_addr = "100.71.229.63",
        code_exec_ssh_port = 50022,
        code_exec_ssh_user = "root",
        code_exec_ssh_pass = "toor",
         # additional = {},
    )

    # return config object
    return config 
