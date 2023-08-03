# URL-Shortner

## What is a URL shortening service?
A URL shortening service is a website that substantially shortens a Uniform Resource Locator (URL). The short URL redirects the client to the URL of the original website. Some popular public-facing URL shortening services are tinyurl.com and bitly.com1.

## How does a URL shortener work?
At a high level, the URL shortener executes the following operations:
1. The server generates a unique short URL for each long URL
2. The server encodes the short URL for readability
3. The server persists the short URL in the data store
4. The server redirects the client to the original long URL against the short URL

- The reasons to shorten a URL are the following:
1. Track clicks for analytics
2. Disguise the underlying URL for affiliates
3. Some instant messaging services limit the count of characters on the URL

## Requirements
- Functional Requirements
1. URL shortening Service similar to TinyURL, or Bitly
2. A client (user) enters a long URL into the system and the system returns a shortened URL
3. The client visiting the short URL must be redirected to the original long URL
4. Multiple users entering the same long URL must receive the same short URL (1-to-1 mapping)
5. The client should be able to choose a custom short URL 
6. The short URL should be readable
7. The short URL should be collision-free
8. The short URL should be non-predictable
9. The short URL should be web-crawler friendly (SEO)
10. The short URL should support analytics (not real-time) such as the number of redirections from the shortened URL
11. The client optionally defines the expiry time of the short URL

- Non-Functional Requirements
1. High Availability
2. Low Latency
3. High Scalability
4. Durable
5. Fault Tolerant

   
