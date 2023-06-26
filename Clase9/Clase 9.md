Análisis de mensajes de odio en XXSS: Modelos NLP (Natural Language Processing) con HuggingFace

- Torch y TensorFlow son similares, Torch se utiliza más a nivel personal y TensorFlow a nivel empresarial.

### Primera prueba: Código de ejemplo

```Python
from transformers import pipeline

pipe = pipeline("text-classification")
result = pipe("Maria wants to kill Johan")
print(result)

pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es")
result = pipe("Maria wants to kill Johan")
print(result)
```

- Buscar en HuggingFace modelos para entender o traducir el catalán.
- Traducción de inglés a catalán:

```Python
from transformers import pipeline

pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ca")
result = pipe("Maria wants to kill Johan")
print(result)
```

### Segunda prueba: modelos individuales

- El tokenizer se encarga de dividir el texto en partes para poder puntuar las partes.
- Los modelos y tokenizer suelen ser el mismo.


```Python
from tqdm import tqdm
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

df = pd.read_csv("dataset-inmigrantes-barcelona.csv", nrows=10, usecols=["tweet_id","text"])

tokenizer = AutoTokenizer.from_pretrained("MMG/xlm-roberta-base-sa-spanish")
model = AutoModelForSequenceClassification.from_pretrained("MMG/xlm-roberta-base-sa-spanish")

pipe = pipeline("text-classification", model=model, tokenizer=tokenizer)

tweets = df["text"].to_list()
tweet_id = df["tweet_id"].to_list()
tup_list = []

for tweet in tweets:
    result = pipe(tweet)
    content = result[0]
    label = content["label"]
    score = content["score"]
    tupla = (tweet, label, score)
    tup_list.append(tupla)

data = pd.DataFrame.from_records(tup_list, columns=["text", "label", "score"])
data.to_csv("analysis.csv", index=False)
```

- El número que indica el modelo es la seguridad con la que afirma la etiqueta.

### Tercer ejemplo: comparación de modelos

```Python
import glob
from tqdm import tqdm
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

models = ["MMG/xlm-roberta-base-sa-spanish", "jorgeortizfuentes/spanish_hate_speech", "francisco-perez-sorrosal/distilbert-base-uncased-finetuned-with-spanish-tweets-clf"]

dataset = "dataset-inmigrantes-barcelona.csv"

def proc(dataset):
    for model in models:
        model_name = model.split("/")[1]
        dataset_new_name = f"procesado-{model_name}.csv"
        tup_list = []
        df = pd.read_csv(dataset, usecols=["tweet_id","text"])
        tweets = df["text"].to_list()
        tweet_id = df["tweet_id"].to_list()

        t = AutoTokenizer.from_pretrained(model)
        m = AutoModelForSequenceClassification.from_pretrained(model)

        for tweet, tid in tqdm(zip(tweets, tweet_id)):
            pipe = pipeline("text-classification", model=m, tokenizer=t)
            result = pipe(tweet)
            content = result[0]
            label = content["label"]
            score = content["score"]
            tupla = (str(tid), tweet, label, score)
            tup_list.append(tupla)

        data = pd.DataFrame.from_records(tup_list, columns=[f"tweet_id", "text", f"label-{model}", f"score-{model}"])
        data.to_csv(dataset_new_name, index=False)

proc(dataset)

lists_of_sets = []
datasets = glob.glob("procesado-*.csv")

dataset_madre = pd.read_csv(datasets[0])

for d in datasets[1:]:
    df = pd.read_csv(d)
    dataset_madre = dataset_madre.merge(df, on=["tweet_id", "text"])

dataset_madre.to_csv(f"final-{dataset}")
```

- El código extrae diferentes archivos que luego se pueden exportar a Tableau para hacer visualizaciones.