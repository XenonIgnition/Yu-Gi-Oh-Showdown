@echo off
setlocal
Echo Opening Terminal in Yu-Gi-Oh Directory
cd C:\Users\Xenonheat\Dropbox\Adesina Projects\Yu-Gi-Oh\scripts\spiders\
cd tutorial\
scrapy shell "https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=1&sess=1&keyword=&stype=1&ctype=&starfr=&starto=&pscalefr=&pscaleto=&linkmarkerfr=&linkmarkerto=&link_m=2&atkfr=&atkto=&deffr=&defto=&othercon=2"
pause