
# Question and Answering LLM

Hi!!! Lads Welcome to this repository. This is a question-and-answering application, which uses the power of Generative AI to answer your doubts.

LLM (Large Language Models) is a type of artificial intelligence algorithm that uses the power of Deep learning techniques to understand the data, which is usually trained on massively large amounts of data to generate or respond to text-based data ie. Human understanding/speaking language.

The buzz term Generative AI is closely related to LLMs as it works and generates text-based responses /contents.

How does LLM work?
There are a few basic steps that are involved in training LLM.

The initial step of training an LLM is to train the basic layer of LLM which is trained using a relatively large/massive amount of data. These data are typically unstructured as these data are text-based and it uses Unsupervised machine learning techniques to find the underlying pattern of the text-based data.

Once the base layer of the LLM is trained, the second step of the training includes hyperparameter tuning or fine-tuning of the model so that the LLM can understand the underlying pattern, hidden insights of the text data to understand and generalize on the context of the training data.

After this LLM uses the Deep learning NLP technique named Transformers to effectively find the relationship between the words, the importance of the words and understand the context using self-attention models.

Once the complete training of the LLM is done the testing of the model is usually done by providing prompts to the model and the response of the model to it.

What is Langchain?
Langchain is an open-source framework that allows users to connect or work with Large Language Models with our own custom data.

That is Langchain is an intermediate that allows us to closely work with LLM’S acting as a wrapper.

Langchain is Agent-based and Data-centric.

Components of Langchain
LLM components
Chains
Agents
LLM components:
LLM wrappers
Prompt templates
Indexing
Memories
LLM wrappers:

LLM wrappers are simply an intermediate that allows one to connect to a Large Language Model.

Prompt Templates:

Prompt templates are the primary input given to the LLMs to effectively get the solutions from the LLMs

Asking clear and concise questions. Provide relevant context to the question to help narrow down the scope of the answer.
Use language that is consistent with the language of the answer you’re seeking.

Indexing:

Indexing refers to ways to structure documents/texts so that LLMs can best interact with them for extracting useful information to work with.

Memories:

Memories in LLM are used to store, remember, and retrieve the previous data that the user has interacted with to complete a task.

Chains:

Chains in Langchain are used to connect one or more LLMs to work to an input eventually bringing out the solution precisely.

Types of chains in Langchain:

There are two types of chain used in Langchain

Simple sequential chain
General form of sequential chain
Simple sequential chain:

A simple sequential chain is a series of chains connected to each other sequentially to produce an output for a particular prompt. Here in a simple sequential chain, the output of one LLM is given as an input to another LLM.

General form of sequential chain:

It is the exact opposite of the simple sequential chain as multiple inputs and multiple outputs are given to LLM.

Agents:

Agents are typically API calls that allow the LLMs to connect to external data on the internet.

A typical example of this is when we prompt the LLM to do a simple or complex task such as 7.2**8.4 the output of LLM will be an approximate number resulting to the prompt where as the output is nowhere near the original output. So with the help of the agents, it is possible to overcome this issue.

Applications of Langchain:

1. Text Summarization tool

2. Sentiment Analysis

3. Q/A Answering System

4. Chatbots

Conclusion:
Large language models (LLMs) are a powerful new type of artificial intelligence that can be used to create various applications. LangChain is an open-source framework that makes it easier to develop LLMs applications.

LLMs and LangChain are still under development, but they have the potential to revolutionize the way we interact with computers. As these technologies mature, we can expect to see even more powerful and innovative applications that use LLMs.


## Authors

- [@Karthik](https://impartial-wealth-154607.framer.app/projects)


## License

[MIT](https://choosealicense.com/licenses/mit/)


