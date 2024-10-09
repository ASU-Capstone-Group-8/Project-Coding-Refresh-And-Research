import argilla as rg

HF_TOKEN = "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"

client = rg.Argilla(
    api_url="https://dlsmallw-my-argilla.hf.space",
    api_key="HxsHuYHE73cdfA829u6XgyxogAEaQGleMTllLF0Y7C9LCrc31n6OjhBWO-lHlL6tyaMZtcQ1mK2BrdpMdKxNdf1YCPCLBk8GYnB2UEXQWAc",
    headers={"Authorization": f"Bearer {HF_TOKEN}"}
)

settings = rg.Settings(
    guidelines="Classify the reviews as positive or negative.",
    fields=[
        rg.TextField(
            name="review",
            title="Text from the review",
            use_markdown=False,
        ),
    ],
    questions=[
        rg.LabelQuestion(
            name="my_label",
            title="In which category does this article fit?",
            labels=["positive", "negative"],
        )
    ],
)
dataset = rg.Dataset(
    name=f"test_set",
    workspace="argilla", # change this to your workspace
    settings=settings,
    client=client,
)
dataset.create()

records = [
    rg.Record(
        fields={
            "review": "This is a great product.",
        },
    ),
    rg.Record(
        fields={
            "review": "This is a bad product.",
        },
    ),
]
dataset.records.log(records)