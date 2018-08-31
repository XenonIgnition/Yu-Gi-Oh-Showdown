@echo off
setlocal
Echo Opening Terminal in Yu-Gi-Oh Directory
cd C:\Users\Xenonheat\Dropbox\Adesina Projects\Yu-Gi-Oh\scripts\spiders\
cd tutorial\
scrapy crawl yugioh -o yugioh.json
pause