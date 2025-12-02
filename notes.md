## Links

- [Tecplot Docs website](https://tecplot.com/documentation/)
- [Tecplot 360 User Manual](https://tecplot.azureedge.net/products/360/2013r1m1/adkum.pdf)
- [Tecplot 360 ADK Reference](https://tecplot.azureedge.net/products/360/2013r1m1/adkrm/index.html)
- [PyTecplot Docs](https://tecplot.azureedge.net/products/pytecplot/docs/index.html#)
- [Tecplot 360 Macro Scripting Guide](https://tecplot.azureedge.net/products/360/current/360-scripting-guide.pdf)

## Getting local copy of PyTecplot docs for Copilot

Downloaded [PyTecplot docs](https://tecplot.azureedge.net/products/pytecplot/docs/index.html#) using wget command from [this SO answer](https://superuser.com/a/1358488):

```sh
wget -r -np -l 2 -A html https://tecplot.azureedge.net/products/pytecplot/docs/index.html#
```

Then converted everything to markdown using a pandoc command from [this gist](https://gist.github.com/bzerangue/2504041):

```sh
find . -name "*.ht*" | while read i; do pandoc -f html -t markdown "$i" -o "${i%.*}.md"; done
```

Then cleaned up html files (deleted them) with this command from [this SO answer](https://askubuntu.com/a/377442):

```sh
find . -name "*.ht*" -type f -delete
```