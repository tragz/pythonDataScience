
# Perplexity PP
Perplexity is the inverse probability of test set normalized by the number of words. helps understand how well the model generalizes on the unseen data.

Perplexity should be low on both the training and validation datasets. 

A model with low training perplexity but high validation perplexity might be overfitting.

PP applies specifically to classical language model ( autoregressive or causal language models) and not well defined for masked language models like BERT (see [summary of the models](https://huggingface.co/docs/transformers/main/en/model_summary)).

#### Key properties of perplexity
1. `intrinsic` metric
2. metric quantifies how `certain` a model is about the predictions it makes
3. `quickly` calculated using just the probability distribution the model leans from training datasets.

#### Intuition
lower the perplexity measure the `better` the language mode is at modelling unseen sentences

simple monotonic function of `entropy`
 ![img.png](img.png)

## Installation

#### Add Virtual Environment
```bash
    python -m venv venv
    source venv/bin/activate
```

#### Install openAI

```bash
    pip install evaluate
```
Restart the Kernal after installing the packages    
## Documentation
####  How to evaluate a Language Model?
- Evaluating a Language model let us know whether one language model is better than another
    - Intrinsic evaluation - captures how well the model captures what it is supposed to capture
    - Extrinsic evaluation - task based evaluation that essentially captures how useful the model is for a particular task

#### Intrinsic Evaluation
- NLP system e2e is often very expensive 
- easier metric that can quickly used to evaluate potential improvements in a language model
- Good scores during intrinsic evaluation do not always mean better scores during extrinsic evaluation
    - perplexity
    - cross-entropy
    - bit-per-character

#### Interpreting Perplexity
- perplexity of a uniform random variable with K outcomes is K
    - PP of fair coin is 2
    - PP of fair 6 sided die is 6

#### Limitations and Bias
-    output values is based heavily on what text the model is trained on. This means that perplexity scores are not comparable between modles / datasets


## REFERENCES
1. [Perplexity - Evlaution of LLMs Part 1](https://www.linkedin.com/pulse/perplexity-evaluation-llms-part-1-akash-gautam-jnkpc/)