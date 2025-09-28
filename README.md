# VTHacks13

## group members

| Name          | GitHub username | discord username |
| ------------- | --------------- | ---------------- |
| Can Pekkan    | C4N-6           | the_pateto_man   |
| Awab Eltigani | AwabEltigani    | remontadaaaa     |
| Calvin        | CalvinAHarr     | charriott03      |
| Dylan Cerrudo | DylanCerrudo    | dylancerrudo     |

## Inspiration

When Calvin took Data Structures and Algorithms, he had a habit of waiting until the weekend to do the projects. He also waited until then to check Piazza for insights on problems to avoid. This meant that whenever he did open Piazza, he would see a flood of posts that it would be too cumbersome to sift through when he had a specific problem. After all, he didn't want to bother the TA's with a question they already answered. If only there was a way to save time here!

## What it does

Piazza Answers is an AI chatbot that uses Piazza posts and responses as context to answer questions specific to questions on class projects.

## How we built it

We used the [unofficial piazza api](https://github.com/hfaran/piazza-api) to get piazza post, we read the terms and service and it said not to show any personal identifiable information. our program then sends those post to Gemini to answer the prompt. we where planing on sorting the responses based on the confidence values, but it turns out that Gemini dose not give confidence values. so we decided to sort the piazza posts based on how many keywords of the prompt it used. this is not the best solution but is a good compromise to finish this project in time.

## Challenges we ran into

On the frontend side, I faced the challenge of displaying the question on the page after entering it into the textbox and making sure that the answer was able to be displayed.

## Accomplishments that we're proud of

Getting connected to the Gemini API from the frontend.

## What we learned

Inspired by teammates, Calvin learned not to use vibe coding as a crutch. Instead, he tries to understand what the AI is coding and using that as a reference for what the project.

## What's next for Piazza Answers
