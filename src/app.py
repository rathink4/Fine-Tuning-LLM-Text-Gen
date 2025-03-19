from peft import AutoPeftModelForCausalLM, PeftConfig
from transformers import AutoTokenizer, AutoModelForCausalLM
import streamlit as st

@st.cache_resource
class AppModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
        self.tokenizer.pad_token = self.tokenizer.eos_token

        self.trained_model = AutoPeftModelForCausalLM.from_pretrained('text-generation-lora-model-v2')

        self.trained_model.to("cpu")
    
    def generate_synopsis(self, starter_prompt: str):
        inputs = self.tokenizer(starter_prompt, return_tensors="pt").to("cpu")

        outputs = self.trained_model.generate(
            inputs.input_ids,
            max_new_tokens = 75,
            do_sample=True,
            top_k=50,
            top_p=0.95,
        )

        output_str = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)
        return output_str


model = AppModel()
prompt = st.text_area("Enter the begining of your movie idea..")
clicked = st.button("Generate synopsis")

if clicked:
    generated_story = model.generate_synopsis(prompt)[0]

    chat_message = st.chat_message("ai")
    chat_message.markdown(generated_story)