from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.retrievers import WikipediaRetriever
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

import os

import requests

from flask import Flask, render_template, redirect, url_for, request

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

retriever = WikipediaRetriever()


def summarize_wiki(query: str) -> str:
    results: list[str] = [i.page_content for i in retriever.invoke(query)]
    prompt_list = [
		("system", "You are a helpful assistant"),
		("user", "Can you help me summarize information about {query}? Based on the info?")
	]
    
    for info in results:
        prompt_list.append(
			("user", info)
		)
        
    prompt = ChatPromptTemplate.from_messages(prompt_list).invoke({"query": query})
    return llm.invoke(prompt).content
