#!/usr/bin/python3
"""Fetch posts from JSONPlaceholder and process them."""

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts and print titles."""
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        data = response.json()

        for post in data:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch posts and save them into a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        posts_list = []

        for post in data:
            posts_list.append({
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            })

        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts_list)
