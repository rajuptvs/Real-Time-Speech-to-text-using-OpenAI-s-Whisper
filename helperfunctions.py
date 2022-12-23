import whisper
class whisper_gpt:
    def __init__(self,model_size,file) :
        self.model_size=model_size
        self.file=file
        self.model = whisper.load_model(model_size)

    
    def transcribe(self):
        self.final = self.model.transcribe(self.file)
        print(self.final["text"])
        return self.final["text"]
        
    def ntranscribe(self):
        self.final = self.model.transcribe(self.file)
        return self.final["text"]
    def get_result(self):
        self.transription=self.final["text"]
       
        
    
    def save_transcript(self,text,filename):
        with open(filename, 'w') as f:
            f.writelines(text)
