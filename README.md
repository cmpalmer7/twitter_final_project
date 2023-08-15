# twitter_final_project

## Purpose

This program will allow you to pull 100 recent tweets based on keyword in order to better understand current sentiment about a topic in real time. All tweets returned are from the last seven days. 

## Set up

You will need to obtain a bearer token from the twitter API in order to pull tweets from the service. The free level does not allow for searching of current tweets. You will need at least basic access. 

Once you have the key, add it to your .env file like this

```sh
BEARER_TOKEN="KEY HERE"
```

Create a virtual environment:


```sh
conda create -n tweets-env python=3.10
```

Activate the environment: 

```sh
conda activate tweets-env
```

Install third-party packages:

```sh
pip install -r requirements.txt
```

## Usage

Run the tweet report:

```sh
python -m app.tweets
```

## Testing

```sh
pytest
```