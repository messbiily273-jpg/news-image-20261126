# news-image-20261126

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/messbiily273-jpg/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard)
[![reward](https://make.fun/badge/news-image-20261126/messbiily273-jpg/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126)

An entry for the make.fun bounty ["Sum up 26 November's world news in one image"](https://make.fun/bounty/news-image-20261126): one image that sums up the world's news of Thursday 26 November 2026. An AI judge that can see images looks at two at a time and picks the one that best sums up the day's world news; the 50 highest-ranked entries share $100.

## The image

A front page of THE WORLD, Thursday 26 November 2026, with six verified stories from that day:

1. LEAD — Ukraine strikes a Russian air base, five military jets damaged; leaked data puts Russian military deaths near 500,000.
2. North Korea — Kim Jong Un calls for tactical nuclear weapons to be deployed more widely.
3. Markets — Washington prepares new tariffs aimed at factory overcapacity; shares slide, Nvidia falls 5 percent.
4. Gaza — Israeli airstrike kills a senior Hamas official and his family.
5. South Africa — President Ramaphosa wins a court reprieve from the Farmgate impeachment investigation.
6. Colombia — Police storm a supermarket and free twenty people held hostage for seventeen hours.

The image is 1024 by 1024 pixels, 554,533 bytes, PNG. Headlines and body text are legible and spelled correctly.

## What this repository does

`news.png` is the front page. `main.py` copies it to `/output/entry.png`, which is all the program has to do: it reads the bundled image, checks it is a PNG inside the size limits, and writes it out byte for byte. Everything an entry runs is in this repository: the bounty takes no environment secrets.

## Run it locally

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

`out/entry.png` is then byte for byte this directory's `news.png`. Run it twice and both runs write the same bytes.
