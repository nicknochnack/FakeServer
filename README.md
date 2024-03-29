# LLaMA
Run sick LLM apps hyper fast on your local machine for funzies. 

## See it live and in action 📺
<a href=""><img src="https://i.imgur.com/jvTcxvV.png"/></a>


# Startup 🚀
1. Git clone https://github.com/ggerganov/llama.cpp 
2. Run the make commands: 
- Mac: `cd llama.cpp && make`
- Windows (from <a href="https://github.com/ggerganov/llama.cpp/blob/master/README.md">here</a> ):
    1. Download the latest fortran version of [w64devkit](https://github.com/skeeto/w64devkit/releases).
    2. Extract `w64devkit` on your pc.
    3. Run `w64devkit.exe`.
    4. Use the `cd` command to reach the `llama.cpp` folder.
    5. From here you can run:
        ```bash
        make
        ```
3. pip install openai 'llama-cpp-python[server]' pydantic instructor streamlit
4. Start the server: 
- Single Model Chat </br>
`python -m llama_cpp.server --model models/mistral-7b-instruct-v0.1.Q4_0.gguf `
- Single Model Chat with GPU Offload</br>
`python -m llama_cpp.server --model models/mistral-7b-instruct-v0.1.Q4_0.gguf --n_gpu -1` 
- Single Model Function Calling with GPU Offload</br>
`python -m llama_cpp.server --model models/mistral-7b-instruct-v0.1.- Q4_0.gguf --n_gpu -1 --chat functionary` 
- Multiple Model Load with Config</br>
`python -m llama_cpp.server --config_file config.json`
- Multi Modal Models</br>
`python -m llama_cpp.server --model models/llava-v1.5-7b-Q4_K.gguf --clip_model_path models/llava-v1.5-7b-mmproj-Q4_0.gguf --n_gpu -1 --chat llava-1-5` </br>

# Models Used 🤖
- Mistral: https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF
- Mixtral: https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF
- LLaVa: https://huggingface.co/jartine/llava-v1.5-7B-GGUF/tree/main

# Who, When, Why?

👨🏾‍💻 Author: Nick Renotte <br />
📅 Version: 1.x<br />
📜 License: This project is licensed under the MIT License </br>
